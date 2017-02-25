import urllib2
import nltk
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Mani_Ratnam'
html = urllib2.urlopen(url).read()		// Reading data from webpage

soup = BeautifulSoup(html,"lxml")		// Exclude html tags
raw=soup.getText()

from nltk.tokenize import word_tokenize	// Extract words
tokens=nltk.word_tokenize(raw)

from nltk.corpus import stopwords		// Exclude end words
vocabulary=set(words)
vocabulary=[x for x in vocabulary if x not in stopwords.words('english')]
vocab_sorted=sorted(vocabulary, key=lambda s: s.lower())

from nltk.tokenize import RegexpTokenizer  // exclude ',",
tokenizer = RegexpTokenizer(r'\w+')
words=tokenizer.tokenize(raw)
print words

import re									//extract url
myString = "This is my tweet check it out http://tinyurl.com/blah, http://abcdl.com/blah"
re.findall(r'(https?://\S+)', myString)