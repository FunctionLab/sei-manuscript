#!/bin/bash

INDIR="./sei_data/1000G_EUR_Phase3_vcfs.cluster_assignments"
for fn in $INDIR/*.annot; do
    echo $fn
    sh seqclass_louvain_all.sh $fn
done
