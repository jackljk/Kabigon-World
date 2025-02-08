# Anime Music Generator

This project was inspired by a lecture from MUS 7 in UCSD, where we learnt about AI Gen Music pieces from artist. Which prompted me to train a model for myself, using anime music to create tunes that sound like they could come from an Anime Opening. 

## How to use
To generate music, `cd` into `src` folder and run this command
```
python generate.py "results/anime_large.pt" ".../save_path/{file_name}.mid 
```
Some keywords you could use to modify the music generation are:

- `-c, --compile`: (Flag) If specified, the model will be `torch.compile`d for potentially better speed. Default: `False`.
- `-m, --mode`: Specify the decoding mode. Options:
  - `'categorical'`
  - `'argmax'`
- `-k, --top-k`: Top `k` samples to consider during decode sampling. Default: `all`. (Must be a positive integer.)
- `-t, --temperature`: Temperature for decode sampling:
  - Lower values: More confident (deterministic) sampling.
  - Higher values: More diverse sampling. Default: `1.0`.
- `-tm, --tempo`: Approximate tempo of the generated sample in BPM. (Must be a positive integer.)
- `-i, --midi-prompt`: Path to a MIDI file. If specified, the program will generate music that continues the input MIDI file.
- `-it, --midi-prompt-tokens`: Number of tokens to sample from the MIDI prompt as a prefix for continuation. (Requires `--midi-prompt`.)
- `-v, --verbose`: (Flag) Enable verbose output for more detailed information during execution.


## TODOs
- [x] Train baseline models (Transformer Model)
- [ ] Incorporate more than just piano tunes 
    - [ ] AI Generated Lyrics ?
    - [ ] More instruments
- [ ] Different architetures 

## Acknowledgments

This project uses the Transformer architecture from [music-transformer](https://github.com/spectraldoy/music-transformer) as a foundational model. Special thanks to the creators of the repository for providing an excellent implementation, which was instrumental in training my anime music generator.

If you're interested in their work, please check out their repository for more details on the original implementation.