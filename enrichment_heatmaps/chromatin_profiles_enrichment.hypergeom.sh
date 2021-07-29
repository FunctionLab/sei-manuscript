#!/bin/bash

for ((i=0; i<40; i++)); do
    python -u chromatin_profiles_enrichment.hypergeom.py $i
done
