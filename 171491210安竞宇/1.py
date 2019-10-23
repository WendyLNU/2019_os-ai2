A=0
B=1
C=2
D=3
E=4
F=5
G=6
H=7
I=8
L=9
M=10
N=11
O=12
P=13
R=14
S=15
T=16
U=17
V=18
Z=19
PLACES_NUM=20#构建一个20*20的矩阵
#地图
class Graph:
    def __init__(self):
        self.remania_graph=[[0]*PLACES_NUM for i in range(PLACES_NUM)]
    def add_edge(self,_from,_to,_value):
        if _from < PLACES_NUM:
            if _to < PLACES_NUM:
                self.remania_graph[_from][_to]=_value

    def get_edge(self,_from,_to):
        return self.remania_graph[_from][_to]
class Stack:#问题的最终解
    def _init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
        return
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        if self.stack:
            return False
        return True
#close表
class Queue:
    def __init__(self):
        self.queue=[]
    def put(self,value):
        self.queue.append(value)
        return
    def get(self):
        return self.queue.pop(0)
    def contain(self,value):
        return value in self.queue
    def is_empty(self):
        if self.queue:
            return False
        return True
#open表
class PriortyQueue:
    def __init__(self):
        self.queue=[]
    def put(self,node_cost):
        self.queue.append(node_cost)
    def get(self):
        if self.queue:
            min_i=0
            min_cost=self.queue[min_i][1]
            for i in range(len(self.queue)):
                if self.queue[i][1]<min_cost:
                    min_i=i
                    min_cost=self.queue[i][1]
            return self.queue.pop(min_i)
    def contain(self,value):
        for i in range(len(self.queue)):
            if self.queue[i][0]==value:
                return self.queue[i],True
        return None,False
    def is_empty(self):
        if self.queue:
            return False
        return True
#初始化无向图
def init_graph():
    graph =Graph()
    graph.add_edge(O,Z,71)
    graph.add_edge(O,S,151)
    graph.add_edge(A,Z,75)
    graph.add_edge(A,S,140)
    graph.add_edge(A,T,118)
    graph.add_edge(T,L,111)
    graph.add_edge(L,M,70)
    graph.add_edge(M,D,75)
    graph.add_edge(D,C,120)
    graph.add_edge(S,R,80)
    graph.add_edge(S,F,99)
    graph.add_edge(R,C,146)
    graph.add_edge(F,B,211)
    graph.add_edge(R,P,97)
    graph.add_edge(C,P,138)
    graph.add_edge(P,B,101)
    graph.add_edge(B,G,90)
    graph.add_edge(B,U,85)
    graph.add_edge(U,H,98)
    graph.add_edge(U,V,142)
    graph.add_edge(V,I,92)
    graph.add_edge(I,N,87)
    graph.add_edge(H,E,86)

    return  graph
def a_star(graph,h,_root,_goal):
    g=[0]*PLACES_NUM
    parents=[0]*PLACES_NUM
    pq_open=PriortyQueue()
    q_close=Queue()
    s_path=Stack()
    s_parent=Stack()
    pq_open.put([_root,0])

    while pq_open.is_empty()==False:
        parrent_node=pq_open.get()
        if parrent_node==_goal:
            break
        q_close.put(parrent_node[0])
        for i in range(20):
            length=graph.get_edge(parrent_node[0],i)
            if length!=0:
                node,result=pq_open.contain(i)
                f=parrent_node[1]-h[parrent_node[0]]+length+h[i]
                if q_close.contain(i):
                    continue
                elif result==True:
                    if node[1]>f:
                        node.pop()
                        parents[i]=parrent_node[0]
                        pq_open.put([i,f])
                else:
                    parents[i]=parrent_node[0]
                    pq_open.put([i,f])
    path=[]
    cost=0
    print("parents:",parents)
    p=_goal
    while p!=_root:
        cost +=graph.get_edge(p,parents[p])
        path.append(p)
        p=parents[p]
    length=len(path)-1
    print('path:',_root,end='')
    for i in range(length+1):
        print("-->",path[length-i],end='')
    print()
    return cost
if __name__ == '__main__':
    graph=init_graph()
    h=(366,0,160,242,161,178,77,151,226,244,241,234,380,98,193,253,329,80,199,374)
    print("node:","A","B")
    cost=a_star(graph,h,eval('A'),eval('B'))
    print('cost:',cost)
    print()
    print("node","C","B")
    cost=a_star(graph,h,eval('C'),eval('B'))
    print('cost:',cost)
    print()
    print("node","U","B")
    cost=a_star(graph,h,eval('U'),eval('B'))
    print('cost:',cost)
    print()



#A*