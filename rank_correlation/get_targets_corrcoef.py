import os

import h5py
import numpy as np


SEI_DIR = './sei_data'
TGT_FILE = os.path.join(SEI_DIR, 'test_predictions.h5')


if __name__ == '__main__':
    mat = h5py.File(TGT_FILE, 'r')['targets'][()].T
    np.save(os.path.join(SEI_DIR, 'tgts.test-2m.corrcoef.npy'), np.corrcoef(mat))
