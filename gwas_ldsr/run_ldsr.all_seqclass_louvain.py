import os


DATA_DIR = './data'
BIM_DIR = os.path.join(DATA_DIR, '1000G_EUR_Phase3_plink')
HAPMAP_DIR = os.path.join(DATA_DIR, 'hapmap3_snps')

ANNOT_DIR = './sei_data/ldsr_annotations/seqclass_louvain_all'


if __name__ == '__main__':
    for chrom in range(1, 23):
        print('LDSR on chromosome {0}'.format(chrom))
        annot_fp = os.path.join(
            ANNOT_DIR, '{0}.annot'.format(chrom))
        prefix = os.path.join(ANNOT_DIR, str(chrom))

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
