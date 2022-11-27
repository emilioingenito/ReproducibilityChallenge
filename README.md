
# Reproducibility challenge: Imputing Out-of-Vocabulary Embeddings with LOVE Makes Language Models Robust with Little Cost

This repository is the implementation of the reproducibility challenge carried out by Andrea Carotti and Emilio Ingenito in order to reproduce the main claims of the paper [Imputing Out-of-Vocabulary Embeddings with LOVE Makes Language Models Robust with Little Cost](https://arxiv.org/abs/2203.07860). 

## How to run our experiments

In order to reproduce the results of our analysis, you can exploit the Jupyter Notebook file we provided, which allows to run the analysis through a step by step procedure, as suggested by the authors. To this end, please check out the file [ReproducibilityChallenge_LOVE.ipynb](https://github.com/ckclassrooms/emilioingenito/ReproducibilityChallenge/tree/main/ReproducibilityChallenge_LOVE.ipynb). In this file you will also find charts and tables, in which we show the main results of our analysis.

## Main files

The main files of this repository - useful to run the experiments - are the following: 
* [train.py](https://github.com/emilioingenito/ReproducibilityChallenge/blob/main/train.py): this file allowed us to train the LOVE model on a specific dataset
* [produce_emb.py](https://github.com/emilioingenito/ReproducibilityChallenge/blob/main/produce_emb.py): this file geenrates the embedding for a given vocabulary
* [attacks.py](https://github.com/emilioingenito/ReproducibilityChallenge/blob/main/attacks.py): this file allowed us to corrupt the datasets (i.e. generate another dataset, from the original one, with a specific typo probability)
* [evaluate.py](https://github.com/emilioingenito/ReproducibilityChallenge/blob/main/evaluate.py): this file performs the **intrinsic task** evaluation
* [corrupt_Ner.py](https://github.com/emilioingenito/ReproducibilityChallenge/tree/main/dataset_corruption/corrupt_Ner.py): this file corrupts datasets for NER tasks (e.g. CONLL-03, BC2GM), given a specific typo probability
* [corrupt_CNN.py](https://github.com/emilioingenito/ReproducibilityChallenge/tree/main/dataset_corruption/corrupt_CNN.py): this file corrupts datasets for CNN tasks (e.g. SST2, MR), given a specific typo probability
* [cnn_text_classification/main.py](https://github.com/emilioingenito/ReproducibilityChallenge/tree/main/extrinsic/cnn_text_classification/main.py) : this file performs the **CNN extrinsic task** evaluation 
* [rnn_ner/main.py](https://github.com/emilioingenito/ReproducibilityChallenge/tree/main/extrinsic/rnn_ner/main.py): this file performs the **NER extrinsic task** evaluation  

## How to train the model

In our experiments, we used the pretrained LOVE model provided by the authors of the paper. We also trained the model using an instance of a VM (through Google Cloud Platform). In order to train the model, make sure to download the file [wiki-news-300d-1M.vec.zip](https://fasttext.cc/docs/en/english-vectors.html), put it in the directory /data, and run the following command:

```train
python train.py -dataset data/wiki-news-300d-1M.vec
```
