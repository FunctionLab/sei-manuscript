#!/bin/bash

INDIR="./sei_data/1000G_EUR_Phase3_vcfs.cluster_assignments"
for fn in $INDIR/*.annot; do
    echo $fn
    sbatch seqclass_with_baseline.sh $fn
done
