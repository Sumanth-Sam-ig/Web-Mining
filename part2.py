from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

qset=[]

docs={}

for i in range(50):
    soc=open("files/data"+str(i)+".txt","rt")
    docs[i]=soc.read()
    qset=qset+[docs[i]]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(qset)

true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
kmeans=model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])

a=list(kmeans.labels_)

for i in range(5):
    print(" Documents in  Cluster ", i,"= ",a.count(i))




