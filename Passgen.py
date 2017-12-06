#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import random

r = random.SystemRandom()
nb_words=6

words_path = '/usr/share/dict/words' 			#dictionnary source
separator_list='#/!.?+-* '						 #separator of the different words
separator= r.choice(separator_list)

with open(words_path) as words:
	words=words.read().split()

passp=''
for i in range(0,nb_words):
	word_pos = r.randrange(len(words))
	passp += words[word_pos] + separator

print(passp)
print(len(words))

#
#s = "some string"
#print(r.choice(s)) # print random character from the string
#print(s[r.randrange(len(s))]) # same

