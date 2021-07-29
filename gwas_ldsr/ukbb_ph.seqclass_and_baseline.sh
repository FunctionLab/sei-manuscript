#!/bin/bash

LDSR_DIR=$1
for fn in ./data/UKBB/*formatted.sumstats; do
    for ((i=0; i<40; i++)); do
        python -u partition_heritability.seqclass_and_baseline.py $fn $i $LDSR_DIR
    done
done

