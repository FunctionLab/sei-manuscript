# Sei Framework manuscript code

This repository contains code to generate the results from the manuscript, "A sequence-based global map of regulatory activity for deciphering human genetics." 

## Overview

We have organized the repository by analysis. For example, `enrichment_heatmaps` contains the code/notebooks to generate all log fold-change enrichment heatmaps in the manuscript (Fig 2a, Supplementary Figs 5-11). 

This code has been tested on Python 3.6, and includes a number of Python scripts and Python/R Jupyter notebooks. Please set up a conda environment, install the packages listed in the `requirements.txt` file, and also install the R kernel for Jupyter notebook. Example commands:

```
conda create --name=sei-manu python=3.6
conda install jupyter
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=sei-manu
conda install -c r r-irkernel
conda install --file requirements.txt -c anaconda -c conda-forge -c bioconda -c pytorch -c intel
```

Some of the python notebooks also call R with rpy2, therefore the R dependencies need to be installed. The R package dependencies are `data.table`, `ggplot2`, `ggrepel`, `patchwork`, `shades`, and `plyr`. 

## Data

Additionally, run

```
sh ./download_data.sh
```

to get the data and resource files used in these analyses. **NOTE**: `download_data.sh` contains the commands to download data for ALL the analyses in this repository, which can total around 1TB or more. We have commented out all analysis-specific downloads by default, and highly recommend you review the memory requirements for each analysis in the `download_data.sh` file before deciding to download anything. 

Each directory may also have its own README you should refer to before running any of the scripts/notebooks provided. 

### Sequence Classes

If you are interested in running the Sei framework on your own list of variants, you can refer to the [sei-framework](https://github.com/FunctionLab/sei-framework) repository. 

We also provide some additional resources in [https://sei-files.s3.amazonaws.com/resources.tar.gz](https://sei-files.s3.amazonaws.com/resources.tar.gz) which can be used for reproducing or adapting the analyses we described in the manuscript. As mentioned earlier, you can refer to `download_data.sh` to get analysis-specific data files.

The files in `resources`: 
- Sei model: `sei.py`, `sei.pth`
- Chromatin profiles: `sei_chromatin_profiles.txt` (`sei_profiles*.npy` are the NumPy-loadable versions of this file) 
- Sequence class names: `cnames.tsv`
- Computing sequence class scores (see methods): `histone_inds.npy` (histone normalization), projection `projvec_targets.npy`
- Louvain community clustering sequence class assignments\*: `seqclass_louvain_wgt.npy` and corresponding coordinates `genome_coordinates.seqclass_louvain_wgt.txt`
- Genome-wide sequence class annotations (hg38)\*: `hg38.seqclass_annotation.bed`

\*Note: We provide the annotations for all 61 clusters output by Louvain community clustering. Our manuscript only focuses on the largest 40 sequence classes (see methods), but you can refer to Supplementary Figure 19 for an interpretation of clusters 40-61, which mostly have low enrichment or are enriched in repeats.   

## Code for results/figures

The directories correspond to the following figures/analyses:
- `visualize_genome`: Visualization of human genome sequences across the whole-genome (Fig 1)
- `enrichment_heatmaps`: Log fold-change enrichment heatmaps (Fig 2a, Supplementary Figs 5-11)
- `enhancer_gene_expr`: Enhancer sequence classes near TSS are correlated with relevant cell-type-specific gene expression (Fig 2b)
- `eQTL_effect_sizes`: Sequence class-level variant effects are predictive of directional GTEx variant gene expression effects (Fig 2c)
- `evolutionary_constraints`: Regulatory sequence classes are under evolutionary constraints (Fig 3, Supp Fig 13); contains R notebook
- `gwas_ldsr`: UKBB GWAS heritability analysis (Fig 4, Supp Files 4 and 5); this is a R notebook
- `pathogenic_mutations`: Sequence class predictions for disease regulatory mutations (Fig 5, Supp Fig 14, Supp file 6); this is a R notebook
- `performance_curves`: Sei chromatin profile model performance (Supp Fig 2, Supp File 2);
- `rank_correlation`: Correlation structure of Sei model predictions matches the correlation structure of the targets (Supp Fig 3)
- `sei_vs_beluga_comparison`: Model performance for Sei and DeepSEA Beluga models on the overlapping set of 2,002 chromatin profiles (Supp Fig 4)

## Help
Please post in the Github issues or e-mail Kathy Chen (chen.kathleenm@gmail.com) with any questions about the repository, requests for more data, additional information about the results, etc.  
