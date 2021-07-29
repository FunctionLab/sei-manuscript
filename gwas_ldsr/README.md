# LD score regression on sequence classes

We provide the Python scripts needed to run LDSR with sequence class annotations and the Jupyter notebook used to generate the figures/supplementary files in the manuscript.

## Requirements
The Python scripts need to be run with with Python 2.7, because the `ldsc` tool is written in Python 2.7. The notebook is written in R.  

Download [`ldsc`](https://github.com/bulik/ldsc) into this directory (or symlink to this dir), according to the instructions in the LDSC github repository. 

## Scripts

Writing the per-chromosome LDSR annotation files using sequence classes (annotations are based on the Louvain community clustering whole-genome sequence assignments):
```
sh all_files.seqclass_louvain_all.sh
```

Writing the per-chromosome LDSR annotation files using sequence classes and LDSR v2.2 baseline annotations:
```
sh all_files.seqclass_with_baseline.sh
```

Run LDSR, for only sequence class annots:
```
sh run_ldsr.all_seqclass_louvain.sh
```

LDSR for sequence class + baseline annots:
```
sh run_ldsr.seqclass_and_baseline.sh <seq-class>
```
where `<seq-class>` is a number from 0-40 (the index of each sequence class)

Partitioning heritability, for only sequence class annots:
```
sh ukbb_ph.all_seqclass_louvain.sh ./sei_data/ldsr_annotations/seqclass_louvain_all
```

Partitioning heritability for sequence class + baseline annots:
```
sh ukbb_ph.seqclass_and_baseline.sh ./sei_data/ldsr_annotations/seqclass_and_baseline
```


