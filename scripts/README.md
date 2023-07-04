# How-to
`run_training.py` automates the training of a, by default, 1 layer, 128 dimensional transformer that learns to detect valid sequences of moves. A standard invocation of this script will look like `python3 run_training.py "<experiment name>" "<dataset>"`, or, with actual variable values: `python3 run_training.py "all games test" "all"`. Check out line 126 in `run_training.py` for all the options.

By default, this script will save model and training checkpoints in the `scripts` folder under the given experiment name. You can add `--fine_tune "<previous_experiment>.pt"` to fine tune on an already run model, or do `--fine_tune "recent"` to fine-tune the most recently saved model.  