from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import Birch

qset=[]

docs={}

for i in range(50):
    soc=open("files/data"+str(i)+".txt","rt")
    docs[i]=soc.read()
    qset=qset+[docs[i]]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(qset)

model = Birch(branching_factor=50, n_clusters=5, threshold=0.5)
clusters =model.fit(X)

print(" Cluster info ")

a=list(clusters.labels_)

for i in range(5):
    print(" Documents in  Cluster ", i,"= ",a.count(i),"\n")
    for j in range(50):
        if(a[j]==i):
            print("doc",j," ",end=" ")
    print("\n")




