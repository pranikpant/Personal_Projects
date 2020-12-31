class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        if self.rear is None: #if list is empty
            self.front = self.rear = Node(data) #creates new node and sets front and rear equal to it
        else: #if list is not empty
            self.rear.next = Node(data) #adds new node to the rear
            self.rear = self.rear.next
    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")     
        else:
            value = self.front.data
            self.front = self.front.next #moves head pointer to the right, dequeing the element at the front
            print(value)
            return value
            
    def is_empty(self):
        return self.size == 0

    def len(self):
        count = 0
        current = self.front
        while(current): #iterates through the list until it reaches the end to get the count of nodes
            count += 1
            current = current.next
        return count
    
    def first(self):
        print(self.front.data) #prints the head (first element of list)
    
    def rotate(self):
        if self.front is None: 
            print("Queue is empty")
            return
        self.rear.next = self.front #sets tail to point to the head
        self.front = self.front.next #sets the 2nd element as new head
        self.rear = self.rear.next #old head becomes new tail

queue = LinkedQueue()
queue.dequeue() # print error message or throw exception
queue.enqueue(6) # queue = 6
queue.enqueue(2) # queue = 6->2
queue.enqueue(7) # queue = 6->2->7
queue.dequeue() # print 6 and queue = 2->7
queue.first() # print 2 and queue = 2->7
queue.enqueue(1) # queue = 2->7->1
queue.rotate() # queue = 7->1->2
queue.enqueue(5) # queue = 7->1->2->5
queue.dequeue() #prints 7
queue.dequeue() #prints 1
queue.dequeue() #prints 2
queue.dequeue() #prints 5
queue.dequeue() #prints error message
            