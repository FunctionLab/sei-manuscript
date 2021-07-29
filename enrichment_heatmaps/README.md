# Sequence class enrichment of genome annotations and chromatin profiles

## Scripts

Run the following scripts to get the Cistrome DB chromatin profile (targets) enrichment for the sequence classes, and their associated p-values by Fisher's Exact test.  

```
python -u chromatin_profiles_enrichment.py
```

```
sh chromatin_profiles_enrichment.hypergeom.sh
```

## Notebooks (run in order)
1. `sei_profile_enrichments.ipynb`: This notebook generates Supplementary Figure 11, showing the top 25 enriched Cistrome DB chromatin profiles for each sequence class. 
2. `multi_annotation_enrichments.ipynb`: Generates Figure 2a, showing the enrichment of sequence classes for various genome annotations (Cistrome DB tracks, Roadmap Epigenomics tracks, RepeatMasker centromere) 
3. `histone_mark_enrichments.ipynb`: Generates Supplementary Figures 5-10, showing histone mark enrichment across cell types, from the Roadmap Epigenomic chromatin profile tracks
