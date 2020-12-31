from utils import new_array
import numpy
from base import BaseList

class ArrayStack(BaseList):
    
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):

        self.a = new_array(1)
        self.n = 0
        self.j = 1
        self.capacity = len(self.a)

    def get(self, i):

        return self.a[i] #returns the element of specified index

    def set(self, i, x):

        self.a[i] = x
        return self.a[i] #sets array element with specified element, index and returns it

    def add(self, i, x): 

        if self.n == self.capacity: #if array is full, calls resize
            self._resize()
        
        if self.n == 0: #if no elements in array, uses set function to add
            self.set(i, x)
        else:
            #self.a[i%len(self.a)] = self.a[i-1]
            b = new_array(self.capacity) #makes a new array b and copies array a into it
            for j in range(i):
                b[j] = self.a[j]
            b[i]=x

            for j in range(i,self.n): 
                b[j+1]=self.a[j]
            self.a=b

        self.n += 1

        return self.a
        #print(self.a)

    def remove(self, i): 

        if self.n == 0: #nothing in array
            print("List is empty")
        elif self.a[i] == None: #no element at given index
            print("There is nothing at that index.")
        else:
            for j in range(i+1, self.n+1): #iterates through the array and shifts it to the left
                self.set(j-1, self.a[j])
            self.n -= 1
            return self.a
  
    def _resize(self):
        b = new_array(2*self.capacity) #resizes array to double size
        for i in range(self.capacity):
            b[i] = self.a[i]
        self.a = b
        self.capacity = 2*self.capacity

stack = ArrayStack()
stack.add(0,1)
stack.add(0,2)
stack.add(1,3)
stack.add(3,5)
stack.add(2,4)
print(stack.get(0)) # it prints 2
print(stack.get(1)) # it prints 3
print(stack.get(2)) # it prints 4
print(stack.get(3)) # it prints 1
print(stack.get(4)) # it prints 5
