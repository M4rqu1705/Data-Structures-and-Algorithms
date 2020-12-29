class ArrayList:
    def __init__(self, dataType):
        self.dataType = dataType
        self.data = []

    def remove_duplicates(self):
        new_array = ArrayList(int)
        for i in range(len(self.data)):
                # if self.data[i] not in new_array:
            if not new_array.isMember(self.data[i]):
                new_array.add(self.data[i])
        
        self.data = new_array.data
        del new_array

DEFAULT_SIZE = 10

class DynamicBag:
    def __init__(self, dataType):
        def __init__(self, dataType, size = DEFAULT_SIZE):
            self.dataType = dataType
            self.bag = [None] * size
            self.currentSize = 0
        
        def bag_analizer(self, bagB):
            new_list = ArrayList(int)
            for x in range(bagB.currentSize):
                count = self.bag.count_copies(bagB.bag[x])
                new_list.data.append(count)
            return new_list

                    

