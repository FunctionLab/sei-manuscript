# Evolutionary constraints

To avoid downloading large files multiple times over, we excluded a directory from `sei_data` in the `evolutionary_constraints` data `.tar.gz` that is required to run the Jupyter notebooks, called `1000G_EUR_seqclass_scores`. The data is included in the `.tar.gz` for the `eQTL_effect_sizes`. From the top-level directory of the Github repository, run the following commands:

```
wget https://sei-files.s3.amazonaws.com/eQTL_effect_sizes.tar.gz
tar -xzvf eQTL_effect_sizes.tar.gz
cd evolutionary_constraints/sei_data
ln -s ../../eQTL_effect_sizes/sei_data/1000G_EUR_seqclass_scores .
```

before proceeding to run the Jupyter notebooks.


