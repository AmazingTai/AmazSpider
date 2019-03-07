# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urljoin

def is_link(mainurl, securl):
    newurl = set()
    try:
        c=urllib.request.urlopen(mainurl)
        soup=BeautifulSoup(c.read(), 'html.parser')
        links=soup('a')
        for link in links:
            if('href' in dict(link.attrs)):
                url=urljoin(mainurl,link['href'])
                if url.find("'")!=-1:continue
                url=url.split('#')[0] #去锚点
                if url[0:4]=='http': 
                    newurl.add(url)
        if securl in newurl:
            return 1
        else:
            return 0
    except:
    	return 0

def linkDic(urls):
    urldict = dict()
    for i in urls:
        turls = []
        for j in urls:
            if i != j:
            	if is_link(i, j):
                    turls.append(j)
        if turls:
            urldict[i] = turls
        else:
        	urldict[i] = []
    #print(len(urldict))
    #print(urldict)
    return urldict


if __name__ == '__main__':
	urls = ["http://www.sdust.edu.cn/", "http://xy.sdust.edu.cn/",
	"http://xy.sdust.edu.cn/index.php"]
	print(linkDic(urls))
    