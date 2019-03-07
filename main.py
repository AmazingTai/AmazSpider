# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import jieba
import re
import Databases
import PageRank

ignorewords=set(['的','但是','然而','能','在','以及','可以','使'])
class crawler:
    def __init__(self,dbname):
        pass
    def __del__(self):
        pass  
    def validword(self,word):
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = zhPattern.search(word)
        if match:
            return 1
        else:
            return 0

    def addtoindex(self,url,soup):
        #if self.isindexed(url): return
        print('Indexing '+url)
        
        text=self.gettextonly(soup)      #获取文本信息
        words=self.separatewords(text)   #分词
        dicn=list(words)
        
        title = []
        for i in range(len(dicn)):
            word=dicn[i]
            if word in ignorewords: continue
            if self.validword(word):
                title.append(word)
        Databases.save(title, url)    #关键词和URL存库

    #从一个Html网页中提取文字（不带标签的）
    def gettextonly(self,soup):
        v=soup.string
        if v==None:
            c=soup.contents
            resulttext=''
            for t in c:             #获取文本信息
                resulttext+=self.gettextonly(t)+'\n'
            return resulttext
        else:
            return v.strip()
       
    def separatewords(self,text):   #结巴分词
        seg_list=jieba.cut_for_search(text);
        return seg_list
        
    '''def separatewords(self,text):
        ##该方法仅仅局限于分英文单词
        splitter=re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s!=' ']
    '''

    #从一组小网页开始进行广度优先搜索，直到某一给定深度，期间为网页建立索引
    def crawl(self,pages,depth=2):
        for i in range(depth):
            newpages=set()
            for page in pages: #广度
                try:
                    c=urllib.request.urlopen(page)
                except:
                    print ("Could not open %s" % page) 
                    continue
                soup=BeautifulSoup(c.read())
                self.addtoindex(page,soup) #索引
                
                links=soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'")!=-1:continue
                        url=url.split('#')[0] #去锚点
                        if url[0:4]=='http':   
                            newpages.add(url)
            pages=newpages
            
            
pagelist=['http://www.sdust.edu.cn/']

if Databases.empty() == 1:
    cra=crawler('')
    cra.crawl(pagelist)

search = input("Please input your keyword: ")

#seach进行结巴分词
seg_list = jieba.cut_for_search(search)
url_num = 0
link = []
for sword in seg_list:
    urls = Databases.read(sword)
    urls = list(set(urls))
    if urls:
        for each in urls:
            link.append(each)
            #print(each)
            url_num += 1
            
link = list(set(link))
for each in link:
    print(each)

print("number of url : ", len(link))
print("Sorting...")
if link:
    result = PageRank.Rank(link)
    length = len(result)
    for i in range(length):
        print(result[i][0])    
