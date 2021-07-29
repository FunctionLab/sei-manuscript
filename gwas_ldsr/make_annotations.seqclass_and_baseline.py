import os
import sys

import numpy as np
import pandas as pd


DATA_DIR = './data'
SEI_DIR = './sei_data'
OUT_DIR = os.path.join(
    SEI_DIR, 'ldsr_annotations', 'seqclass_and_baseline')



if __name__ == '__main__':
    sc_fp = sys.argv[1]
    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)

    chrom = os.path.basename(sc_fp).split('.')[0]

    base_annots = os.path.join(
        DATA_DIR,
        '1000G_Phase3_baselineLD_ldscores_v2.2',
        'baselineLD.{0}.annot.thin'.format(chrom))

    seqclass_louvain = np.loadtxt(sc_fp)
    sc_mat = np.zeros((40, len(seqclass_louvain)))
    for c in range(40):
        sc_mat[c][seqclass_louvain == c] = 1

    for c in range(sc_mat.shape[0]):
        fp = os.path.join(
            OUT_DIR, '{0}.state{1}.C_{1}.annot'.format(chrom, c))
        if os.path.exists(fp):
            print('skip', fp)
            continue
        sc_preds = sc_mat[c]

        df = pd.read_csv(base_annots, sep='\t')
        df.insert(0, 'C{0}_REF'.format(c), sc_preds)
        df.insert(1, 'base', [1] * len(df))
        df.to_csv(fp,
                  sep='\t',
                  index=False,
                  header=True)


