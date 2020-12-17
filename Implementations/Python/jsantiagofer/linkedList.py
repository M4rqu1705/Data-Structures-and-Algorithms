class Node:
    def __init__(self, name, next):
        self.name = name
        self.next = next
    def has_next(self):
        return self.next != None

class sLinkedList:
    def __init__(self):
        self.size = 0
        self.header = Node(None, None)

    def printList(self):
        if (self.isEmpty()):
            return 0
        
        val = self.header.next
        while val is not None:
            
            if (val.next is None): 
                return  (val.name)
            else: 
                print(val.name)
                val = val.next

    def isEmpty(self):
        if (self.header.next == None):
            return True
        else:
            return False


    def append(self, name):
        self.size +=1
        end = self.header
        
        while end.next is not None:
            end = end.next

        end.next = Node(name, None)
        return
    
    def insert(self, i, name):
        if (i > self.size or i < 0):
            return None
        self.size +=1
        counter = 0
        end = self.header
        while i is not counter:
            end = end.next
            counter +=1
        
        temp = end.next
        end.next = Node(name, temp)
        return
    
    def remove(self, val):
        if self.isEmpty():
            return "Is Empty"
        
        end = self.header
        counter = 0
        while (end.next.name is not val) and (counter is not self.size-1):
            #can be done with next = null instead
            end = end.next
            counter +=1

        if (end.next.name is val):
            # del end.next
            self.size -=1
            end.next = end.next.next
            return

        else:
            return False
    
    def remove_pos(self, i):
        if (i >= self.size) or (i < 0):
            raise Exception("Position not available") 
        counter = 0
        end = self.header
        self.size -=1
        while (counter is not i):
            counter +=1
            end = end.next

        end.next = end.next.next

    def remove_all(self, name):
        if self.remove(name) is not False:
            self.remove(name)
        return

    def getSize(self):
        return self.size

    def clear(self):
        while (not self.isEmpty()):
            self.remove_pos(0)
    
    def isMember(self, name):
        end = self.header
        while end is not None:
            if end.name is name:
                return True
            end = end.next
        return False

    def first_index(self, name):
        counter = -1
        end = self.header
        while (end.name is not name) and (counter <= self.size):
            end = end.next
            counter +=1
        if (end.name is name):
            return counter
        else:
            return -1

    def last_index(self, name):
        if (self.first_index(name) == -1):
            return None

        end = self.header
        counter = -1

        while (counter is not self.size-1):
            end = end.next
            counter +=1

            if (end.name is name):
                last_ind = counter
        return last_ind

    def getAt(self, i):
        if (i < 0 or i >= self.size):
            return None

        counter = -1
        end = self.header
        while (counter is not i):
            counter +=1
            end = end.next
        return end.name

    def setAt(self, i, name):
        if (i < 0 or i >= self.size):
            return None

        counter = -1
        end = self.header
        while (counter is not i):
            counter +=1
            end = end.next
        end.name = name 
    
linkedL = sLinkedList()
linkedL.append("1")
linkedL.append(3)
linkedL.append(99)
linkedL.append(81)
linkedL.append(99)
linkedL.append(5)

linkedL.remove(5)
linkedL.remove_pos(2)
linkedL.remove_all(99)
linkedL.insert(6, 56)
print(linkedL.isMember("1"))
linkedL.clear()
linkedL.setAt(5, 8)
print("getAt : ", linkedL.getAt(5))
print("last index ", linkedL.last_index(99))
print("first index ", linkedL.first_index(99))

print(linkedL.printList())