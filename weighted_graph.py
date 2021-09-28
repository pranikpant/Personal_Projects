class Node:

  def __init__(self, name):
    self.name = name
    self.adjacency = []
    self.parent = None
    self.dist = 0
  
  def add(self, n, w):
    self.adjacency.append([n,w])

def getMin(n):
  minVal = float('inf')
  minIdx = 0
  for i in range(len(n)):
    if n[i].dist < minVal and n[i].parent is None:
      minVal = n[i].dist
      minIdx = i
  return minIdx

def dijkstra(s, v):
  for i in v:
    i.dist = float('inf')
  s.dist = 0
  s.parent = None
  queue = [s]
  while queue:
    s = queue.pop(getMin(queue))
    for node in s.adjacency:
      new = s.dist + node[1]
      if node[0].parent is None:
        queue.append(node[0])
      if new < node[0].dist:
        node[0].dist = new
        node[0].parent = s

def shortestToFrom(start, end, v):
  dijkstra(start, v)
  print("\n---Trip from", start.name, "to", end.name, "---")
  print("\nTotal cost: $", end.dist)
  print("\nCities visited:", end = ' ')
  while end.parent is not None and end.name != start.name:
    print(end.name, end = ', ')
    end = end.parent
  print(end.name)
  

def main():

  a = Node("Long Beach")
  b = Node("Las Vegas")
  c = Node("San Francisco")
  d = Node("Pheonix")
  e = Node("Portland")
  f = Node("Salt Lake City")
  g = Node("Aspen")
  h = Node("Glacier N Park")
  a.add(b, 50)
  a.add(c, 250)
  a.add(d, 170)
  a.add(g, 800)
  b.add(f, 190)
  b.add(g, 400)
  c.add(f, 150)
  c.add(e, 250)
  d.add(g, 650)
  e.add(h, 270)
  f.add(h, 250)
  f.add(g, 210)
  g.add(h, 350)
  nodeMap = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h}
  cities = [a,b,c,d,e,f,g,h]
  
  print('-----Cities-----\n')
  for node in nodeMap:
    print(node, ':', nodeMap[node].name)

  valid = False
  while not valid:
      start = input("\nSelect your starting location (a-h): ")
      end = input("Select your destination (a-h): ")
      if start not in nodeMap or end not in nodeMap:
        print('You entered 1 or more invalid locations... please try again')
      else:
        start = nodeMap[start]
        end = nodeMap[end]
        valid = True

  shortestToFrom(start,end,cities)

main()