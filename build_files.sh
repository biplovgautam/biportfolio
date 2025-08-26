#!/bin/bash
echo "BUILD STARTED"

# Set Python version
PYTHON_VERSION="python3.11"

# Check if Python 3.11 is available, fallback to python3
if command -v python3.11 &> /dev/null; then
    PYTHON_CMD="python3.11"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    echo "No suitable Python version found"
    exit 1
fi

echo "Using Python: $PYTHON_CMD"

# Upgrade pip first
$PYTHON_CMD -m pip install --upgrade pip

# Install requirements
$PYTHON_CMD -m pip install -r requirements.txt

# Run migrations
$PYTHON_CMD manage.py migrate --noinput

# Collect static files
$PYTHON_CMD manage.py collectstatic --noinput --clear

echo "BUILD END"
