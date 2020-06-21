import crawl as crawler
import crawl_from_files as crawler_files
import os
from os import path
import preprocessor as pre
import measure as mea


print('* '*10+'MENU'+'* '*10)
print('* 1.crawler from default directory        *')
print('* 2.crawler from your website             *')
print('* '*10+'* * '+'* '*10)




choose = int(input('what do you want to do ? '))
dir = ''
if(choose == 1):
    crawler_files.run('topic')
elif(choose == 2):
    result_list = []
    url = input('input your url: ')
    if('http://' not in url and 'https://' not in url ):
        dir =  url
        url = 'http://' + url
    else:
        dir = url.split('/')[2] #get domain name to create dir
    if(not path.exists(dir)):
        os.mkdir(dir)
    _path = dir+'/data.txt'
    f = open(_path,'w',encoding='utf-8')
    # create dir TF_IDF
    if(not path.exists('TF_IDF')):
        os.mkdir('TF_IDF')
    # create dir bag of word
    if(not path.exists('BOW')):
        os.mkdir('BOW')
    tf_file = open('TF_IDF/data.txt','w+')
    bow_file = open('BOW/data.txt','w+')

    f.write(crawler.crawl(url))

    result_list.append(pre.preprocessor(_path))
    print('done!')
    continous = int(input("do you want to get some topic from your website? "))
    
    if(continous):
        ls_url = crawler.getUrl(url)
        [print(str(i+1)+":"+ls_url[i]) for i in range(len(ls_url))]
        check = 1
        while check:
            option = int(input("choose your option? "))
            url_option = ''
            temp=ls_url[option-1].split('/')[2:]
            for string in temp:
                url_option+=string
            if('.html' in url_option):
                url_option = url_option[:-4]
            if(not path.exists(dir+'/'+url_option)):
                os.mkdir(dir+'/'+url_option)
            _path = dir+'/'+url_option+'/data.txt'
            f = open(_path,'w',encoding='utf-8')
            f.write(crawler.crawl(ls_url[option-1]))
            result_list.append(pre.preprocessor(_path))
            check=int(input('do you want to contious!'))

    tf_idf = mea.TF_IDF(result_list)
    [tf_file.write(i) for i in tf_idf] # run solve tf_idf
    bow = mea.BoW(result_list)
    bow_file.write(str(bow)) # run solve bow
    mea.cosin(bow) # run solve cosin

else:
  print('somthing went wrong !!!')