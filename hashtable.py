class Node:
    def __init__(self,key,value):  #create a Node class for linked list collision control
        self.value = value
        self.key = key
        self.next = None

class Entry:
    def __init__(self,key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self,numBuckets):
        self.table = numBuckets * [None] #intialize hash table
        self.numBuckets = numBuckets
        self.n = 0
    
    def simple_hash(self,key):
        if type(key) is str:  
            x = 0
            for character in key:
                x += ord(character) # add in value of next character
        else:
            x = key
        h = x % self.numBuckets #compression function to change integer to index
        return h
    
    def add(self,key,value):
        h = self.simple_hash(key)
        if self.table[h] is None: #checks to see if simple hash works with no collision
            self.table[h] = Node(key, value) #each input is a Node in case of collisions
        else:
            temp = self.table[h]
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(key, value) #adds a node at the end of the linked list at the index
            temp.next.next = None
        return self.table[h].value
    
    def updateValue(self,key,value):
        h = self.simple_hash(key)
        temp = self.table[h]
        if temp.next is None:
            temp.value = value
            return
        while True:
            if temp.key == key: #if node has the same key, updates its values
                temp.key = key
                temp.value = value
                return
            if temp.next is None:
                break
            temp = temp.next #iterates through the list
        self.table[h] = temp
        return self.table[h].value
    
    def delete(self,key):
        h = self.simple_hash(key)
        temp = self.table[h]
        if temp is None: #if there is no value at the index
            print("There is no value associated with this key")
            return
        if temp.next is None: #if there is no linked list at the index
            self.table[h] = None
            return
        else: #if there is a linked list at the index
            while True:
                if temp.key == key:
                    while temp.next is not None:
                        temp.value = temp.next.value #copies the values of the following node to this node
                        temp.key = temp.next.key #copies the keys
                        temp = temp.next #iterates to next node
                    temp.value = None #sets the last node as None to delete it
                    temp.key = None
                    return 
                temp = temp.next #goes through the list to find node with given key
            print("Error: Key does not exist") #error statement if the given key doesnt exist
            return
    
    def lookUp(self,key):
        h = self.simple_hash(key)
        temp = self.table[h]
        while temp:
            if temp.key == key:
                print("Value at Key " + str(key) + ": " + temp.value)
                return
            else:
                temp = temp.next #iterates through the list to find node with given key
        print("Error: Key does not exist")
        return
        
    def print(self):
        for k in range (self.numBuckets):
            current = self.table[k]
            if current is None: #prints none whereever the node is None 
                print(None)
            else:
                while current is not None:
                    if current.value is not None:
                        print(current.value, end = ' ') 
                    current = current.next #prints each node value as it iterates through
                print()

class DoubleHashTable:
    def __init__(self,numBuckets):
        self.table = numBuckets * [None]
        self.numBuckets = numBuckets
    
    def hash1(self, key):
        if type(key) is str:  
            x = 0
            for character in key:
                x += ord(character) # add in value of next character
        else:
            x = key
        h1 = x % self.numBuckets #compression function to change integer to index
        return h1
    
    def hash2(self, key):
        if type(key) is str:  
            x = 0
            for character in key:
                x += ord(character) # add in value of next character
        else:
            x = key
        h2 = 5 - (x % 5) #compression function to change integer to index
        return h2

    def doubleHash(self, key): 
        for i in range(self.numBuckets):
            hashcode = (self.hash1(key) + i*self.hash2(key)) % self.numBuckets #double hash function
            if self.table[hashcode] is None: #if there is no value at the index of hashcode, it is returned to use
                return hashcode

    def add(self,key,value):
        h = self.hash1(key)
        if self.table[h] is None: #if table is empty with simple has index, inputs value
            self.table[h] = (key,value)
            return
        if self.table[h] is not None:
            h = self.doubleHash(key) #calls for double hasing if simple hasing does not provide an empty index
            self.table[h] = (key,value)
            return
    
    def delete(self,key):
        h = self.hash1(key)
        if self.table[h][0] == key: #if key at index given by simple hashing matches given key, sets it to None
            self.table[h] = None
            return
        for i in range(self.numBuckets):
            if self.table[i] is None: #goes back into the loop if table index is None
                continue
            if self.table[i][0] == key: #deletes table index where index key is equal to given key
                self.table[i] = None
                return
        print("Error: Key does not exist")

    def updateValue(self,key,value):
        h = self.hash1(key)
        if self.table[h][0] == key: #if key at index given by simple hashing matches given key, updates its values
            self.table[h] = (key,value)
            return
        for i in range(self.numBuckets):
            if self.table[i] is None:
                continue
            if self.table[i][0] == key: #updates values where keys match
                self.table[i] = (key,value)
                return
        print("Error: Key does not exist")
    
    def lookUp(self,key):
        h = self.hash1(key)
        if self.table[h] == key:
            return self.table[h].value
        for i in range(self.numBuckets):
            if self.table[i] is None:
                continue
            if self.table[i][0] == key: #returns value of index where keys match
                print("Value at Key " + str(key) + ": " + self.table[i][1])
                return
        print("Error: Key does not exist")
    
    def print(self):
        for i in range(self.numBuckets):
            if self.table[i] is None:
                print(None)
                continue
            print(self.table[i][1])
            
if __name__ == '__main__':
    
    ht = HashTable(10)
    print("---Hash Table w/ Chaining---")
    print("\n")
    ht.add(50, "Pranik")
    ht.add(22, 'Billy')
    ht.add(33, 'Andres')
    ht.add(63, 'Larry')
    ht.add(4, 'Bob')
    ht.add(55, 'Jones')
    ht.add(5, 'Alisha')
    ht.add(75, 'Brian')
    ht.add(65, 'Lisa')
    ht.add(85, 'Jacob')
    ht.add(95, 'Allison')
    ht.updateValue(22, 'Maya')
    ht.delete(95)
    ht.delete(75)
    ht.lookUp(4)
    ht.lookUp(900)
    print("\n")
    ht.print()

    dht = DoubleHashTable(7)
    print("\n")
    print("---Hash Table w/ Double Hash---")
    print("\n")
    dht.add(50, "Pranik")
    dht.add(29, "Juan")
    dht.add(36, "Brian")
    dht.add(4, "Prashant")
    dht.add(97, "Hammad")
    dht.add(34, "Alisha")
    dht.add(15, "Atharva")
    dht.updateValue(15, "Ace")
    dht.delete(34)
    dht.delete(50)
    dht.lookUp(15)
    dht.lookUp(897)
    print("\n")
    dht.print()
