'''
Scripts we used to corrupt the datasets of NER tasks,
exploiting the function -get_random_attacks- with a specific combination of typo probabilities
'''

import codecs
import attacks
with codecs.open("extrinsic/rnn_ner/evaluation/devel.tsv", 'r', encoding='utf-8', errors='ignore') as in_file:
    out = open("extrinsic/rnn_ner/evaluation/devel_corr.tsv", 'w')
    for line in in_file:
        words = line.split()
        corr_words = []
        for i in range(len(words)):
            if i==0:
                corr_word = attacks.get_random_attack(words[i], [0.18, 0.18, 0.18, 0.18, 0.18, 0.1])
            else:
                corr_word = words[i]
            corr_words.append(corr_word)
        corr_words = ' '.join(corr_words)+'\n'
        out.write(corr_words)
