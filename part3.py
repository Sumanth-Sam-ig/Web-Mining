from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix
import seaborn as sns; sns.set()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_fscore_support


qset=[]

docs={}

for i in range(50):
    soc=open("files/data"+str(i)+".txt","rt")
    docs[i]=soc.read()
    qset=qset+[docs[i]]

train=qset[0:40]
test=qset[40:50]

target=[]
init_labels=[]

for i in range(40):
    target=target+[str(i//20)]
for i in range(10):    
    init_labels=init_labels+[str(i%2)]
    

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train,target)
labels = model.predict(test)


vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(qset)

tree = DecisionTreeClassifier(criterion = "entropy",max_depth=10, min_samples_leaf=5,random_state=100)

tree.fit(X[0:40], target)

tree_labels=tree.predict(X[40:50])

print(" Actual labels = ")
print(init_labels)

print(" \nBayes clasifier properties")

print("Predicted labels = ")
print(labels)

print( "accuray=", accuracy_score(init_labels, labels))

a=precision_recall_fscore_support(init_labels, labels,average=None,labels=['0', '1'])

print("precision = ",a[0])
print("recall = ",a[1])
print("f_score = ",a[2])
print("support = ",a[3])

print("\nDecision tree properties")

print("Predicted labels = ")
print(tree_labels)

print("accuray=",accuracy_score(init_labels, tree_labels))

a=precision_recall_fscore_support(init_labels, tree_labels,average=None,labels=['0', '1'])


print("precision = ",a[0])
print("recall = ",a[1])
print("f_score = ",a[2])
print("support = ",a[3])










