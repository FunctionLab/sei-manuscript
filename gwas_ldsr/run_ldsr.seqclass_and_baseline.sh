#!/bin/bash
#SBATCH --partition=ccb
#SBATCH --time=1-00:00:00
#SBATCH --mem=100G
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=kchen@flatironinstitute.org

echo $1
python -u run_ldsr.seqclass_and_baseline.py $1
