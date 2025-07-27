from collections import deque

class Node :
    def __init__(self,value,left=None,right=None):
       self.value = value
       self.left = left
       self.right = right

class bs:
    def __init__(self):
        self.root = None

    def insert(self,new:Node):
      
        if self.root is None:
            self.root = new
            return
        
        tmp = self.root
        parent = None #the role dial had khona howa tchof fin 7bssti so when tmp iwssl l none and the while loop breaks check 

        while tmp is not None:
            if tmp.value > new.value:
                parent = tmp
                tmp = tmp.left
                

            elif tmp.value < new.value:
                parent = tmp
                tmp = tmp.right
            else: return

        if parent.value > new.value:
                parent.left = new
        elif parent.value < new.value:
                parent.right = new

    
        
        
       

    def bfs(self,noeud):
        if noeud is None:
            return
        
        queue = deque()
        queue.append(noeud)
        print(noeud.value)
        while queue:
            noeud = queue[0]
           
            if noeud.left is not None:
                lissr = noeud.left
                print(lissr.value) 
                queue.append(lissr)
            if noeud.right is not None:
                limn = noeud.right
                print(limn.value)
                queue.append(limn)
            

           

            queue.popleft()


chjra = bs()
E = Node(10)
F = Node(5)
G = Node(15)
H = Node(12)
I = Node(3)
J = Node(3)
K = Node(7)

chjra = bs()
chjra.insert(E)  # 10 root
chjra.insert(F)  # 5 left of 10
chjra.insert(G)  # 15 right of 10
chjra.insert(H)  # 12 left of 15
chjra.insert(I)  # 18 right of 15
chjra.insert(J)  # 3 left of 5
chjra.insert(K)  # 7 right of 5

chjra.bfs(E)
