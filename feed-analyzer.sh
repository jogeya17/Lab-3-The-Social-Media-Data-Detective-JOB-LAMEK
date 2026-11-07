#!/bin/bash

cut -d',' -f2 twitter_dataset.csv \
| tail -n +2 \
| sort \
| uniq -c \
| sort -nr \
| head -5