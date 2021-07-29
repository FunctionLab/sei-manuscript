# Figure 2b notebook

`gene_expression.ipynb` is the notebook used to generate Figure 2b, showing that enhancer sequence class annotations near gene TSSs are correlated with cell-type-specific gene expression. 

## `data` directory
- `geneanno.exp.csv`: The cell-type-specific gene expression data
- `geneanno.hg19.csv`: The gene CAGE TSS coordinates
(both files use hg19 coordinates)

## `sei_data` directory
- `sorted.hg19.tiling.bed.ipca_randomized_300.labels.merged.bed.gz` and the associated index `.tbi` file (uses the `pytabix` package). This is the lifted over sequence class annotations for the whole genome (based on Louvain community clustering, original sequences were in hg38). For anyone who wishes to use this file for their own application, any overlapping sequence class annotations as a result of liftover can be skipped.

## `figures` directory
The generated figure. 
