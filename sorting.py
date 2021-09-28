import time
import random

def quickSort(a):

  length = len(a)
  if length < 2:
    return a
  if a[0] > a[length//2]:
    if a[0] < a[-1]:
        median = a[0]
    elif a[length//2] > a[-1]:
        median = a[length//2]
    else:
        median = a[-1]
  else:
    if a[0] > a[-1]:
        median = a[0]
    elif a[length//2] < a[-1]:
        median = a[length//2]
    else:
        median = a[-1]

  i, j = 0, len(a)-1
  while i < j:
    if a[i] < median:
      i += 1
      continue
    if a[j] > median:
      j -= 1
      continue
    a[i], a[j] = a[j], a[i]
  indx = a.index(median)
  s = 0
  while (s < length and a[indx] < a[s]):
    a[s], a[indx] = a[indx], a[s]
    s+=1

  left = quickSort(a[ : len(a)//2])
  right = quickSort(a[len(a)//2 : ])
  return left+right

def insertion_sort(a):
  
  length = len(a)
  if length == 0:
    return -1
  elif length == 1:
    return a
  else:
    for i in range(1, length):
      x = a[i]
      j = i-1
      while j >=0 and x < a[j] :
        a[j+1] = a[j]
        j -= 1
      a[j+1] = x
  return a

def max_heapify(a, i, n):

  max_idx = i 
  left_idx = 2*i + 1    
  right_idx = 2*i + 2     
  if left_idx < n and a[max_idx] < a[left_idx]:
    max_idx = left_idx
  if right_idx < n and a[max_idx] < a[right_idx]:
    max_idx = right_idx
  if max_idx != i:
    a[i],a[max_idx] = a[max_idx],a[i] 
    max_heapify(a, max_idx, n)

def build_MaxHeap(a, n):

  for i in range(n//2 - 1, -1, -1):
    max_heapify(a, i, n)

def heapSort(a):

  n = len(a)
  build_MaxHeap(a, n)
  for i in range(n-1, 0, -1):
    a[i], a[0] = a[0], a[i]   
    max_heapify(a, 0, i)

def selectionSort(a):

  n = len(a)
  for i in range(n):
    smallest = i
    for j in range(i+1, n):
      if a[smallest] > a[j]:
        smallest = j
    a[i], a[smallest] = a[smallest], a[i]

def main():
    currTime = time.asctime(time.localtime(time.time()))
    print("It is currently: ", currTime, "GMT")
    print("\nHow would you like to sort today?")

    run = 1
    while run != 0:

        print("\n-------Menu-------")
        print("1. Heap Sort")
        print("2. Insertion Sort")
        print("3. Quick Sort")
        print("4. Selection Sort")
        print("5. Exit")

        mainMenu = input()
        while not mainMenu.isdigit() or int(mainMenu) < 1 or int(mainMenu) > 5:
            print("Invalid Input... Please try again")
            mainMenu = input()

        if int(mainMenu) == 1: #heapsort

            redo = 1
            while redo != 0:

                n = input("\nPlease enter a positive integer: ")

                while True:
                    if not n.isdigit():
                        print("\nInvalid Input... Please enter an integer")
                        n = input()
                    elif int(n) <= 0:
                        print("\nInvalid Input... Please enter a positive integer")
                        n = input()
                    else:
                        break

                arr = []
          
                for i in range(int(n)):
                    arr.append(random.randint(-100, 100))
                print("\nYour array: ", arr)
                heapSort(arr)
                print("\nSorted:", arr)

                print("\n1. Redo")
                print("2. Menu")
                print("3. Exit")
                menuChoice2 = input()

                while not menuChoice2.isdigit() or int(menuChoice2) < 1 or int(menuChoice2) > 3:
                    print("Invalid Input... Please try again")
                    menuChoice2 = input()
                if int(menuChoice2) == 1:
                    redo = 1
                elif int(menuChoice2) == 2:
                  redo = 0 
                else:
                    print("\nThank you have a good day!")
                    redo = 0
                    run = 0

        if int(mainMenu) == 2: #insertionSort

          while redo != 0:
            arr = []
            for i in range(10):
              arr.append(random.randint(-100, 100))
            print("\nYour array: ", arr)
            insertion_sort(arr)
            print("\nSorted:", arr)

            print("\n1. Redo")
            print("2. Menu")
            print("3. Exit")

            menuChoice2 = input()
            while not menuChoice2.isdigit() or int(menuChoice2) < 1 or int(menuChoice2) > 3:
              print("Invalid Input... Please try again")
              
            if int(menuChoice2) == 1:
              redo = 1
            elif int(menuChoice2) == 2:
              redo = 0 
            else:
              print("\nThank you have a good day!")
              redo = 0
              run = 0
        
        if int(mainMenu) == 3: #quicksort

          while redo != 0:
            arr = []
            for i in range(10):
              arr.append(random.randint(-100, 100))
            print("\nYour array: ", arr)
            quickSort(arr)
            print("\nSorted:", arr)

            print("\n1. Redo")
            print("2. Menu")
            print("3. Exit")

            menuChoice2 = input()
            while not menuChoice2.isdigit() or int(menuChoice2) < 1 or int(menuChoice2) > 3:
              print("Invalid Input... Please try again")
              
            if int(menuChoice2) == 1:
              redo = 1
            elif int(menuChoice2) == 2:
              redo = 0 
            else:
              print("\nThank you have a good day!")
              redo = 0
              run = 0

        if int(mainMenu) == 4: #selectionSort

          while redo != 0:
            arr = []
            for i in range(10):
              arr.append(random.randint(-100, 100))
            print("\nYour array: ", arr)
            selectionSort(arr)
            print("\nSorted:", arr)

            print("\n1. Redo")
            print("2. Menu")
            print("3. Exit")

            menuChoice2 = input()
            while not menuChoice2.isdigit() or int(menuChoice2) < 1 or int(menuChoice2) > 3:
              print("Invalid Input... Please try again")
              
            if int(menuChoice2) == 1:
              redo = 1
            elif int(menuChoice2) == 2:
              redo = 0 
            else:
              print("\nThank you have a good day!")
              redo = 0
              run = 0

        if int(mainMenu) == 5:
            print("\nThank you have a good day!")
            run = 0 

main()

