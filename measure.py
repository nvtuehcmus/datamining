from sklearn import *
import preprocessor as pre
import os
import re
from os import path
from scipy import spatial
def BoW(textList):
    results = feature_extraction.text.CountVectorizer()
    
    result = results.fit_transform(textList).todense()
    return result

def TF_IDF(textList):

    results = feature_extraction.text.TfidfVectorizer(analyzer='word',ngram_range=(1,3),min_df=0,stop_words='english')

    tf_id_matrix = results.fit_transform(textList)
    feature_name = results.get_feature_names()
    return str(tf_id_matrix).split('\n')


def cosin(bow):
    if(not path.exists('cosin')):
        os.mkdir('cosin')
    fcosine = open('cosin/data.txt','w')
    for i in range(len(bow)-1):
        for j in range(1,len(bow)):
            fcosine.write("D{0} AND D{1}: ".format(str(i),str(j)))
            fcosine.write(str(1-spatial.distance.cosine(bow[i],bow[j]))+'\n')
