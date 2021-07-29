import os
import sys

import h5py
import numpy as np
import pandas as pd
from scipy.stats import fisher_exact


RESOURCES_DIR = '../resources'
SEI_DIR = './sei_data'

CASSIGN_FILE = os.path.join(RESOURCES_DIR, 'seqclass_louvain_wgt.npy')
sclass_assign = np.load(CASSIGN_FILE)


CHROM_PROFILES_FILE = os.path.join(RESOURCES_DIR, 'sei_profiles.npy')
chromatin_profiles = np.load(CHROM_PROFILES_FILE)

TGTS_FILE = os.path.join(SEI_DIR, 'hg38.tiling.randsort.aa.targets.h5')
TGTS_ROWLABELS_FILE = os.path.join(SEI_DIR, 'hg38.tiling.randsort.aa.row_labels.txt')

OUTDIR = os.path.join(SEI_DIR, 'fisher_exact')
os.makedirs(OUTDIR, exist_ok=True)


if __name__ == '__main__':
    sequence_class = int(sys.argv[1])
    print('Running for sequence class {0}'.format(
        sequence_class))

    targets = h5py.File(TGTS_FILE, 'r')['targets']
    targets_row_labels = pd.read_csv(TGTS_ROWLABELS_FILE, sep='\t')

    targets = np.array(targets)[~targets_row_labels['contains_unk']]

    sclass_profile_pvalues = np.zeros(targets.shape[1])
    sclass_profile_oddsratio = np.zeros(targets.shape[1])

    in_sclass = targets[
        sclass_assign[:targets.shape[0]] == sequence_class, :]
    out_sclass = targets[
        sclass_assign[:targets.shape[0]] != sequence_class, :]

    for ix in range(targets.shape[1]):
        in_sclass_and_tgt = len(np.where(
            in_sclass[:, ix] == 1)[0])
        in_sclass_and_no_tgt = len(np.where(
            in_sclass[:, ix] == 0)[0])
        in_tgt_and_no_sclass = len(np.where(
            out_sclass[:, ix] == 1)[0])
        no_tgt_and_no_sclass = len(np.where(
            out_sclass[:, ix] == 0)[0])

        oddsratio, pval = fisher_exact(
            np.array([[in_sclass_and_tgt, in_tgt_and_no_sclass],
                      [in_sclass_and_no_tgt, no_tgt_and_no_sclass]]))
        sclass_profile_oddsratio[ix] = oddsratio
        sclass_profile_pvalues[ix] = pval

    np.save(os.path.join(OUTDIR, '{0}.pvalues.npy'.format(
        sequence_class)), sclass_profile_pvalues)
    np.save(os.path.join(OUTDIR, '{0}.oddsratio.npy'.format(
        sequence_class)), sclass_profile_oddsratio)


