// add(), erase(), erase_all(), count(), clear(), is_member(), size(), is_empty(), iterate_over_all_values
#include <vector>
#include <iostream>
using namespace std;

class dynamicBag {
    private:
        vector<int> v;
    public:
    
    // Constructor
    dynamicBag(){
        cout << "Already constructed!" << endl;
    }

    // add()
    void add(int k) {
        this->v.push_back(k);
    }

    // erase()
    bool erase(int k){
        for (int i = 0; i< this->size(); i++) {
            if (this->v[i] == k) {
                this->v.erase(this->v.begin() + i);
                return true;
            }
        }
        return false;
    }

    // erase_all()
    int erase_all(int k) {
        int i;
        for (i = 0; this->erase(k) ; i++) {
        }
        return i;
    }

    // count()

    int count(int k){
        int counter = 0;
        for (int i = 0; i < this->size(); i++) {
            if (this->v.at(i) == k) {counter+=1;}
        }

        return counter;
    }   

    // clear
    void clear() {
        this->v.clear();
    }

    // is_member
    bool is_member(int k) {
        return (this->count(k) > 0);
    }

    // size()
    int size(){
        return (this->v.size());
    }
    
    // is_empty
    bool is_empty(){
        return (this->size() == 0);
    }
    
};


int main() {
    dynamicBag bag = dynamicBag();
    bag.add(3);
    bag.add(4);
    bag.add(3);
    bag.add(3);

    cout << "Count is: " << bag.count(3) << endl;
    bag.erase_all(3);
    cout << bag.count(3) << endl;
    cout << bag.size() << endl;
    return 0;
}