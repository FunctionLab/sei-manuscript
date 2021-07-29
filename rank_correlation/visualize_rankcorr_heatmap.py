import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import rankdata
import seaborn as sns


SEI_DIR = './sei_data'
FIGS_DIR = './figures'
SEI_PROFILES = np.load('../resources/sei_profiles.npy')

ORDERING = np.load(os.path.join(
    SEI_DIR, 'sei_preds.clustermap.cols_reord.npy'))


if __name__ == '__main__':
    mat = np.load(sys.argv[1])
    outfile = os.path.join(FIGS_DIR, sys.argv[2])

    mat = mat[ORDERING][:, ORDERING]
    rankmat = rankdata(mat).reshape(mat.shape)

    df = pd.DataFrame(rankmat)
    df.columns = SEI_PROFILES
    df.rename(index={i: l for (i, l) in enumerate(SEI_PROFILES)},
              inplace=True)

    sns.set(font_scale=0.10)
    plt.figure(figsize=(14, 12))
    ax = sns.heatmap(df, xticklabels=48, yticklabels=48,
                     cbar_kws={'shrink': 0.2})
    plt.tight_layout()
    plt.savefig(outfile, dpi=600)


