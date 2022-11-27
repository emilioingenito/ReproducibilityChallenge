'''
Useful scripts which we used to format the  MR dataset
'''

import codecs
with codecs.open("rt-polarity_original_positive.txt", 'r', encoding='utf-8', errors='ignore') as lines:
	out = open('positive.txt', 'w')
	count = 0
	for line in lines:
                if(len(line)>3 && line[0] not in String.punctuation)
                        word = line[0]
                        word = f(word)
                        new_line = word+line[1:]
                        out.write(new_line)
                else:
                        out.write(line)
	lines.close()
	out.close()

