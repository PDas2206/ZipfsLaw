# -*- coding: utf-8 -*-
'''
ZIPF'S LAW

This program empirically verifies the Zipf's Law on 4 texts.
'''

import nltk
import matplotlib
import matplotlib.pyplot as plt

'''
openening the files
'''
jungle_file=open("junglebook.txt","r",encoding="utf-8")
bible_file=open("kingjamesbible_tokenized.txt","r",encoding="utf-8")
bg_file = open("SETIMES.bg-tr.bg", "r", encoding="utf-8")
tr_file = open("SETIMES.bg-tr.tr", "r", encoding="utf-8")


def zipf(corpora_file):
    '''
    *************************************************************************
    This function proves the Zipf's law for the called corpora
    *************************************************************************

    '''
    corpora_words=[]
    for line in corpora_file:
        corpora_words.extend(line.split()) #splitting text into tokens by whitespace
        
    fdist=nltk.FreqDist(w.lower() for w in corpora_words) #finding frequency of each word after converting all of them to lower case 
    sorted_freq=sorted(fdist.values(), reverse=True) #sorting the frequency data and plotting it
    plt.plot(sorted_freq)
    plt.xlabel('Rank of words based on frequency')
    plt.ylabel('Frequency of words')
    plt.title('Zipf\'s law')
    plt.show()
    
    """
    This section extracts the values from sorted_freqs list and 
    creates another list with values from 1 to total number of frequency 
    elements present in sorted_freqs for the new y and x axis data respectively.
    This is done to eliminate the case of matplotlib.pyplot.loglog ignoring the data 
    corresponding to the rank 1 stored at index 0 of the sorted_freqs list.
    """
    x = [i for i in range(1,len(sorted_freqs)+1)]
    y = [*sorted_freqs]

    plt.loglog(x,y)
    plt.xlabel('Rank of words based on frequency in logarithmic scale')
    plt.ylabel('Frequency of words in logarithmic scale')
    plt.title('Zipf\'s law for Jungle Book-Logarithmic scale')
    plt.show()
    jungle_file.close()

    
'''
Calling the zipf function over each set of texts
'''
zipf(jungle_file)
zipf(bible_file)
zipf(bg_file)
zipf(tr_file)
