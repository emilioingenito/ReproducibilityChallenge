'''
Scripts we used to corrupt the datasets of CNN tasks,
exploiting the function -get_random_attacks- with a specific combination of typo probabilities
'''

import codecs
import attacks
with codecs.open("extrinsic/cnn_text_classification/evaluation/dev.tsv", 'r', encoding='utf-8', errors='ignore') as in_file:
    out = open("extrinsic/cnn_text_classification/evaluation/dev_corr.tsv", 'w')
    for line in in_file:
        words = line.split()
        corr_words = []
        for word in words:
            corr_word = attacks.get_random_attack(word, [0.18, 0.18, 0.18, 0.18, 0.18, 0.1])
            corr_words.append(corr_word)
        corr_words = ' '.join(corr_words[:-1])+'\t'+words[-1]+'\n'
        out.write(corr_words)
