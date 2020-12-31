from utils import new_array
from base import BaseSet

class ArrayQueue(BaseSet):

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):

        self.a = new_array(1)
        self.n = 0
        self.capacity = len(self.a)
        self.front = -1 
        self.rear = -1
        self.ghost = 0
    
    def resize(self, capacity):

        b = new_array(2*capacity) #doubles array size
        for i in range(self.capacity):
            b[i] = self.a[i]
        self.a = b
        self.capacity = 2*capacity
    
    def add(self, x):

        if self.front == -1 and self.rear == -1: #there are no elements in the array yet
            self.front = self.rear = 0
            self.a[self.rear] = x #sets first element to x
        elif (self.rear+1)%self.capacity == self.front: #array is full, calls for resize
            self.resize(self.capacity)
            self.add(x) #calls function back           
        else:
            self.rear = (self.rear+1)%self.capacity #searches for an empty space within array to maximize usage
            self.a[self.rear] = x
        
        print(self.a)

    def remove(self):

        if self.front == -1 and self.rear == -1: #queue is empty
            print("Queue is empty")
        elif self.front == self.rear: #only 1 element left in the array
            self.ghost = self.a[self.front] #sets the element removed to a variable
            self.a[self.front] = None #removes element
            self.front = self.rear = -1
            return self.ghost    
        else:
            self.ghost = self.a[self.front] #sets element removed to a variable
            self.a[self.front] = None #removes element
            self.front = (self.front+1)%self.capacity 
            print(self.a)
            return self.ghost
    
    def __str__(self):

        s = "["
        for i in range(self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        s += "]"
        return s

queue = ArrayQueue()
#sample test cases 
queue.remove() # it prints “Queue is empty”
queue.add(1)
queue.add(2)
queue.add(3)
queue.remove() # it returns 1
queue.add(4)
queue.remove() # it returns 2
queue.remove() # it returns 3
queue.add(5)
queue.remove() # it returns 4
queue.remove() # it returns 5
queue.remove() # it prints “Queue is empty”
queue.add(2)
queue.add(3)
queue.add(1000)
queue.remove()
queue.remove()
