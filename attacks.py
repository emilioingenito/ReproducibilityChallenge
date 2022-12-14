import random
import numpy as np
import nlpaug.augmenter.char as nac

# function useful to load synonyms from a specific
# file which should be included as a parameter
def load_synnoym(path='data/synonym.txt'):
    all_syn = dict()
    for line in open(path, encoding='utf8'):
        line = '\t'.join(line.split())
        row = line.strip().split('\t')
        all_syn[row[0]] = row[1].split('__')
    return all_syn

all_syn = load_synnoym()

# insert a keyboard mistake in the given word:
# e.g the word 'play' can become 'plat' or 'plau'
def keyboard(word, max_char=1):
    aug = nac.KeyboardAug(include_upper_case=False, aug_char_max=max_char)
    auged_word = aug.augment(word)
    return auged_word

# insert an extra character in a given word
# e.g. from 'play' to 'plaby'
def insert_aug(word, max_char=1):
    aug = nac.RandomCharAug(action="insert", aug_char_max=max_char)
    auged_word = aug.augment(word)
    #print(word, auged_word)
    return auged_word

# swap two characters of a given word
def swap_aug(word, max_char=1):
    aug = nac.RandomCharAug(action="swap", aug_char_max=max_char)
    auged_word = aug.augment(word)
    #print(word, auged_word)
    return auged_word

# deletes a character from a give word
def delete_aug(word, max_char=1):
    aug = nac.RandomCharAug(action="delete", aug_char_max=max_char)
    auged_word = aug.augment(word)
    #print(word, auged_word)
    return auged_word

# swaps a word with a possible synonym
def synonym_aug(word):
    if word not in all_syn:return None
    syns = list(all_syn[word])
    if len(syns) == 0:
        return None
    aug_word = random.choice(list(all_syn[word]))
    return aug_word


def ocr_aug(word, max_char=1):
    aug = nac.OcrAug(aug_char_max=max_char)
    return aug.augment(word)

# given typos probabilities and a specific word, it corrupts the word
def get_random_attack(word, probs=[0.07, 0.07, 0.07, 0.07, 0.36, 0.36]):
    attack_type = ['swap', 'delete', 'insert', 'keyboard', 'synonym', 'unchange']
    attack_probs = np.array(probs)
    attack_probs = attack_probs / sum(attack_probs)
    attack = np.random.choice(attack_type, 1, p=attack_probs)[0]
    #print(attack)
    for _ in range(5):
        if attack == 'swap':
            return swap_aug(word)
        if attack == 'delete':
            return delete_aug(word)
        if attack == 'insert':
            return insert_aug(word)
        if attack == 'keyboard':
            return keyboard(word)
        if attack == 'synonym':
            aug_syn = synonym_aug(word)
            if aug_syn:return aug_syn
        if attack == 'unchange':
            return word
    return word


if __name__ == '__main__':
    pass