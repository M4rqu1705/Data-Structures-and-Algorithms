class dArrayList:
    def __init__(self):
        self.data = []
        # self.size = 0'
        

    def printAll(self):
        if self.isEmpty():
            # raise Exception("List is Empty")
            return "List is Empty"
        
        for element in self.data:
            print(element)
        return
    def add(self, element):
        self.data.append(element)

    def insertAt(self, i, element):
        self.data.insert(i, element)

    def remove(self, element):
        self.data.remove(element)

    def removeAt(self, i):
        del self.data[i]

    def removeAll(self, element):
        # look for more efficient way
        while self.isMember(element):
            self.data.remove(element)

    def clear(self):
        self.data = []

    def isMember(self, element):
        for data in self.data:
            if data == element:
                return True
        
        return False 

    def size(self):
        return len(self.data)
    
    def first_index(self, element):
        if not self.isMember(element):
            return None
        return self.data.index(element)

    def last_index(self, element): 
        if not self.isMember(element):
            return None
        
        reversedList = self.data[::-1]
        return (reversedList.index(element) + len(newList)-1)
    
    def getAt(self, i):
        if i >= len(self.data) or i < 0:
            return None
        return self.data[i]
    
    def setAt(self, i, element):
        if i >= len(self.data) or i < 0:
            return None
        self.data[i] = element

    def isEmpty(self):
        return len(self.data) == 0

array = dArrayList()
array.add("Marcos")
array.add("Alejandro")
array.insertAt(1, "foo")
array.insertAt(1, "foo")
array.add("foo")
array.add([2, 3])

array.insertAt(0, "bar")
array.removeAt(4)

array.printAll()
# array.remove("foo")
# array.removeAt(0)
# # array.clear()
# print(array.isMember("Marcos"))
# print("first index: ", array.first_index("foo"), "last index: ", array.last_index("foo"))
# print("\nNew List")

# array.printAll()

# array.removeAll("foo")
# print(array.isMember("foo"))
print("size: ", array.size())
print("isMember: ", array.isMember([2,3]))
# # print("size: ", array.size())
# print("Is Empty? ", array.isEmpty())
# array.setAt(0, "jorge")
# print(array.getAt(0))