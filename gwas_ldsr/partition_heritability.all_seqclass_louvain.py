import os
import sys


DATA_DIR = './data'
OUT_DIR = './sei_data/ukbb_heritability/'


if __name__ == '__main__':
    sumstats_file = sys.argv[1]
    in_dir = sys.argv[2]

    prefix, dirname = os.path.split(in_dir)
    if len(dirname) == 0:
        _, dirname = os.path.split(prefix)
    out_subdir = os.path.join(OUT_DIR, dirname)
    if not os.path.isdir(out_subdir):
        os.makedirs(out_subdir)

    print(sumstats_file, in_dir, out_subdir)
    os.system(
        ('python ./ldsc/ldsc.py '
         '--h2 {0} '
         '--ref-ld-chr {1}/@ '
         '--w-ld-chr {4}/weights_hm3_no_hla/weights. '
         '--overlap-annot '
         '--frqfile-chr {4}/1000G_Phase3_frq/1000G.EUR.QC. '
         '--print-coefficients '
         '--print-delete-vals '
         '--out {2}/{3}\n').format(
             sumstats_file,
             in_dir,
             out_subdir,
             os.path.basename(sumstats_file),
             DATA_DIR))
