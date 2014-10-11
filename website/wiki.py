import wikipedia
import nltk
import re
from nltk.corpus import stopwords
import string

def all_text(inp):
    current_page = wikipedia.page(wikipedia.search(inp, results = 1))# search finds what it thinks is most relivent not the exact right match
    test = (current_page.content).split("\n")
    print(len(test))
    remo = []
    for x in test:
        if x =="":
            test.remove(x)
    print (len(test))
    for x in test:
        print (x)
        print("__________________________________________________________")
        

def most_freq(inp):
    current_page = wikipedia.page(wikipedia.search(inp, results = 1))
    list_words= ((current_page.content.translate(string.punctuation)).lower()).split()
    reavent_words = [w for w in list_words if not w in stopwords.words('english')]
    fdisk = nltk.FreqDist(reavent_words)
    return fdisk.most_common(50)



all_text("glasgow")
