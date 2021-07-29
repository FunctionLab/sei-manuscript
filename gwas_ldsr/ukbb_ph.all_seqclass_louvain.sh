#!/bin/bash

LDSR_DIR=$1
for fn in ./data/UKBB/*formatted.sumstats; do
    python -u partition_heritability.all_seqclass_louvain.py $fn $LDSR_DIR
done

