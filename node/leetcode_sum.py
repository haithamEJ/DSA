class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        tmp1 = l1
        t1= []

        tmp2 = l2
        t2 = []

        while tmp1:
            t1.append(tmp1.val)
            tmp1= tmp1.next
        
        while tmp2:
            t2.append(tmp2.val)
            tmp2= tmp2.next

        result1 = int(''.join(map(str, t1)))
        result2 = int(''.join(map(str, t2)))

        total = result1+result2

        digits = list(map(int, str(total)[::-1]))
        count = 0
        jdid = ListNode()

        while(count!= len(digits)-1):
            jdid.val = digits[count]
            count = count + 1

        return jdid
        

        
        