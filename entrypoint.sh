#!/bin/bash

# Check if there are any model files
if [ ! -f "/app/models/*.tar.gz" ]; then
  echo "No valid model found. Training a new model..."
  rasa train
else
  echo "Model found. Skipping training."
fi

# Start Rasa server
rasa run --enable-api --cors "*" --debug
