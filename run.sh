#!/usr/bin/env sh

gcc even_biggier.c -o biggier

ARG_COUNT=16 ARG_LEN=1000 PROC_COUNT=1000 USE_BIGGIER=true ./biggie.py
