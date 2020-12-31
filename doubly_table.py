class Node:
    def __init__(self,key,val):
        self.value = val
        self.next = None
        self.prev = None
        self.key = key
        self.index = 0
        
class HashTable:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
                  
    def insert_by_Index(self,index,key,val):
        if index == 0:
            self.insert_at_First(key, val) #inserts Node at first if its being inserted at index 0
        elif index == self.n-1:
            self.insert_at_Last(key, val) #inserts Node at the end if index is last index of the list
        else:
            new = Node(key, val) 
            old = self.getNode_by_Index(index) #inserts node before the old node at given index, changing its pointers
            new.next = old 
            new.prev = old.prev 
            new.next.prev = new
            new.prev.next = new
            self.n += 1
            return new
        
    def getNode_by_Key(self,key) -> Node: #helper function to get a node by the given key
        n = self.head
        while n.key != key: #iterates through the list until the keys match
            if n.next is None:
                return 999 #returns error value if it has gone through the list without finding a key
            n = n.next
        return n
        
    def getNode_by_Value(self,value) -> Node: #helper function to get a node by the given value
        n = self.head
        while n.value != value: #iterates through the list until the values match
            if n.next is None:
                return 999 #returns error value if it has gone through the list without finding a value
            n = n.next
        return n

    def getNode_by_Index(self,index) -> Node: #helper function to get a node by the given index
        if index == self.n-1: #if index is the last in the list, returns the tail
            return self.tail 
        if index == 0: #returns the head if the index is 0
            return self.head
        p = self.head 
        for i in range(index): #iterates through the list as many times as the given index to reach the correct node
            p = p.next
        return p
                           
    def getValue_by_Index(self,index):
        if index > self.n-1:
            return "Out of index"
        v = self.getNode_by_Index(index) #calls the helper function and returns Node's value
        return v.value
                
    def getValue_by_Key(self,key):
        v = self.getNode_by_Key(key) #calls the helper function and returns Node's value
        if v == 999: #error
            return
        return v.value

    def delete_by_Value(self,val):
        d = self.getNode_by_Value(val) #calls the helper function to find the right node
        if d == 999: #error
            print("Value was not found")
            return
        if d.prev is None: #if found node is the head, arranges its pointers appropriately
            d.next.prev = None
            self.head = d.next
        if d.next is None: #if found node is the tail, arranges its pointers appropriately
            d.prev.next = None
            self.tail = d.prev
        else: #if found node is somewhere in the middle, arranges points appropriately
            d.prev.next = d.next 
            d.next.prev = d.prev
        self.n -= 1
        
    def delete_by_Index(self,index):
        d = self.getNode_by_Index(index) #calls helper function to get the correct node
        d.prev.next = d.next #set nodes of previous and next nodes
        d.next.prev = d.prev #set nodes of previous and next nodes
        self.n -= 1

    def delete_by_Key(self,key):
        d = self.getNode_by_Key(key) #calls helper function to get the correct node
        if d == 999: #error
            print("Key was not found")
            return
        if d.prev is None: #if found node is the head, arranges its pointers appropriately
            d.next.prev = None 
            self.head = d.next
        if d.next is None: #if found node is the tail, arranges its pointers appropriately
            d.prev.next = None
            self.tail = d.prev
        else: #if found node is somewhere in the middle, arranges points appropriately
            d.prev.next = d.next
            d.next.prev = d.prev
        self.n -= 1
    
    def print_all_keyValues(self):
        out = self.head
        print('[', end = "")
        while out is not None: #iterates through the list printing each node value
            print("%r" % out.key, end = " ")
            if out.next is not None:
                print(",", end="")
            out = out.next
        print("]")

    def insert_at_First(self,key,val):
        new = Node(key,val)
        new.next = self.head 
        new.prev = None
            #change prev of head node to new node  
        if self.head is not None: 
            self.head.prev = new
            #move the head to point to the new node 
        self.head = new
        if self.n == 0:
            self.tail = self.head 
        self.n += 1
            
    def insert_at_Last(self,key,val):
        new = Node(key,val)
        self.tail.next = new
        self.tail.next.prev = new
        new.next = None 
        new.prev = self.tail
            #change prev of head node to new node  
        if self.tail is not None: 
            self.tail.prev = new
            #move the head to point to the new node 
        self.tail = new
        if self.n == 0:
            self.head = self.tail
        self.n += 1

    def length(self):
        if self.head != None and self.tail != None:
            return self.n
        else:
            print("Note: Table is Empty!")
            return 0

# test cases               
d1 = HashTable()

d1.insert_at_First("csulb",1)
d1.insert_at_First("CECS",2)
d1.insert_at_First("CECS274",3)
d1.insert_at_Last("CS",4)
d1.insert_by_Index(0,"life",12)
d1.insert_at_First("time",44)
d1.insert_by_Index(3,"value",12)
d1.insert_by_Index(4,"good",26)
d1.insert_by_Index(4,"eng",27)
d1.delete_by_Value(8)
d1.delete_by_Index(1)
d1.delete_by_Key("good")
d1.insert_at_First("why",24)
d1.insert_at_Last("how",57)
d1.insert_by_Index(3,"know",145)
d1.insert_by_Index(4,"yes",243)
d1.delete_by_Index(1)
d1.delete_by_Key("juan")
d1.delete_by_Value(243)

print("HashTable: ",end="")
d1.print_all_keyValues()
print("Length:",d1.length())
print("Value at Key 'eng':",d1.getValue_by_Key("eng"))
print("Value at Key 'csulb':",d1.getValue_by_Key("csulb"))
print("Value at Key 'good':",d1.getValue_by_Key("good"))
print("Value at index 3:",d1.getValue_by_Index(3))
print("Value at index 7:",d1.getValue_by_Index(7))






