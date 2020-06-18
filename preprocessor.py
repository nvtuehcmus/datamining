import os
import re
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

def getFile(path):
    list_path=[]
    for root,dir,files in os.walk(path):
        for file in files:
            list_path.append(root+"/"+file)
    return list_path

#open file
def readFile(path):
    read_file=open(path,'r',encoding='utf-8')
    read_file.closed
    return read_file.read()


def clear_html(text):
    soup=BeautifulSoup(text,'html.parser')
    return soup.get_text()

def remove_special_character(text):
    string = re.sub('[^\w\s]','',text) #using regular expression to change special character to ''
    string = re.sub('\s+',' ',string)
    string= string.strip()
    return string

def Clean_stopWord(listWord):
    stopWords= set(stopwords.words('english'))
    listWordNew= [word for word in listWord if word not in stopWords]
    return listWordNew

def Stemmer(listWord):
    ps = PorterStemmer()
    listWordNew=[ps.stem(word) for  word in listWord]
    return listWordNew

def run(list_path):
    i=1
    textList = []
    for path in list_path:
        text = clear_html(readFile(path))
        #remove special character
        string= remove_special_character(text)
        # change text to list text
        listWord = string.split(' ')
        #lower all word in list
        listWord= [word.lower() for word in listWord]
        #clean stop word and stermmer text
        newWords = Stemmer(Clean_stopWord(listWord))
        #join list to text
        newText = ' '.join(newWords)
        textList.append(newText)
    return textList

def preprocessor(path):
    text = clear_html(readFile(path))
    #remove special character
    string= remove_special_character(text)
    # change text to list text
    listWord = string.split(' ')
    #lower all word in list
    listWord= [word.lower() for word in listWord]
    #clean stop word and stermmer text
    newWords = Stemmer(Clean_stopWord(listWord))
    #join list to text
    newText = ' '.join(newWords)
    f=open(path,'w',encoding='utf-8')
    f.write(newText)
    f.close()
    