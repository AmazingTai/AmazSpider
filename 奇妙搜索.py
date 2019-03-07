# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import jieba

class Node(object): #节点结构体
    def __init__(self, val,wh,p=0):
        self.data = val #val为string类型
        self.webhead = wh
        self.next = p

class LinkList(object):#链表
    def __init__(self):#初始化
        self.head = 0

    def __getitem__(self, key):#得到某一节点的内容，key相当于节点下标

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key < 0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):#修改某节点内容

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data,webhead):#初始化链表

        self.head = Node(data,webhead)

    def getlength(self):#返回链表长度

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):#判断链表是否为空

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):#清空链表

        self.head = 0


    def append(self,data,wh):#队尾插入

        q = Node(data,wh)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getdata(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')
            
    def getwh(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.webhead

        else:

            print ('target is not exist!')
            
    def insert(self,index,data,wh):#在任意位置插入

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Node(data,wh,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(data,wh,p)
            post.next = q
            q.next = p


    def delete(self,index):#删除任意节点

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
            
        if index == 0:
            self.head = self.head.next
            
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index == j:
            post.next = p.next

    def index(self,value):#查找链表中内容等于value的内容

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1



class Web(object): #节点结构体
    def __init__(self, val, p=0):
        self.data = val #val为string类型
        self.next = p

class WebList(object):#链表
    def __init__(self):#初始化
        self.head = 0

    def __getitem__(self, key):#得到某一节点的内容，key相当于节点下标

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):#修改某节点内容

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):#初始化链表

        self.head = Web(data)

    def getlength(self):#返回链表长度

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):#判断链表是否为空

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):#清空链表

        self.head = 0


    def append(self,data):#队尾插入

        q = Web(data)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getdata(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')
            
    def insert(self,index,data):#在任意位置插入

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Web(data, self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Web(data, p)
            post.next = q
            q.next = p


    def delete(self,index):#删除任意节点

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
            
        if index == 0:
            self.head = self.head.next
            
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index == j:
            post.next = p.next

    def index(self,value):#查找链表中内容等于value的内容

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1

class Result(object): #节点结构体
    def __init__(self, val, p=0):
        self.data = val #val为string类型
        self.next = p

class ResultList(object):#链表
    def __init__(self):#初始化
        self.head = 0

    def __getitem__(self, key):#得到某一节点的内容，key相当于节点下标

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):#修改某节点内容

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):#初始化链表

        self.head = Result(data)

    def getlength(self):#返回链表长度

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):#判断链表是否为空

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):#清空链表

        self.head = 0


    def append(self,data):#队尾插入

        q = Result(data)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getdata(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')
            
    def insert(self,index,data):#在任意位置插入

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Result(data, self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Result(data, p)
            post.next = q
            q.next = p


    def delete(self,index):#删除任意节点

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
            
        if index == 0:
            self.head = self.head.next
            
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index == j:
            post.next = p.next

    def index(self,value):#查找链表中内容等于value的内容

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


ignorewords=set(['的','但是','然而','能','在','以及','可以','使'])
#ignorewords=set(['the','of','to','and','a','in','is','it'])
ll = LinkList()
 
class crawler:
    def __init__(self,dbname):
        pass
    def __del__(self):
        pass                     
    def addtoindex(self,url,soup):
        #if self.isindexed(url): return
        print('Indexing '+url)
        
        text=self.gettextonly(soup)      #获取文本信息
        words=self.separatewords(text)   #分词
        dicn=list(words)
        
        for i in range(len(dicn)):
            word=dicn[i]
            if word in ignorewords: continue
            if ll.getlength() == 0:
              wl = WebList()
              wl.initlist(url)
              ll.initlist(word,wl)

            if ll.getlength() > 0:
              i = ll.index(word)
              if i == -1:
                wl = WebList()
                wl.initlist(url)
                ll.append(word,wl)
                #print(word)
              if i != -1:
                j = ll.getwh(i).index(url)
                if j == -1:
                    ll.getwh(i).append(url)

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
cra=crawler('')
cra.crawl(pagelist)
search = input("Please putin your keyword: ")
      
rl = ResultList()
rl.initlist('CONGCONG')
#seach进行结巴分词
seg_list = jieba.cut_for_search(search) 
for sword in seg_list:
    k = ll.index(sword)
    if k != -1:
        p = ll.getwh(k).getlength()
        for m in range(0,p):
            b = ll.getwh(k).getdata(m)
            if rl.index(b) == -1:        
                rl.append(b)
                print(b)
# python3 /Users/amazingtai/Desktop/Python/pachong/奇妙搜索.py