# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:12:04 2015

@author: Shubham Suzanne
"""
#The program retrieves the webpage, removes  HTML content , collects the complete vocabulary, and stores it in a text file,
#vocab.txt.
#It also collects the 20 most common words and appends the result to a second text file, frequent.txt
import nltk
import urllib
import sys
from nltk import *
from nltk.tokenize import RegexpTokenizer
from urllib import request
from bs4 import BeautifulSoup

fail = False
url = "http://www.timeanddate.com/calendar/autumnal-equinox.html"
#if "http://" not in url[0:7]:
 #then url = "http://"+url
print( "Attempting to open ", url)
try:
   linecount=0
   page=request.urlopen(url)
except:
   print("\nCould not open URL: ", url)
   fail = True

#the program is tokenized to remove HTML
nohtml = BeautifulSoup(page).get_text()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(nohtml)
print(tokens)

#printing the list of words in "vocab.txt"
def writeVocab():
    print('\nCreating a new text file for writing the vocab of webpage to the text file vocab.txt')
    textFileName = 'vocab.txt'
    
    try:
        print('\nWriting to the text file..\n') 
        #Trying to create a new file or open an extisting one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(tokens))
        writeToTextFile.close()
        print('File writing completed!\n\n\n')
        #if it cannot access the file:
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
    
writeVocab()

#retrieving the 20 most frequently found words
print(' \nList most frequent words :\n')
fdist = FreqDist(tokens)
mostFrequentWords = fdist.most_common(20)
print(mostFrequentWords)

def writeFrequentWords():
    print('\nCreating a new text file for writing result of 20 frequent words to frequent.txt')
    #New text file
    textFileName = 'frequent.txt'
    
    try:
        print('\nWriting to the text file..\n') 
        #Trying to create a new file or open an existing one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(mostFrequentWords))
        writeToTextFile.close()
        print('File writing completed!\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
        
writeFrequentWords()        
    
    
