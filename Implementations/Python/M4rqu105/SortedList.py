from SinglyLinkedList import SinglyLinkedList

class SortedList:

    def __init__(self, param = None):
        if param is None:
            self.linked_list = SinglyLinkedList()
        else:
            self.linked_list = SinglyLinkedList(param)

    def add(self, element):

        for i, value in enumerate(self.linked_list):
            if value >= element:
                self.linked_list.insert(i, element)
                return True

        self.linked_list.append(element)

        return True

    def remove(self, element):
        return self.linked_list.remove(element)

    def delete(self, position):
        return self.linked_list.delete(position)

    def get(self, position):
        return self.linked_list.get(position)

    def index(self, element):
        return self.linked_list.index(element)

    def last_index(self, element):
        return self.linked_list.last_index(element)

    def contains(self, element):
        return self.linked_list.contains(element)

    def size(self):
        return self.linked_list.size()

    def isEmpty(self):
        return self.linked_list.isEmpty()

    def clear(self):
        self.linked_list.clear()

    def __str__(self):
        return str(self.linked_list)

    def __repr__(self):
        return repr(self.linked_list)


if __name__ == "__main__":

    ll1 = SortedList()

    import random

    for i in range(random.randint(10, 20)):
        ll1.add(random.randint(-1, 1))

    breakpoint()




