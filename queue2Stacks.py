from utils import new_array

class QueueStacks(object):

    def __init__(self):

        self.stack1 = []
        self.stack2 = []
    
    def add(self, x):
        self.stack1.append(x)
    
    def remove(self):

        if len(self.stack1) == 0:
            print("Queue is empty")
        else:
            capacity = len(self.stack1)-1
            for i in range(capacity):
                self.stack2.append(self.stack1.pop())
            removedvalue = self.stack1.pop()

            for j in range(capacity):
                self.stack1.append(self.stack2.pop())

            return(removedvalue)

queue = QueueStacks()
queue.remove() # it prints “Queue is empty”
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.remove()) # it returns 1
queue.add(4)
print(queue.remove()) # it returns 2
print(queue.remove()) # it returns 3
queue.add(5)
print(queue.remove()) # it returns 4
print(queue.remove()) # it returns 5
print(queue.remove()) # it prints “Queue is empty”