#include <iostream>
#include <string>
#include <any>

using namespace std;
// void add(int index, Object element)
// void addFirst(Object element)
// void addLast(Object element)
// bool addAll(int index, Collection collection)
// bool addAll(Collection collection)
// void clear()
// Object* clone()
// bool contains(object element)
// Object getIndex(int index)
// Object getFirst()
// Object getLast()
// int indexOf(Object element)
// Object[] iterator()
// Object poll(int index)
// Object pollFirst()
// Object pollLast()
// bool remove(int index)
// bool remove(Object element)
// int size()


class LinkedList{
    private:

    struct Node{
        string value;
        Node* next;
    };

    int _size = 0;
    Node root = Node();
    
    public:

    LinkedList(string startValue){
        root.value = startValue;
        root.next = NULL;

        _size = 1;
    }

    int size(){
        return(_size);
    }

    void add(int index, string element){
        if(index > this->size() || index < 0){
            throw "Index Error";
        }

        Node* pointer = &root;

        for(int i = 0; i < index-1; i++){
            *pointer = *pointer->next;
        }

        Node newNode = Node();

        newNode.value = element;
        newNode.next = pointer->next;

        pointer->next = &newNode;

        _size = this->size() + 1;  
    }

    void printAll(){
        Node pointer = root;

        while(pointer.next != NULL){
            cout << pointer.value << ", " << endl;
            pointer = *pointer.next;
        }

        // cout << pointer.value << endl;
    }

// void add(int index, Object element)
// void addFirst(Object element)
// void addLast(Object element)
// bool addAll(int index, Collection collection)
// bool addAll(Collection collection)
// void clear()
// Object* clone()
// bool contains(object element)
// Object getIndex(int index)
// Object getFirst()
// Object getLast()
// int indexOf(Object element)
// Object[] iterator()
// Object poll(int index)
// Object pollFirst()
// Object pollLast()
// bool remove(int index)
// bool remove(Object element)



};


int main(){
    LinkedList ll("Jorge");

    ll.add(1, "Marcos");
    ll.printAll();
    cout << ll.size() << endl;
    ll.add(1, "Joel");
    ll.printAll();
    cout << ll.size() << endl;
    ll.add(1, "Nildalys");
    ll.printAll();
    cout << ll.size() << endl;
}