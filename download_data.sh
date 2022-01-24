#!/bin/bash

# MUST download `resources`  3GB .tar.gz, 4GB decompressed
wget https://sei-files.s3.amazonaws.com/resources.tar.gz
tar -xzvf resources.tar.gz

# For the remaining .tar.gz files, you can download based on
# which analyses you want to run, keeping in mind the storage
# requirements for this data.

# 76MB .tar.gz, 101MB decompressed
# wget https://sei-files.s3.amazonaws.com/enhancer_gene_expr.tar.gz
# tar -xzvf enhancer_gene_expr.tar.gz

# 390MB .tar.gz, 41GB decompressed
# wget https://sei-files.s3.amazonaws.com/enrichment_heatmaps.tar.gz
# tar -xzvf enrichment_heatmaps.tar.gz

# 108GB .tar.gz, 115GB decompressed
# wget https://sei-files.s3.amazonaws.com/eQTL_effect_size.tar.gz
# tar -xzvf eQTL_effect_sizes.tar.gz

# 432MB .tar.gz
# wget https://sei-files.s3.amazonaws.com/evolutionary_constraints.tar.gz
# tar -xzvf evolutionary_constraints.tar.gz

# 39GB .tar.gz, 134GB decompressed
# wget https://sei-files.s3.amazonaws.com/gwas_ldsr.tar.gz
# tar -xzvf gwas_ldsr.tar.gz

# 622KB .tar.gz, 5.6MB decompressed
# wget https://sei-files.s3.amazonaws.com/pathogenic_mutations.tar.gz
# tar -xzvf pathogenic_mutations.tar.gz

# 186GB .tar.gz, 612GB decompressed
# wget https://sei-files.s3.amazonaws.com/performance_curves.tar.gz
# tar -xzvf performance_curves.tar.gz

# 8GB .tar.gz, 7GB decompressed
# wget https://sei-files.s3.amazonaws.com/rank_correlation.tar.gz
# tar -xzvf rank_correlation.tar.gz

# 12GB .tar.gz, 5GB decompressed
# wget https://sei-files.s3.amazonaws.com/sei_vs_beluga_comparison.tar.gz
# tar -xzvf sei_vs_beluga_comparison.tar.gz

# 209GB .tar.gz, 218GB decompressed
# wget https://sei-files.s3.amazonaws.com/visualize_genome.tar.gz
# tar -xzvf visualize_genome.tar.gz
