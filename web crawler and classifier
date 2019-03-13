import nltk,webbrowser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from html.parser import HTMLParser  
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]
        
    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html; charset=UTF-8':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return self.links
        else:
            return "",[]
    def getData(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html; charset=UTF-8':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString
        else:
            return "",[]

 
a={}

for i in range(10):
    a[i]="files/file"+str(i)+".txt"
  
sources = []

def getlinks(url):
    parser = LinkParser()
    links=parser.getLinks(url)
    return links[1:11]

stop_words = set(stopwords.words('english'))
stopWords = stopwords.words('english')

ps=PorterStemmer()

def getdata(url,no):
    text1=[]
    parser=LinkParser()
    data=parser.getData(url)
    t=open("files/data"+str(no)+".txt","w")
    soup = BeautifulSoup(data)
    text=soup.get_text().encode("utf-8")

    text=str(text)
    content=text.split()

    info=""
    
    for w in content:
        if(w.isalpha()):
            #if (len(w)<13 & len(w)>2):
            if(w not in stop_words):
                    text1=text1+[w]

    text1=list(set(text1))
    
    for w in text1:
        info=info+w+" "

    t.write(info)
    t.close()
    return "files/data"+str(no)+".txt"


sources=sources+getlinks("https://en.wikipedia.org/wiki/Pacific_Ocean")
sources=sources+getlinks("https://en.wikipedia.org/wiki/Olympic_Games")
sources=sources+getlinks("https://en.wikipedia.org/wiki/Astronomy")
sources=sources+getlinks("https://en.wikipedia.org/wiki/Intel")
sources=sources+getlinks("https://en.wikipedia.org/wiki/Bon_Jovi")

files={}
conn={}


for i in range(50):
    conn[i]=sources[i]
    print(sources[i])
    #files[sources[i]]=getdata(sources[i],i)


query=input("Enter the query : ")

q=''
for w in query.split():
	q=q+ps.stem(w)+" "

qset=[]

qset=qset+[q]

docs={}

for i in range(50):
    soc=open("files/data"+str(i)+".txt","rt")
    docs[i]=soc.read()
    qset=qset+[docs[i]]

tfidf_vectorizer = TfidfVectorizer(stop_words=stopWords)

tfidf_matrix_train = tfidf_vectorizer.fit_transform(qset)

similarity=cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train[1:])

print(similarity)

cos={}

for i in range(50):
    cos[i]=similarity[0][i]
    
res=list(cos.values())
res.sort(reverse=True)


out=[]

for i in range(10):
    if(res[i]>0):
     for j in range(50):
        if(cos[j]==res[i]):
            if(j not in set(out)):
                 out=out+[j]
                 break
    
for i in range(len(out)):
    print(conn[out[i]] ," similarity == " ,cos[out[i]])

for i in range(len(out)//3):
    webbrowser.open_new(conn[out[i]])






    

    

