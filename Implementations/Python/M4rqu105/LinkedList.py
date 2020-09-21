import copy
import random

class Node:
  value=None
  next=None

class LinkedList:
  def __init__(self, value):
    self.root = Node()
    self.root.value = value
    self.root.next = None
    self.size = 1

  
  def add(self, index, value):
    if index > self.size or index < 0:
      raise "Error"

    pointer = self.root

    for i in range(0, index-1):
      pointer = pointer.next

    newNode = Node()
    newNode.value = value
    newNode.next = pointer.next
    pointer.next = newNode

    self.size += 1

  def addLast(self, value):
    self.add(self.size, value)

  def addFirst(self, value):
    self.add(0, value)

  def clear(self):
    self.root.value = None
    self.root.next = None

    self.size = 0
  
  def contains(self, value):
    pointer = self.root

    while pointer.next is not None:
      if pointer.value == value:
        return True
      
    return False

  def getIndex(self, value):
    pointer = self.root
    i = 0

    while pointer.next is not None:
      if pointer.value == value:
        return i
      i+=1
      
    return -1

  def getFirst(self):
    return self.root.value

  def getLast(self):
    pointer = self.root

    while pointer.next is not None:
      pass
      
    return pointer.value

  def poll(self, index):
    if index == 0:
      temp = self.root.value
      self.root = self.root.next
      self.size -= 1

      return temp

    pointer = self.root

    for i in range(index-1):
      pointer = pointer.next

    temp = pointer.next.value
    pointer.next = pointer.next.next

    self.size -= 1

    return temp

  def pollFirst(self):
    self.poll(0)

  def pollLast(self):
    self.poll(self.size-1)

  def removeIndex(self, index):
    pointer = self.root

    for i in range(index-1):
      pointer = pointer.next

    pointer.next = pointer.next.next

    self.size -= 1

    return True

  def remove(self, value):
    pointer = self.root
    i = 0

    while pointer.value != value and pointer.next is not None:
      pointer = pointer.next
      i += 1
    
    if pointer.value != value:
      return False

    return self.removeIndex(i)
    

  def clone(self):
    return copy.copy(self.root)


  def printAll(self):
    pointer = self.root

    while pointer.next is not None:
      print(pointer.value, end=', ')
      pointer = pointer.next
    
    print(pointer.value)

if __name__ == "__main__":
  ll = LinkedList("Jorge")
  ll.add(1, 'Marcos')
  ll.printAll()
  ll.add(1, 'Joel')
  ll.printAll()
  ll.add(1, 'Nildalys')
  ll.printAll()

  ll.remove("Marcos")
  ll.printAll()

  ll.add(1, "Jorge Padre")
  ll.printAll()

  ll.removeIndex(random.randint(0, ll.size-1))

  ll.printAll()

  ll.pollLast()
  ll.printAll()

  ll.pollFirst()
  ll.printAll()
