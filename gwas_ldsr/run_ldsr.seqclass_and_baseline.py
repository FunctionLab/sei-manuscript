import os
import sys


DATA_DIR = './data'
BIM_DIR = os.path.join(DATA_DIR, '1000G_EUR_Phase3_plink')
HAPMAP_DIR = os.path.join(DATA_DIR, 'hapmap3_snps')

ANNOT_DIR = './sei_data/ldsr_annotations/seqclass_and_baseline'


if __name__ == '__main__':
    seqclass = sys.argv[1]
    for chrom in range(1, 23):
        print('Processing chrom {0}, sequence class {1}'.format(
            chrom, seqclass))
        annot_fp = os.path.join(
            ANNOT_DIR, '{0}.state{1}.C_{1}.annot'.format(chrom, seqclass))
        prefix = os.path.join(ANNOT_DIR, '{0}.state{1}.C_{1}'.format(
            chrom, seqclass))

        if os.path.isfile(prefix + '.l2.ldscore.gz'):
            print('skipping', prefix)
            continue

        os.system(
            ('python ./ldsc/ldsc.py '
             '--l2 '
             '--bfile {0}/1000G.EUR.QC.{1} '
             '--ld-wind-cm 1 '
             '--annot {2} '
             '--thin-annot '
             '--out {3} '
             '--print-snps {4}/hm.{1}.snp').format(
                 BIM_DIR, chrom, annot_fp, prefix, HAPMAP_DIR))
