import wikipedia
import nltk
import re
from nltk.corpus import stopwords
import string

def all_text(inp):
    current_page = wikipedia.page(wikipedia.search(inp, results = 1))
    text = current_page.content
    headings = re.finditer("[^=]==[^=](.*)[^=]==[^=]", text)
    sub_headings = re.finditer("[^=]===[^=](.*)[^=]===[^=]",text)
    
    heading_points = []  
    for x in iter(headings):
        heading_points += [(x.span())]
    print (heading_points)

    sub_heading_points = []  
    for x in iter(sub_headings):
        sub_heading_points += [(x.span())]
    print (sub_heading_points)

    
    
            

def most_freq(inp):
    current_page = wikipedia.page(wikipedia.search(inp, results = 1))
    list_words= ((current_page.content.translate(string.punctuation)).lower()).split()
    reavent_words = [w for w in list_words if not w in stopwords.words('english')]
    fdisk = nltk.FreqDist(reavent_words)
    return fdisk.most_common(50)



all_text("glasgow")
