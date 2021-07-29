# Model performance comparison with DeepSEA Beluga

We compute the AUCs and AUPRCs for DeepSEA Beluga and Sei on the same holdout test sequences and chromatin profiles (2002 profiles from Roadmap and ENCODE predicted by both models). 

The test dataset is the same one used for DeepSEA Beluga's test performance evaluation in the ExPecto publication.  

We include the evaluation YAML and test datasets used in this evaluation. The config files can be used with `selene-sdk`:

```
python -m selene_sdk <config.yml>
```
