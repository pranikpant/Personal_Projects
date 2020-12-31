import numpy as np
from base import BaseList

class DLList(BaseList):
    
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i: int) -> Node: 
        if i < (self.n/2): #if index is within first half of the list, use the head to iterate forward
            p = self.dummy.next
            for x in range(i):
                p = p.next
        else: #use tail if index is in second half of the list
            p = self.dummy
            for x in range(self.n-i):
                p=p.prev
        return p

    def get(self, i: int):
        if i < 0 or i >= self.n: 
            raise IndexError()
        return self.get_node(i).x

    def set(self, i: int, x):
        u = self.get_node(i) #calls get node function to get the node at specified index
        y = u.x 
        u.x = x #sets the data at the node to specified value
        return y

    def _remove(self, w: Node):
        if self.n == 0:
            print("List is empty")
            return
        w.prev.next = w.next #makes the previous node point the next node
        w.next.prev = w.prev #makes the next node point to the previous node

    def remove(self, i: int):
        if i < 0 or i >= self.n: 
            print("Index is out of range")
            return
        self._remove(self.get_node(i))
        self.n -= 1

    def add_before(self, w: Node, x):
        u = DLList.Node(x) #creates a new node with specified data
        u.prev = w.prev #sets the new node's prev pointer to the node that will be before it
        u.next = w #sets the new nodes next pointer to the node it is being added behind
        u.next.prev = u #sets the node in front of the new node's prev pointer to the new node
        u.prev.next = u #sets the node behind the new node's next pointer to the new node
        return u

    def add(self, i: int, x):
        if i < 0 or i > self.n:    
            raise IndexError()
        self.add_before(self.get_node(i), x)
        self.n += 1

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

    def size(self) -> int:
        return self.n

    def append(self, x : np.object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        if self.n==1:
            return True
        if self.n % 2 == 0: #if the list has an even number of elements
            temp = self.get_node((self.n//2)-1) #set pointer to the node left of the middle
            current = self.get_node((self.n//2)) #set pointer to the node right of the middle
            for x in range(self.n-(self.n//2)): #iterates through the list comparing the right and left
                if temp.x != current.x:
                    return False
                temp = temp.prev #iterates left pointer left each time it loops
                current = current.next #iterates right pointer right each time it loops                
        else: #if odd number of elements
            temp = self.get_node((self.n//2)-1) #ignore the middle element, set pointer to left of middle element 
            current = self.get_node((self.n//2)+1) #ignore the middle element, set pointer to right of middle element 
            
            for x in range(self.n-(self.n//2)-1):#iterates through the list comparing the right and left
                if temp.x != current.x:
                    return False
                temp = temp.prev #iterates left pointer left each time it loops
                current = current.next #iterates right pointer right each time it loops 
        return True 

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

dl = DLList()
dl.remove(0) # print error message or raise exception
dl.add(0,5)
print(dl)   # print [5]
dl.add(0,1)
print(dl)   # print [1,5]
dl.add(1,3)
print(dl)   # print [1,3,5]
dl.add(2,6)
print(dl)   # print [1,3,6,5]
dl.remove(2)
print(dl)   # print [1,3,5]
dl.add(1,2)
print(dl)   # print [1,2,3,5]
dl.add(3,4)
print(dl)   # print [1,2,3,4,5]
dl.append(6)
print(dl)   # print [1,2,3,4,5,6]
dl.set(5,1)
print(dl)   # print [1,2,3,4,5,1]
dl.remove(3)
print(dl)   # print [1,2,3,5,1]
print(dl.isPalindrome())    # print False
dl.set(1,5)
print(dl)   # print [1,5,3,5,1]
print(dl.isPalindrome()) #print True
