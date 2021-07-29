import os

import h5py
import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import seaborn as sns


SEI_DIR = './sei_data'
SEIPRED_FILE = os.path.join(SEI_DIR, 'test_predictions.h5')

if __name__ == '__main__':
    mat = h5py.File(SEIPRED_FILE, 'r')['predictions'][()].T
    corrmat = np.corrcoef(mat)
    np.save(os.path.join(SEI_DIR, 'sei_preds.test-2m.corrcoef.npy'),
            corrmat)

    df = pd.DataFrame(corrmat)
    cm = sns.clustermap(df)

    assert np.all(
        cm.dendrogram_row.reordered_ind ==
        cm.dendrogram_col.reordered_ind), \
        'row and col hclust are not equivalent'
    np.save(os.path.join(SEI_DIR, 'sei_preds.clustermap.cols_reord.npy'),
            cm.dendrogram_col.reordered_ind)




