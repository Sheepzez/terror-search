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

    out ={}
    c = 0
    for x in range(len(heading_points)-1):
        temp = {}
        if sub_heading_points != []:
            while sub_heading_points[c][0]< heading_points[x][1]:
                temp[text[sub_heading_points[c][0]+3:sub_heading_points[c][1]-3]]=text[sub_heading_points[c][1]+3:sub_heading_points[c+1][0]-3]
                c+=1
        else:
            temp[text[(heading_points[x][0]+3):(heading_points[x][1]-3)]]= text[(heading_points[x][1]):(heading_points[x+1][0])]
            
        out[text[(heading_points[x][0]+3):(heading_points[x][1]-3)]] = temp
    print(out)    
    #{heading:{sub_heading:data , sub_heading:data }, heading:{sub_heading:data , sub_heading:data} }
            

def most_freq(inp):
    current_page = wikipedia.page(wikipedia.search(inp, results = 1))
    list_words= ((current_page.content.translate(string.punctuation)).lower()).split()
    reavent_words = [w for w in list_words if not w in stopwords.words('english')]
    fdisk = nltk.FreqDist(reavent_words)
    return fdisk.most_common(50)



all_text("hackathon")
