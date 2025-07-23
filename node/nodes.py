class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self):
        temp = self.head

        while temp:
            print(f"{temp.data}->",end="")
            temp = temp.next

        print("NULL")

    def insertAtEnd(self,data):
        newNode = Node(data)
        newNode.next = None
        temp = self.head
            
        while temp.next:
            temp = temp.next
        
        temp.next = newNode

    def size(self):
        temp = self.head
        i = 0
        while temp:
            i = i + 1
            temp = temp.next   
        return i

    def insertAtIndex(self,index,data):
        newNode = Node(data)
        temp = self.head
        temp2 = self.head
        i = 1
        taille = self.size()

        if(index > taille) : return

        while i != index :
            temp = temp.next
            i += 1
        
        temp2 = temp.next
        temp.next = newNode
        newNode.next = temp2
    
    def remove_node(self,info):
        temp = self.head   
        temp2 = self.head
        while temp.next.data != info :
            temp = temp.next

        print(temp.data)
        temp2 = temp.next
        temp.next = temp2.next

      
    
l = LinkedList()


l.insertAtBegin(1)
l.insertAtEnd(2)
l.insertAtEnd(3)
l.insertAtEnd(4)
l.insertAtIndex(2,22)
l.display()

l.remove_node(2)

l.display()

