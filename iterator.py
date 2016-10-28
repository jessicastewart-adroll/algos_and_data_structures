'''
Implement Iterator class with next and hasNext which run O(1) time.
'''
from collections import deque

class Iterator(object):
    def __init__(self):
        self.deque = deque()
        
    def my_append(self, n):
        self.deque.append(n)
        
    def next(self):
        if self.hasNext():
            print(self.deque.popleft())
        else:
            print('Empty')
        
    def hasNext(self):
        return True if len(self.deque) >0 else False
        
        
test = Iterator()
test.my_append('first')
test.my_append('second')
test.my_append('third')

test.hasNext()
test.next()
test.hasNext()
test.next()
test.hasNext()
test.next()
test.hasNext()
test.next()
