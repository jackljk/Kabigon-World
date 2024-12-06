#!/bin/bash

# Set the base directory for your project
export BASEPATH="/home/jklim/jack/personal/Kabigon-World/Anime Music Generator/src"

# Export the name of the current script
export SCRIPT_NAME=$(basename "$0")

# Run the Python script using BASEPATH
python "$BASEPATH/train.py" \
    "$@" \
    "$BASEPATH/processed_data/anime.pt" \
    "$BASEPATH/checkpoints/anime.pt" \
    "$BASEPATH/results/anime.pt" \
    100 \
    "$@"
