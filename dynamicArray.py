from utils import new_array

class DynamicArray:

    def __init__(self):
        self.a = new_array(1) #creates a new array of length 1
        self.n = 0
        self.capacity = len(self.a)

    def insert(self, k, value):

        if self.n == self.capacity: #compares number of elements to capacity of array to call for resize
            b = new_array(2 * self.capacity) #doubles array size

            for j in range(k):
                b[j] = self.a[j] #sets array a elements over to b
            b[k]=value 

            for j in range(k,self.n): 
                b[j+1]=self.a[j] #shifts elements over 1 to the right
            self.capacity=2*self.capacity
            self.a=b #transfers array elements back over to a               

        else:

            for j in range(self.n, k, -1):
                self.a[j] = self.a[j-1] #inserts value into array
            self.a[k] = value

        self.n += 1

    def __str__(self):
        s = "["
        for i in range(self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        s += "]"
        return s


dynamic_array = DynamicArray()
#sample test cases
dynamic_array.insert(0,1)
dynamic_array.insert(0,2)
dynamic_array.insert(1,3)
dynamic_array.insert(3,5)
dynamic_array.insert(2,4)
dynamic_array.insert(4,7)
dynamic_array.insert(6,9)
dynamic_array.insert(2,3)
print(dynamic_array)