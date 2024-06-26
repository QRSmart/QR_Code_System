# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config gcc libpq-dev

# Get NodeJS
COPY --from=node:18.14.0-slim /usr/local/bin /usr/local/bin
# Get npm
COPY --from=node:18.14.0-slim /usr/local/lib/node_modules /usr/local/lib/node_modules

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Copy the source code into the container.
COPY . .
COPY python_env /app/.env
COPY react_env /app/frontend/.env

WORKDIR /app/web

RUN npm install && npx tailwindcss -i ./static/css/main.css -o ./static/css/style.css

WORKDIR /app/frontend

RUN npm install && npm run build

WORKDIR /app

# Switch to the non-privileged user to run the application.
USER root

# Expose the port that the application listens on.
EXPOSE 80

# Run the application.
CMD ["python3", "run.py"]
