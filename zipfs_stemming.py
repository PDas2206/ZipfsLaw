# -*- coding: utf-8 -*-
"""
ZIPF'S LAW_STEMMING

This program empirically verifies the Zipf's Law on 4 texts, after STEMMING 
is performed on each text.
"""

import nltk
import matplotlib
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
#from matplotlib.ticker import ScalarFormatter


# Opening all the files required
jungle_file = open("junglebook.txt", "r", encoding="utf-8")
bible_file = open("kingjamesbible_tokenized.txt", "r", encoding="utf-8")
bg_file = open("SETIMES.bg-tr.bg", "r", encoding="utf-8")
tr_file = open("SETIMES.bg-tr.tr", "r", encoding="utf-8")

"""
*************************************************************************
This section deals with proving the Zipf's law for the junglebook corpus
*************************************************************************

"""
jungle_words=[]
for line in jungle_file:
    tokens=nltk.word_tokenize(line)
    jungle_words.extend(tokens)

"""
Performing stemming on the tokenized text
"""
porter = PorterStemmer()
stemmed_words = [porter.stem(w) for w in jungle_words]

#processing to prove zipf's law 
fdist = nltk.FreqDist(stemmed_words)
sorted_freqs = sorted(fdist.values(), reverse=True)

#plotting the acquired data
plt.plot(sorted_freqs)
plt.xlabel('Rank of words based on frequency')
plt.ylabel('Frequency of words')
plt.title('Zipf\'s law for Jungle Book-Stemmed')
plt.show()

"""
This section extracts the values from sorted_freqs list and 
creates another list woth values from 1 to total number of frequency 
elements present in sorted_freqs for the new y and x axis data respectively.
This is done to eliminate the case of matplotlib.pyplot.loglog ignoring the data 
corresponding to the rank 1 stored at index 0 of the sorted_freqs list.

"""
x = [i for i in range(1,len(sorted_freqs)+1)]
y = [*sorted_freqs]
plt.loglog(x,y)
plt.xlabel('Rank of words based on frequency in logarithmic scale')
plt.ylabel('Frequency of words in logarithmic scale')
plt.title('Zipf\'s law for Jungle Book-Stemmed-Logarithmic scale')
plt.show()
jungle_file.close()
 

"""

*****************************************************************************   
This section deals with proving the Zipf's law for the kingsjamesbible corpus
***************************************************************************** 

"""    
bible_words=[]
for line in bible_file:
    bible_words.extend(line.split())
"""
Performing stemming on the tokenized text
"""
porter = PorterStemmer()
stemmed_words = [porter.stem(w) for w in bible_words]

#processing to prove zipf's law     
fdist = nltk.FreqDist(w.lower() for w in bible_words)
sorted_freqs = sorted(fdist.values(), reverse=True)
plt.plot(sorted_freqs)
plt.xlabel('Rank of words based on frequency')
plt.ylabel('Frequency of words')
plt.title('Zipf\'s law for King James\'s Bible-Stemmed')
plt.show()

"""
This section extracts the values from sorted_freqs list and 
creates another list woth values from 1 to total number of frequency 
elements present in sorted_freqs for the new y and x axis data respectively.
This is done to eliminate the case of matplotlib.pyplot.loglog ignoring the data 
corresponding to the rank 1 stored at index 0 of the sorted_freqs list.

"""
x = [i for i in range(1,len(sorted_freqs)+1)]
y = [*sorted_freqs]
plt.loglog(x,y)
plt.xlabel('Rank of words based on frequency in logarithmic scale')
plt.ylabel('Frequency of words in logarithmic scale')
plt.title('Zipf\'s law for King James\'s Bible-Stemmed-Logarithmic scale')
plt.show()
bible_file.close()


"""

*******************************************************************************
This section deals with proving the Zipf's law for the bulgarian SETIMES corpus
*******************************************************************************

"""
bg_words=[]
for line in bg_file:
    bg_words.extend(line.split())
 
"""
Performing stemming on the tokenized text
"""
porter = PorterStemmer()
stemmed_words = [porter.stem(w) for w in bg_words]

#processing to prove zipf's law 
fdist = nltk.FreqDist(w.lower() for w in bg_words)
sorted_freqs = sorted(fdist.values(), reverse=True)
plt.plot(sorted_freqs)
plt.xlabel('Rank of words based on frequency')
plt.ylabel('Frequency of words')
plt.title('Zipf\'s law for SETIMES Bulgarian-Stemmed')
plt.show()

"""
This section extracts the values from sorted_freqs list and 
creates another list woth values from 1 to total number of frequency 
elements present in sorted_freqs for the new y and x axis data respectively.
This is done to eliminate the case of matplotlib.pyplot.loglog ignoring the data 
corresponding to the rank 1 stored at index 0 of the sorted_freqs list.

"""
x = [i for i in range(1,len(sorted_freqs)+1)]
y = [*sorted_freqs]
plt.loglog(x,y)
plt.xlabel('Rank of words based on frequency in logarithmic scale')
plt.ylabel('Frequency of words in logarithmic scale')
plt.title('Zipf\'s law for SETIMES Bulgarian-Stemmed-Logarithmic scale')
plt.show()
bg_file.close()


"""

*******************************************************************************
This section deals with proving the Zipf's law for the Turkish SETIMES corpus
*******************************************************************************

"""
tr_words=[]
for line in tr_file:
    tr_words.extend(line.split())

"""
Performing stemming on the tokenized text
"""
porter = PorterStemmer()
stemmed_words = [porter.stem(w) for w in tr_words]

#processing to prove zipf's law     
fdist = nltk.FreqDist(w.lower() for w in tr_words)
sorted_freqs = sorted(fdist.values(), reverse=True)
plt.plot(sorted_freqs)
plt.xlabel('Rank of words based on frequency')
plt.ylabel('Frequency of words')
plt.title('Zipf\'s law for SETIMES Turkish-Stemmed')
plt.show()

"""
This section extracts the values from sorted_freqs list and 
creates another list woth values from 1 to total number of frequency 
elements present in sorted_freqs for the new y and x axis data respectively.
This is done to eliminate the case of matplotlib.pyplot.loglog ignoring the data 
corresponding to the rank 1 stored at index 0 of the sorted_freqs list.

"""
x = [i for i in range(1,len(sorted_freqs)+1)]
y = [*sorted_freqs]
plt.loglog(x,y)
plt.xlabel('Rank of words based on frequency in logarithmic scale')
plt.ylabel('Frequency of words in logarithmic scale')
plt.title('Zipf\'s law for SETIMES Turkish-Stemmed-Logarithmic scale')
plt.show()
tr_file.close()

