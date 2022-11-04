# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:36:17 2020

@author: PRIYANKA
"""

"""
NEW ZIPFS PROGRAM USING FUNCTIONS
"""

import nltk
import matplotlib
import matplotlib.pyplot as plt

# openening the files
jungle_file=open("junglebook.txt","r",encoding="utf-8")
bible_file=open("kingjamesbible_tokenized.txt","r",encoding="utf-8")


def zipf(corpora_file):
    corpora_words=[]
    for line in corpora_file:
        corpora_words.extend(line.split())
        
    fdist=nltk.FreqDist(w.lower() for w in corpora_words)
    sorted_freq=sorted(fdist.values(), reverse=True)
    plt.plot(sorted_freq)
    plt.xlabel('Rank of words based on frequency')
    plt.ylabel('Frequency of words')
    plt.title('Zipf\'s law')
    plt.show()
    
zipf(jungle_file)
zipf(bible_file)
