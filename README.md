# zipf's law
To empirically prove the Zipf’s law, the provided corpora (Jungle book, King James Bible, SETIMES in Bulgarian and in Turkish) and some methods from the NLTK library have been used. Firstly for each corpora the text has been tokenized and stored into lists, from wherein the frequency distribution of each token is being calculated. This frequency distribution is used to plot the graphs (using matplotlib). The hyperbolic nature of the plots prove that the rank of a word is inversely proportional to the frequency of that word in the frequency distribution chart of a text, in other words it empirically proves the Zipf’s law as valid.

Additionally the program also provides logarithmic scale plots to depict the same phenomena to provide a clearer view of the actual frequency distribution with respect to the rank of a token for the different corpora. A problem while plotting the data using logarithmic scale is that log(0) is undefined and hence its value is automatically ignored by matplotlib. But 0 in our case is rank 1 (the index 0 of the frequency list is rank 1), and hence of mighty importance. So as not to lose the data corresponding to this value two new list has been defined. The first list has the new x-axis data values i.e. rank of the words according to frequency starting from 1. The y-axis data is just the values from the list containing the sorted word frequencies. To verify whether the law remains valid after performing stemming over the date, a separate program has been provided (zipfs_stemming.py) that determines the same. 
## Getting Started:
The programs in this repo have been coded using Python 3. To run the files one has to have Python 3 or above installed in their systems. Additionally you need the following packages to be installed: \
nltk \
matplotlib 
## Running the programs:
To execute the programs from the command shell, do the following steps: \
		1. Change the directory to this folder in your system. \
		2. To now execute the programs, type the following after the prompt appears: \
			python <filename>.py \
		(where <filename> is any of the below stated ones) \
For zipfs_stemming.py to perform stemming, we have used the PorterStemmer method in nltk. This has been imported using the following command: \
				from nltk.stem.porter import PorterStemmer
		
