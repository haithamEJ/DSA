#preorder , postorder , inorder 
from collections import deque


class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

 
    def preorder(self,noeud):
        if noeud is None:
            return
        
        print(noeud.value)
        self.preorder(noeud.left)
        self.preorder(noeud.right)
    
    def inorder(self,noeud):
        if noeud is None:
            return
        
        self.inorder(noeud.left)
        print(noeud.value)
        self.inorder(noeud.right)
    
    def postorder(self,noeud):
        if noeud is None:
            return
        
        self.postorder(noeud.left)
        self.postorder(noeud.right)
        print(noeud.value)


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
            
        


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(10)


A.left = B 
A.right = C
B.left = D
B.right = E
C.left = F

# A.preorder(A)
# print("==================================")
# A.inorder(A)
# print("==================================")
# A.postorder(A)

A.bfs(A)