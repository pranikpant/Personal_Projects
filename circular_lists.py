class Node: 
      
    # Constructor to create  a new node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CreateList: 
      
    # Constructor to create a empty circular linked list 
    def __init__(self): 
        self.head = None
        self.count = 0
  
    # Function to insert a node at the beginning of a 
    # circular linked list 
    def add(self, data): 
        if not self.head:
            self.head = Node(data) #creates a new node and makes it head
            self.head.next = self.head
        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head: #iterates through the list
                current = current.next
            current.next = new_node
            new_node.next = self.head #points it back to the head
        self.count += 1

    # Function to print nodes in a given circular linked list 
    def print(self): 
        temp = self.head 
        if self.head is not None: 
            while temp: 
                print (temp.data, end = ' ')
                temp = temp.next
                if (temp == self.head): 
                    break
    
    def countNodes(self):
        print("\ncount number:", self.count)
  

class CircularLinkedList:    
    cl = CreateList();    
    #Adds data to the list    
    cl.add(4)    
    cl.add(5)    
    cl.add(7)    
    cl.add(8)    
    cl.add(12)   
    cl.add(56)   
    cl.add(85)
    cl.add(41) 
    #Displays all the nodes present in the list   
    cl.print()
    cl.countNodes() 
