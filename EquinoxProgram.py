# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:12:04 2015

@author: Shubham Suzanne
"""
#The program retrieves the webpage, removes the html content from it, collects 
#the entire vocabulary and stores it in a text file vocab.txt also it finds the
#20 most frequents words from the vocab and appends the result to another text 
#file frequent.txt
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
 #  url = "http://"+url
print( "Attempting to open ", url)
try:
   linecount=0
   page=request.urlopen(url)
except:
   print("\nCould not open URL: ", url)
   fail = True

nohtml = BeautifulSoup(page).get_text()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(nohtml)
print(tokens)

def writeVocab():
    print('\nCreating a new text file for writing the vocab of webpage to the text file vocab.txt')
    #Name of text file for writing vocab
    textFileName = 'vocab.txt'
    
    try:
        print('\nWriting to the text file..\n') 
        #Trying to create a new file or open one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(tokens))
        writeToTextFile.close()
        print('File writing completed!\n\n\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
    
writeVocab()

print(' \nList most frequent words :\n')
fdist = FreqDist(tokens)
mostFrequentWords = fdist.most_common(20)
print(mostFrequentWords)

def writeFrequentWords():
    print('\nCreating a new text file for writing result of 20 frequent words to frequent.txt')
    #Name of text file for writing vocab
    textFileName = 'frequent.txt'
    
    try:
        print('\nWriting to the text file..\n') 
        #Trying to create a new file or open one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(mostFrequentWords))
        writeToTextFile.close()
        print('File writing completed!\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
        
writeFrequentWords()        
    
    


    