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
   


    def delete(self,dele:Node):
        if self.root is None:
            self.root = dele
            return
        
        
        tmp = self.root
        parent = None 

        while tmp.value != dele.value:
            if tmp.value > dele.value:
                parent = tmp
                tmp = tmp.left
                

            elif tmp.value < dele.value:
                parent = tmp
                tmp = tmp.right
            else: return

        

        if (parent.value > dele.value) :
                parent.left = None
        elif (parent.value < dele.value) :
                parent.right = None
    

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
A = Node(40)
B = Node(30)
C = Node(50)
D = Node(25)
E = Node(35)
F = Node(45)
G = Node(60)

chjra = bs()
chjra.insert(A)  
chjra.insert(B)  
chjra.insert(C)  
chjra.insert(D) 
chjra.insert(E)  
chjra.insert(F) 
chjra.insert(G)  

chjra.bfs(A)
print("=========================================================")
chjra.delete(C)
print("=========================================================")
chjra.bfs(A)

'''
deletion u still have to deal with some stuff 

Node has no children (a leaf) DONE
Node has one child
Node has two children

'''