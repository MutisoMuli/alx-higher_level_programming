#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the size of the body of the response
body_size=$(curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')

# Display the size in bytes
echo "$body_size"
