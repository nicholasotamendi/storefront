#!/bin/bash

# Exit on error
set -e

pip3.12 install -r requirements.txt
python3.12 manage.py collectstatic --noinput

# Create database tables
python3.12 manage.py migrate