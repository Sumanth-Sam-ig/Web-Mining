import whoosh as wh
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from spellchecker import SpellChecker
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import jaccard_similarity_score

q=input("Enter the query : ")

spell = SpellChecker()
"""from whoosh import qparser, highlight
qtext = 'mary "litle lamb"'
q = qparser.QueryParser("text", myindex.schema)
mysearcher = myindex.searcher()
correction = mysearcher().correct_query(q, qtext)
correction.string
mysearcher.close()
"""
b=list(q.split())

c=[]

for word in b:
        c=c+[spell.correction(word)]
q=" ".join(c)

print("corrected query is ")

print(q)

qset=[]

qset=qset+[q]

docs={}

for i in range(50):
    soc=open("files/data"+str(i)+".txt","rt")
    docs[i]=soc.read()
    qset=qset+[docs[i]]

vectorizer = TfidfVectorizer()

tf = vectorizer.fit_transform(qset)

def get_jaccard_sim(str1, str2):
        a = set(str1.split())
        b = set(str2.split())
        c = a.intersection(b)
        return float(len(c)) / (len(a) + len(b) - len(c))

s=[]
for i in range(50):
        s=s+[get_jaccard_sim(q,docs[i])]

cos={}

for i in range(50):
    cos[i]=s[i]
    
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

print("Top Similar Documents are")

for i in range(len(out)):
    print(" document-",out[i]+1 ," similarity == " ,cos[out[i]])


