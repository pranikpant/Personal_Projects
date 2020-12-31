class priorityQueue:
    def __init__(self):
        self.heap=[]                # an array of integers
        self.size = 0               # the size of heap

    def __len__(self):
        return self.size

    def parent(self,index):
        return int((index-1)/2) #index at which parent node is mapped to
        
    def leftChild(self,index):
        return (index * 2) + 1 #index at which left child is mapped to
        
    def rightChild(self,index):
        return (index * 2) + 2 #index at which right child is mapped to
        
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2] #swaps values at the given indexes
        self.heap[index2] = temp
        
    def insert(self,x):
        self.heap.append(x) #adds new value to the end 
        self.size += 1
        self.upHeap(len(self.heap)-1) #upheaps the value to get it to the right spot
        
    def delete_Max(self):
        self.swap(0, len(self.heap)-1) #swaps the head and the tail
        maximum = self.heap.pop() #removes the tail (the old head)
        self.size -= 1
        self.downHeap(0) #downheaps the head (the old tail) to where it needs to go
        return maximum #returns the old head that was deleted
        
    def upHeap(self, index):
        if self.size == 1: #if theres only 1 value, returns (no upheap necessary)
            return 
        parent = self.parent(index)
        if parent < 0: # Return if we arrive at the root node
            return
        if self.heap[index] > self.heap[parent]: # Swap nodes if current is larger than the parent
            self.swap(index, parent)
            self.upHeap(parent) #recursion to make sure it goes through the entire heap

    def downHeap(self, index):
        if self.size == 1: #if theres only 1 value, returns (no downheap necessary)
            return
        left_child = self.leftChild(index)
        child = left_child
        if left_child >= len(self.heap)-1:
            return
        right_child = self.rightChild(index)
        if self.heap[left_child] < self.heap[right_child]: #if right child is greater, use right child for comparison
            child = right_child
        if self.heap[child] > self.heap[index]: #swaps nodes if the child is greater
            self.swap(child, index)
            self.downHeap(child) #recursion to make sure it goes through the entire heap

#Test case
h = priorityQueue()
h.insert(22)
h.insert(31)
h.insert(12)
h.insert(46)
h.insert(37)
h.insert(32)
print(h.heap)

x = h.delete_Max()
print(h.heap)
x = h.delete_Max()
h.insert(66)
h.insert(42)
h.insert(56)
print(h.heap)
x = h.delete_Max()
h.insert(41)
h.insert(121)
print(h.heap)
x = h.delete_Max()
print(h.heap)

# Default outputs:
#[46, 37, 32, 22, 31, 12]
#[37, 31, 32, 22, 12]
#[66, 32, 56, 22, 31, 12, 42]
#[121, 56, 42, 32, 31, 12, 41, 22]
#[56, 32, 42, 22, 31, 12, 41]