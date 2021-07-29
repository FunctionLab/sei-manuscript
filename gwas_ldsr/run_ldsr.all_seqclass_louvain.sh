#!/bin/bash
#SBATCH --partition=ccb
#SBATCH --time=1-00:00:00
#SBATCH --mem=150G
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=kchen@flatironinstitute.org

python -u run_ldsr.all_seqclass_louvain.py
