#!/bin/bash

cd "$(dirname "$0")"/../src

# Export the name of the current script
export SCRIPT_NAME=$(basename "$0")

# Run the Python script
python train.py "$@" \
    processed_data/anime.pt \
    checkpoints/anime.pt \
    results/anime.pt \
    100 \
    "$@"
    Anime Music Generator\src\processed_data