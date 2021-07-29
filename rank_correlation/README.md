# Rank correlation structure comparison

This directory generates Supplementary Figure 3: the rank-transform of pairwise Spearman correlations for the 21,907 chromatin profiles predicted by Sei show that Sei predictions share a highly similar correlation structure with the experimental observations.


To avoid downloading large files multiple times over, we excluded a file from `sei_data` in the `rank_correlation` data `.tar.gz` that is required to run the Python scripts, called `test_predictions.h5`. This file is provided in `performance_curves.tar.gz`. Please run the following commands from the top-level directory of the Github repository:

```
wget https://sei-files.s3.amazonaws.com/performance_curves.tar.gz
tar -xzvf performance_curves.tar.gz
cd rank_correlation/sei_data
ln -s ../../performance_curves/sei_data/test_predictions.h5 .
```

### Running the code

Get the correlation-coefficient matrices for targets and predictions (can be run in parallel)

```
python -u get_targets_corrcoef.py
python -u get_seipred_corrcoef.py
```

Run `visualize_rankcorr_heatmap.py` for each correlation-coefficient matrix: 

```
python -u visualize_rankcorr_heatmap.py ./sei_data/tgts.test-2m.corrcoef.npy tgts.test-2m.png
python -u visualize_rankcorr_heatmap.py ./sei_data/sei_preds.test-2m.corrcoef.npy sei_preds.test-2m.png
```
