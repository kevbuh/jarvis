#!/bin/sh

python3 buddy/audio.py
wait
source /Users/kevinbuhler/opt/anaconda3/etc/profile.d/conda.sh
wait
conda activate base
wait
python3 buddy/text.py
