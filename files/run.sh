#!/bin/bash

DEPLOYMENT_FOLDER='<deployment_folder>'

source $DEPLOYMENT_FOLDER/venv/bin/activate

gunicorn app:application \
         --bind 127.0.0.1:<port> \
         --workers 2 \
         --threads 2