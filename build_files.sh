#!/bin/bash
echo "BUILD STARTED"

# Upgrade pip first
python3.9 -m pip install --upgrade pip

# Install requirements
python3.9 -m pip install -r requirements.txt

# Run migrations
python3.9 manage.py migrate --noinput

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
