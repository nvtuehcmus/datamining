import requests
import os
from os import path
import preprocessor as pre
#import TF_IDF as tf_idf
list_path=[]
def getFile(path):

    for element in os.listdir(path):
        if('.' not in element):
            getFile(path+'/'+element)#
        else:
            list_path.append(path+"/"+element)
    return list_path

# getFile('topic')
# print(list_path[0].split('/')[1])
def create_dir_tree(dir,topic):
    if(not path.exists(dir)):
        os.mkdir(dir)
    if(not path.exists(dir+'/'+topic)):
        os.mkdir(dir+'/'+topic)
    
def fetch(path):
    list_url_file = getFile(path) # get file which is have url
    list_path = []
    for urls_file in list_url_file:
        f = open(urls_file,'r',encoding='utf-8') # open file to get url and add to list urls
        urls = f.read().split('\n') # beacause f.read() return class string so i have to use split to change to list
        sub_path = urls_file.split('/') # get structure of dir examble 0: root 1:topic 2:file name 
        create_dir_tree('result',sub_path[1])
        
        for i in range(len(urls)):
            try: #

                resp = requests.get(urls[i])
                if resp.ok:
                    result_path = 'result/'+sub_path[1]+'/'+sub_path[2].split('.')[0]+'_'+str(i)+'.txt'
                    resf = open(result_path,'w',encoding='utf-8')
                    resf.write(resp.text)
            except:
                print('cant not fetch to ',urls[i])
                print("*"*100)

def preprocessor(): # reprocessor data from fetch
    for file in getFile('result'):
        pre.preprocessor(file)
    

def TF_IDF():
    if(not path.exists('TF-IDF')):# create dir
        os.mkdir('TF-IDF')



    path_ = 'TF-IDF/TF_IDF.txt'
    list_file = getFile('result')
    f = open(path_,'w',encoding='utf-8')
  
    for i in range(len(list_file)):
        fr = open(list_file[i],'r',encoding='utf-8')
        result = tf_idf.TF_IDF([fr.read()])#loop to solve file in list file
        f.write(list_file[i].split('/')[2]+'\n') #show file name
        for element in result:
            f.write(str(element)+'\n')

def main(path):
    fetch(path)
    preprocessor()
    #TF_IDF()
    




    








