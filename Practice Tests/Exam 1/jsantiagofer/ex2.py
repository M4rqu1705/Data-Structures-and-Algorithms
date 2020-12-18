class list:
    def __init__(self, elements):
        self.elements = []


def replacer(ls, element, replacement):
    count = 0
    # ls.size can also be used
    for i in range(len(ls)):
        if ls[i] == element:
            count +=1
            ls[i] = replacement
    return count

def isPartition(arrayOfSets, target):
    tempUnion = Set(target.dataType)

    for i in range(len(arrayOfSets)):
        # condition #1
        if arrayOfSets[i].isEmpty():
            return False
        # condition #2 // first condition used to not get index out of bounds @ last [i] due to second condition
        for k in range(i+1, len(arrayOfSets)):
            # len and .currentSize can be interchangeable
                # if len(arrayOfSets[i].intersects(target)) != 0:
            if (arrayOfSets[i].intersects(target)).isEmpty() is False:
                return False

        tempUnion = tempUnion.union(arrayOfSets[i])
    
    # condition #3
    for i in range(len(tempUnion)):
        # if target.isMember(tempUnion[i]) is False:
        if tempUnion[i] not in target:
            return False

    return True





        
        

