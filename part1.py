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

def hits(g):
    h,a=net.hits(g, max_iter=50)
    print("\nHub Score\n")
    nodes=list(h.keys())
    degree=list(h.values())
    for i in nodes:
        print(i,"  ",h[i])

    print("\nAuthority Score\n")
    nodes=list(a.keys())
    degree=list(a.values())
    for i in nodes:
        print(i,"  ",a[i])

    
    

    
    
    
    




    
