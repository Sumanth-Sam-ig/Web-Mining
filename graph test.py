import networkx as net
import matplotlib.pyplot as plt

class node:
    def __init__(self,g,a):
        g.add_node(a)
        k.add_node(a)
        self.n=a
        self.pre=0
        self.i={}
        self.o={}
        self.d={}
        self.d[self.n]=0
        
def add_link(g,a,b):
        g.add_edge(b.n,a.n)
 
def add_in_link(g,a,b):
        k.add_edge(a.n,b.n)
        g.add_edge(b.n,a.n)
        a.pre=a.pre+1
        b.d[a.n]=1
        a.i[len(a.i)+1]=b.n
        b.o[len(b.o)+1]=a.n
        for i in range(len(a.i)):
                b.d[list(a.i.values())[i]]=2
            

def add_out_link(g,a,b):
        g.add_edge(a.n,b.n)
        a.o[len(a.o)+1]=b.n
        b.i[len(b.i)+1]=a.n
        b.pre=b.pre+1
        a.d[b.n]=1
        k.add_edge(a.n,b.n)

def show_graph(g):
    """pos=net.spring_layout(g)
    labels={}
    labels[a]=r'$a$'
    labels[b]=r'$b$'
    labels[c]=r'$c$'
    labels[d]=r'$d$'
    net.draw_networkx_labels(g,pos,labels,font_size=16)"""
    net.draw(g,with_labels= True,font_size=16)
    plt.show()

g=net.DiGraph()

nodes={}

k=net.Graph()

a=nodes[0]=node(g,'a')
b=nodes[1]=node(g,'b')
c=nodes[2]=node(g,'c')
d=nodes[3]=node(g,'d')
e=nodes[4]=node(g,'e')
f=nodes[5]=node(g,'f')
g1=nodes[6]=node(g,'g')
h=nodes[7]=node(g,'h')


add_in_link(g,a,b)
add_in_link(g,a,c)
add_in_link(g,a,d)
add_in_link(g,a,f)
add_in_link(g,b,c)
add_in_link(g,b,h)
add_in_link(g,b,a)
add_in_link(g,c,b)
add_in_link(g,c,e)
add_in_link(g,c,h)
add_in_link(g,d,f)
add_in_link(g,d,g1)
add_in_link(g,e,a)
add_in_link(g,e,d)
add_in_link(g,e,h)
add_in_link(g,f,b)
add_in_link(g,f,d)
add_in_link(g,g1,c)
add_in_link(g,g1,a)
add_in_link(g,h,e)
add_in_link(g,h,f)
add_in_link(g,h,b)

def degree_centrality(g):
    a=net.degree_centrality(g)
    nodes=list(a.keys())
    degree=list(a.values())
    for i in nodes:
        print(i,"  ",a[i])
    
def closeness_centrality(g):
    a=net.closeness_centrality(g)
    nodes=list(a.keys())
    degree=list(a.values())
    for i in nodes:
        print(i,"  ",a[i])

def betweenness_centrality(g):
    a=net.closeness_centrality(g)
    nodes=list(a.keys())
    degree=list(a.values())
    for i in nodes:
        print(i,"  ",a[i])

    
def degree_prestige(g):
    a=list(nodes.values())    
    for i in range(len(nodes)):
        print(nodes[i].n,"  ",(nodes[i].pre)/(len(a)-1))


def proximity_prestige(g):
    a=list(nodes.values())
    for i in range(len(a)):
        num=0
        dist=0
        for j in range(len(a)):
            if(net.has_path(g,source=a[j].n,target=a[i].n)):
                num=num+1
                dist=dist+net.shortest_path_length(g,source=a[j].n,target=a[i].n)
        print(a[i].n,"  ",num/dist)               
                
        
def rank_prestige(g):
    a=list(nodes.values())
    p=net.pagerank(g,alpha=0.75)
    for i in range(len(a)):
        val=0
        l=list(a[i].i.values())
        for j in range(len(l)):
            if l[j] in list(p.keys()):
                val=val+p[l[j]]
        print(a[i].n,"  ",val)
            
def co_citation(g):
    a=list(nodes.values())
    for i in range(8):
        for j in range(i+1,8):
            c=0
            ls=[]
            for k in a:
                if a[i].n in list(k.o.values()):
                    if a[j].n in list(k.o.values()):
                        c=c+1
                        ls=ls+[k.n]
            print("(",a[i].n,a[j].n,")"," ",c," ",ls)

def bib_coupling(g):
    a=list(nodes.values())
    for i in range(8):
        for j in range(i+1,8):
            c=0
            ls=[]
            for k in a:
                if a[i].n in list(k.i.values()):
                    if a[j].n in list(k.i.values()):
                        c=c+1
                        ls=ls+[k.n]
            print("(",a[i].n,a[j].n,")"," ",c," ",ls)
    
def pagerank(g):
    a=net.pagerank(g,alpha=0.75)
    nodes=list(a.keys())
    degree=list(a.values())
    for i in nodes:
        print(i,"  ",a[i])
    
    
    
    




    
