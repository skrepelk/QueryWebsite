# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:12:04 2015

@author: Shubham Suzanne
"""

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
tokens = nltk.word_tokenize(nohtml)
print(tokens)

print(' \nList most frequent words :\n')
fdist = FreqDist(tokens)
most = fdist.most_common(20)
print(most)

def write():
    print('\nCreating a new text file\n')
    #Name of text file coerced with .txt
    textFileName = input('Enter name of text file: ') + '.txt'
    
    try:
        print('\nWriting to the text file..\n') 
        #Trying to create a new file or open one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(tokens))
        writeToTextFile.close()
        print('File writing completed!\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
    
write()


    