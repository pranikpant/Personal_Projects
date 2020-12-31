class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end = ', ')
            temp = temp.next

    def insert(self, data):
        new_node = Node(data) #creates a new node
        if self.head is None:
            self.head = new_node #if list is empty, makes new node the head
            return
        last = self.head
        while last.next: #iterates until last node
            last = last.next
        last.next = new_node
    
def merge(l1, l2):
    temp = dummy = Node(0) #creates a dummy node
    while True:
      if l1 is None and l2 is None: #if list is empty
        break
      elif l1 is None: #if first list is empty, returns 2nd list
        temp.next = l2
        break
      elif l2 is None: #if 2nd list is empty, returns first list
        temp.next = l1
        break
      else:
        smallerData = 0 #variable to hold smaller value
        if l1.data <= l2.data: 
          smallerData = l1.data
          l1 = l1.next
        else:
          smallerData = l2.data
          l2 = l2.next
        newNode = Node(smallerData) #new node made with the smaller value
        temp.next = newNode #dummy node points to new node
        temp = temp.next
    return dummy.next

# Test merge() function
# Linked List of L
L = LinkedList()
L.insert(3)
L.insert(6)
L.insert(9)
L.insert(14)
L.insert(17)
# Linked List of M
M = LinkedList()
M.insert(2)
M.insert(8)
M.insert(15)
M.insert(19)
M.insert(22)
# Merge Function
LM = LinkedList()
LM.head = merge(L.head, M.head)
LM.printLL()
