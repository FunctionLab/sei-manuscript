import os

import h5py
import numpy as np
import pandas as pd


RESOURCES_DIR = '../resources'
SEI_DIR = './sei_data'

CASSIGN_FILE = os.path.join(RESOURCES_DIR, 'seqclass_louvain_wgt.npy')
sclass_assign = np.load(CASSIGN_FILE)

CHROM_PROFILES_FILE = os.path.join(RESOURCES_DIR, 'sei_profiles.npy')
chromatin_profiles = np.load(CHROM_PROFILES_FILE)

TGTS_FILE = os.path.join(SEI_DIR, 'hg38.tiling.randsort.aa.targets.h5')
TGTS_ROWLABELS_FILE = os.path.join(SEI_DIR, 'hg38.tiling.randsort.aa.row_labels.txt')

OUTPUT_FILE = os.path.join(SEI_DIR, 'target_enrichments.aa.tsv')


if __name__ == '__main__':
    targets = h5py.File(TGTS_FILE, 'r')['targets']
    targets_row_labels = pd.read_csv(TGTS_ROWLABELS_FILE, sep='\t')

    targets = np.array(targets)[~targets_row_labels['contains_unk']]

    baseline = targets.mean(axis=0)
    np.save(os.path.join(
        SEI_DIR, 'targets_baseline_mean.npy'), baseline)

    sclass_means = []
    for sclass in np.sort(np.unique(sclass_assign)):
        sclass_means.append(np.mean(
            targets[sclass_assign[:targets.shape[0]] == sclass,:], axis=0))
    sclass_means = np.vstack(sclass_means)
    np.save(os.path.join(
        SEI_DIR, 'sclass_mean.npy'), sclass_means)

    df = pd.DataFrame(np.log2(sclass_means / baseline).T,
                      index=chromatin_profiles)
    df.to_csv(OUTPUT_FILE, sep='\t')


