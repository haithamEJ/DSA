from collections import deque

class queue:
#fifo
    def __init__(self,arrayInfo):
         self.list = arrayInfo
    
    def dequeu(self):
         self.list = deque(self.list)
         self.list.popleft()
         print(list(self.list))

q = queue([1,2,3,4])
q.dequeu()