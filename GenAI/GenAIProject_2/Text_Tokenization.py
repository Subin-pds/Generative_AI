import markdown
from bs4 import BeautifulSoup
import re
import nltk
from nltk import word_tokenize, sent_tokenize, pos_tag

def get_word_tokens(text):

   #Sentence tokenization
   sentences = sent_tokenize(text)
   #Word Tokenization + POS
   for sent in sentences:
       words = word_tokenize(sent)
       tagged = pos_tag(words)
       print(f"\n Sentence: {sent}")
       print("POS Tag:", tagged)




