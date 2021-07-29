import os
import sys


DATA_DIR = './data'
out_subdir = './sei_data/ukbb_heritability'


if __name__ == '__main__':
    sumstats_file = sys.argv[1]
    seqclass = sys.argv[2]
    in_dir = sys.argv[3]

    _, dirname = os.path.split(in_dir)
    out_subdir = os.path.join(out_subdir, dirname)
    if not os.path.isdir(out_subdir):
        os.makedirs(out_subdir)

    print(sumstats_file, seqclass, in_dir, out_subdir)
    os.system(
        ('python ./ldsc/ldsc.py '
         '--h2 {0} '
         '--ref-ld-chr {1}/@.state{4}.C_{4} '
         '--w-ld-chr {5}/weights_hm3_no_hla/weights. '
         '--overlap-annot '
         '--frqfile-chr {5}/1000G_Phase3_frq/1000G.EUR.QC. '
         '--print-coefficients '
         '--print-delete-vals '
         '--out {2}/{4}_{3}\n').format(
             sumstats_file,
             in_dir,
             out_subdir,
             os.path.basename(sumstats_file),
             seqclass,
             DATA_DIR))
