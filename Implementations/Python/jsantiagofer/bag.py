DEFAULT_SIZE = 10

class dBag:
    def __init__(self, dataType, size = DEFAULT_SIZE):
        self.currentSize = 0
        self.bag = [None] * size
        self.dataType = dataType

    def printValues(self):
        print("\nValues:")
        for i in range(len(self.bag)):
            print(self.bag[i])

    def validate(self, element):
        # Marcos' better
        if isinstance(element, self.dataType):
            return True
        else:
            try:
                element = dataType(element)
                return True
            except:
                return False

    def expand(self):
        tempBag = dBag(self.dataType, self.capacity()*2)

        for element in self.bag:
            tempBag.add(element)
        
        self.bag = tempBag.bag
        del tempBag

    def contract(self):
        tempBag = dBag(self.dataType, self.capacity()//2)

        for element in self.bag:
            tempBag.add(element)
        
        self.bag = tempBag.bag
        del tempBag


    def capacity(self):
        return len(self.bag)

    def add(self, element):
        if self.validate(element) is False:
            return False

        if not isinstance(element, self.dataType):
            element = self.dataType(element)

        if self.currentSize > len(self.bag)/2:
            self.expand()
        
        pos = hash(element) % self.capacity()

        if self.bag[pos] is None:
            self.bag[pos] = element
            self.currentSize +=1 
            return True
        else:
            if self.bag[pos+1] is None:
                self.bag[pos+1] = element
                self.currentSize +=1
                return True
            else:
                for i in range(self.capacity()):
                    if self.bag[i] is None:
                        self.bag[i] = element
                        self.currentSize +=1
                        return True
            
        return -1

    def remove(self, element):
        if self.validate(element) is False:
            return False

        if isinstance(element, self.dataType) is False:
            element = self.dataType(element)
            
        pos = self.isMember(element)

        if pos == -1:
            return False
        else:
            self.bag[pos] = None
            self.currentSize -=1
            return True

        if self.currentSize <= self.capacity() // 4:
            self.contract()

        return False
    
    def remove_all(self, element):
        if self.validate(element) is False:
            return False

        if isinstance(element, self.dataType) is False:
            element = self.dataType(element)

        while self.isMember(element) != -1:
            pos = self.isMember(element)
            self.bag[pos] = None
            self.currentSize -=1
        
        if self.currentSize <= self.capacity() // 4:
            self.contract()

        return True


    def isMember(self, element):
        if self.validate(element) is False:
            return False

        if isinstance(element, self.dataType) is False:
            element = self.dataType(element)

        pos = hash(element) % self.capacity()
        
        if self.bag[pos] == element:
            return pos
        elif self.bag[pos+1] == element:
            return pos+1
        else:
            for p in range(self.capacity()):
                if self.bag[p] == element:
                    return p
        return -1
    
    def clear(self):
        tempBag = dBag(self.dataType, self.capacity())
        self.bag = tempBag.bag

    def count_copies(self, element):
        counter = 0
        for i in range(self.capacity()):
            if self.bag[i] == element:
                counter +=1

        return counter

    def isEmpty(self):
        return self.bag == [None] * self.capacity()


        
bag = dBag(int, 4)

print("capacity: ", bag.capacity())
print("currentSize: ", bag.currentSize)
bag.add(2)
bag.add(2)
bag.add(2)
bag.add(2)

bag.add("A")
print(bag.isMember(2))
print(bag.count_copies(2))

print("capacity: ", bag.capacity())
print("currentSize: ", bag.currentSize)
bag.remove_all(2)
bag.printValues()
# bag.clear()
print(bag.isEmpty())





