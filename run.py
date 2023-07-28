#!/usr/bin/python3
import os
import uvicorn
from api.v1.app import app

if __name__ == "__main__":
    uvicorn.run("run:app", port=5000, log_level="info", reload=True)