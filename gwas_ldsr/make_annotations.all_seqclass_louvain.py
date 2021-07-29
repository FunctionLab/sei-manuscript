import os
import sys

import numpy as np
import pandas as pd


SEI_DIR = './sei_data'
OUT_DIR = os.path.join(
    SEI_DIR, 'ldsr_annotations', 'seqclass_louvain_all')


if __name__ == '__main__':
    sc_fp = sys.argv[1]
    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)

    chrom = os.path.basename(sc_fp).split('.')[0]

    seqclass_louvain = np.loadtxt(sc_fp)
    sc_mat = np.zeros((40, len(seqclass_louvain)))
    for c in range(40):
        sc_mat[c][seqclass_louvain == c] = 1

    df = pd.DataFrame(sc_mat.T.astype(int))
    df.columns = ['C{0}_REF'.format(c) for c in df.columns]
    df.insert(0, 'base', [1] * len(df))
    df.to_csv(os.path.join(OUT_DIR, '{0}.annot'.format(chrom)),
              sep='\t',
              index=False,
              header=True)


