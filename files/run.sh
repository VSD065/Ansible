#!/bin/bash

# Ensure the deployment folder variable is set
DEPLOYMENT_FOLDER="/opt/example"
PORT="5000"
# Activate the virtual environment
source $DEPLOYMENT_FOLDER/venv/bin/activate

# Start the application using gunicorn
gunicorn app:application \
         --bind 0.0.0.0:$PORT \
         --workers 2 \
         --threads 2


