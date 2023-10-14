
# Reproducibility challenge: Natural Lenguage Processing
* The aim of this project is to reproduce the results of the paper [Imputing Out-of-Vocabulary Embeddings with LOVE Makes Language Models Robust with Little Cost](https://arxiv.org/abs/2203.07860) for the Natual Language Processing course.
* The paper tries to address the problem of extending the word representation of an existing pre-trained language model like FastText and makes it robust to Out Of Vocabulary (OOV) words.
* The authors uses a simple contrastive learning framework called LOVE that follows the principle of mimick-like models to generate vectors for unseen words. It is demonstrated that the model achieves similar and better performances than prior competitors, both on original datasets and on corrupted variants. In addition, the performance of the model used in a plug-and-play fashion with FastText and BERT (that we were unable to reproduce) shows the increase in robustness of the model.

----------

Our results support the main claim of the original paper. In all the three tasks we tried
to reproduce, i.e. intrinsic evaluation, extrinsic evaluation, and robust evaluation, even
though we did not always obtain the same results as the authors, we were able to make
the same overall conclusions.
Hence, for each claim of section 2, here we provide a corresponding section, where
we show the results of our analysis and compare them with the ones provided by the
authors.
Depending on the task, these are the metrics used to compare the performances:
* Intrinsic task: Spearman’s ρ similarity
* Extrinsic task: Accuracy and F1

The results that we obtained strongly support the original claims of the author. The
strength of our approach is the fact that we were able to reproduce the results both
on our personal machines (removing CUDA calls) and on the remote machines. 

---

Please refer to [link](/Report.pdf) for a detailed report.
