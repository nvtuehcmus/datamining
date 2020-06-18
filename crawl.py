import requests
import re



def getUrl(domain):
    r = requests.get(domain)
    text = r.text
    links = re.findall("href=.*title.*</a>",text) #regex get tag a in html file
    urls = []
    for link in links:
        temp = link[6:-1].split(' ')[0][:-1] #split link get link from a
        if ("https" not in temp): #add domain name to link: examble /hihi/haha -> https://huhu/hihi/haha  https://huhu is domain name
            temp = domain + temp
        urls.append(temp)
    return urls

def crawl(domain):
    r = requests.get(domain)
    return r.text

