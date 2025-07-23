class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class bst: #binary search tree              # 6
                                            # /\
                                            # 1 7
    def __init__(self,value):
        self.root = node(value)

    def insert(self,val):
        temp = self.root
        new = node(val)
       
        while(True):
            if (temp.data > val):
                if temp.left is None:  
                    temp.left = new
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new 
                    break
                else :
                    temp = temp.right
    def display(self):
        def go(node):
            if node is not None:
                go(node.left)
                print(node.data)
                go(node.right)
    
        go(self.root)

                
tree = bst(6)        # Root node
tree.insert(1)
tree.insert(7)
tree.insert(3)
tree.insert(8)
tree.insert(0)
tree.insert(5)

tree.display()
           


    