#!/usr/bin/python3
import os
import uvicorn
from api.v1.app import app

if __name__ == "__main__":
    if os.getenv('MODE') == "production":
        uvicorn.run("run:app", host="0.0.0.0", port=80, log_level="info")
    else:
        uvicorn.run("run:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
