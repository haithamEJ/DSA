class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.before = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self,value):
        new = Node(value)
        if self.head == None:
            self.head = new
        else:
            temp = self.head
            new.next = temp
            self.head = new

    def insertLast(self,value):
        new = Node(value)
        if self.head == None:
            self.head = new
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next 
            
            temp.next = new
            new.before = temp

    def insertAt(self,value,pos):
        count = 1
        count2 = 1
        new = Node(value)
        temp = self.head
        temp2 = self.head

        if pos == 1:
            self.insertFirst(value)
            return
        
        while count != pos:
            temp = temp.next
            count = count +1
        
        
        while count2 != pos-1:
            temp2 = temp2.next
            count2 = count2 +1
        

        new.next = temp
        temp2.next = new
        



    def display(self):
        temp = self.head.next
        print(f'{self.head.value}->',end="")
        while temp != None:
            print(f'<-{temp.value}->',end="")
            temp = temp.next

        print("None")

    


dll = LinkedList()


dll.insertFirst(4)
dll.insertFirst(1)
dll.insertFirst(13)
dll.insertLast(99)
dll.insertLast(20)

dll.display()

dll.insertAt(33323,1)

dll.display()
    