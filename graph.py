import time

class Node:

  def __init__(self, name):
    self.name = name
    self.dist = 0
    self.parent = None
    self.adjacency = []
    self.color = 'GRAY' 
  
  def getName(self, n):
    return n.name
  
  def add(self, n):
    self.adjacency.append(n)
  
def bfs(n):
  n.parent = n
  n.dist = 0
  queue = [n]
  while len(queue) > 0:
    x = queue.pop()
    for node in x.adjacency:
      if node.parent is None:
        node.parent = x
        node.dist = (x.dist + 1)
        queue.append(node)

def Explore(nodes):
  for node in nodes:
    if node.color == "GRAY":
      node.color = "BLUE"
      if Is_bipartite(node) == False:
        print("NOT bipartite")
        break 
      else:
        continue
        
def Is_bipartite(n):
  n.parent = n
  n.dist = 0
  queue = [n]
  while len(queue) > 0:
    u = queue.pop() 
    for node in u.adjacency:
      if node.color == 'GRAY':
        if u.color == 'BLUE':
          node.color = 'RED'
        elif u.color == 'RED':
          node.color = 'BLUE'
        node.parent = n
        node.dist = (n.dist + 1)
        queue.append(node)
      elif node.color == u.color:
          return False
  return True

def main():

    print('\n----------Graph----------\n')

    v1 = Node('a')
    v2 = Node('b')
    v3 = Node('c')
    v4 = Node('d')
    v5 = Node('e')
    v6 = Node('f')
    v7 = Node('g')
    v8 = Node('h')
    nodes = [v1, v2, v3, v4, v5, v6, v7, v8]
    v1.add(v3)
    v1.add(v4)
    v2.add(v3)
    v2.add(v5)
    v3.add(v2)
    v3.add(v1)
    v3.add(v4)
    v4.add(v3)
    v4.add(v1)
    v4.add(v5)
    v4.add(v6)
    v5.add(v4)
    v5.add(v2)
    v5.add(v6)
    v6.add(v4)
    v6.add(v5)
    v6.add(v8)
    v8.add(v6)
      
    print('Adjacency\n')
    
    for i in nodes:
      print(i.name, '->', end = ' ')
      if len(i.adjacency) == 0:
        print()
        continue
      for j in i.adjacency:
        if j == i.adjacency[-1]:
          print(j.name)
        else:
          print(j.name, end = ' ')

    flag = -1
    while True:
      print('\nvertices:', end = ' ')
      for n in nodes:
        print(n.name, end = ' ')
      vertex = input('\nSelect a vertex to navigate to: ')
      for x in nodes:
        if x.name == vertex:
          bfs(x)
          flag = 1
      if flag > 0:
        break
      print("\nThat vertex is not in the graph, please try again...")

    temp = Node
    for z in nodes:
      temp = z
      print('\n', z.name, 'path:', temp.name, end = ' ')
      while temp.parent != temp and temp.parent is not None:
        print('->', temp.parent.name, end = ' ')
        temp = temp.parent
      print('\n distance:', z.dist)

    print('\n----------Bipartite Graph?----------\n')
    w1 = Node('a')
    w2 = Node('b')
    w3 = Node('c')
    w4 = Node('d')
    w5 = Node('e')
    w6 = Node('f')
    w7 = Node('g')
    w8 = Node('h')
    w9 = Node('i')
    w1.add(w4)
    w2.add(w4)
    w2.add(w6)
    w3.add(w4)
    w3.add(w5)
    w4.add(w1)
    w4.add(w2)
    w4.add(w3)
    w5.add(w3)
    w6.add(w2)
    w7.add(w8)
    w7.add(w9)
    w8.add(w7)
    w8.add(w9)
    w9.add(w7)
    w9.add(w8)

    clrNodes = [w1, w2, w3, w4, w5, w6, w7, w8, w9]
    Explore(clrNodes)
    for node in clrNodes:
      print(node.name, ":", node.color)

main()