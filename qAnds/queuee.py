# queue = ["Amar", "Akbar", "Anthony"] 
# queue.append("Ram") 
# queue.append("Iqbal") 
# print(queue) 

# print(queue.pop(0)) 

# print(queue) 

# print(queue.pop(0)) 

# print(queue) 

from collections import deque

q = deque([10, 20, 30, 40])
q.popleft() 
print(q)

#queue fifo
