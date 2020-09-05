#include <iostream>
#include <vector>
#include <string>

using namespace std;
// size() -> int
// isEmpty() -> bool
// clear() -> void
// containsKey(key) -> bool
// containsValue(val) -> bool
// put(key, value) -> void
// get(key) -> value
// remove(key) -> value (removes element from hash map)

// putAll(hashMap) -> void (copies all from this to hashMap)

class HashMapStringToInt {
 private:
  int maxContainers;
  int currentSize;
  vector<vector<string> > keys;
  vector<vector<int> > values;

  int hashingFunction(string str) {
    int hash = 0;     // Hash serves as an accumulator

    // Iterate through every character in string
    for (int i = 0; i < str.size(); i++)
      hash += (int)str.at(i);

    // Hash will be within 0 and maxContainers - 1, perfect to use as an index for the containers
    return (hash % this->maxContainers);
  }

 public:
  HashMapStringToInt(int maxContainers = 10) {
    this->maxContainers = maxContainers;
    this->currentSize = 0;

    // The keys nor values have been initialized. For now they're just empty warehouses of containers. We have to fill the keys and values warehouses with containers
    for (int i = 0; i < this->maxContainers; i++) {
      this->keys.push_back(vector<string>());
      this->values.push_back(vector<int>());
    }
  }

  int size(){
    return this->currentSize;
  }

  bool isEmpty(){
    return this->size() == 0;
  }

  void clear(){
    this->currentSize = 0;

    // Delete EVERYTHING from keys and values
    this->keys.clear();
    this->values.clear();

    // Make the containers again just like in the constructor
    for (int i = 0; i < this->maxContainers; i++) {
      this->keys.push_back(vector<string>());
      this->values.push_back(vector<int>());
    }
  }

  bool containsKey(string key) {
    // Which container has the key?
    int containerIndex = hashingFunction(key);

    // Iterate through key container in order to find key
    for (int i = 0; i < this->keys.at(containerIndex).size(); i++)
      if (this->keys.at(containerIndex).at(i).compare(key) == 0)
        return true;

    return false;
  }

  bool containsValue(int value) {
    // Iterate through values warehouse
    for (int i = 0; i < this->values.size(); i++)
      // Iterate through values container
      for (int j = 0; j < this->values.at(i).size(); j++)
        if (value == this->values.at(i).at(j))
          return true;

    return false;
  }

  void put(string key, int value) {
    // Which container has the key?
    int containerIndex = hashingFunction(key);

    // Key is already inside this hash map. Therefore, change the existing key's value
    if (this->containsKey(key)) {
      // Iterate through key container in order to find key
      for (int i = 0; i < this->keys.at(containerIndex).size(); i++) {
        // If the key container has a key that matches the key parameter ...
        if (this->keys.at(containerIndex).at(i).compare(key) == 0) {
          // Change this key's value and break from for loop
          this->values[containerIndex][i] = value;
          break;
        }
      }

      // Key is not currently inside this hash map. It has to be added
    } else {
      // Append current key and values to the end of the correct container
      this->keys[containerIndex].push_back(key);
      this->values[containerIndex].push_back(value);
      this->currentSize++;
    }
  }

  int get(string key) {
    // Throw error if the key is not inside this hash map
    if (!this->containsKey(key)) {
      throw "Key not found";
    }

    // Which container has this key?
    int containerIndex = hashingFunction(key);

    // Iterate through key container in order to find key
    for (int i = 0; i < this->keys.at(containerIndex).size(); i++)
      // If the key container has a key that matches the key parameter ...
      if (this->keys.at(containerIndex).at(i).compare(key) == 0)
        // Return value at same container and at same position
        return this->values.at(containerIndex).at(i);

    throw "Key not found";  
  }

  int remove(string key){
    // Throw error if the key is not inside this hash map
    if (!this->containsKey(key)) {
      throw "Key not found";
    }

    // Which container has this key?
    int containerIndex = hashingFunction(key);

    // Iterate through key container in order to find key
    for (int i = 0; i < this->keys.at(containerIndex).size(); i++){
      // If the key container has a key that matches the key parameter ...
      if (this->keys.at(containerIndex).at(i).compare(key) == 0){
        // Remove from keys and value warehouses
        this->keys[containerIndex].erase(this->keys[containerIndex].begin() + i);

        const int temp = this->values.at(containerIndex).at(i);

        this->values[containerIndex].erase(this->values[containerIndex].begin() + i);

        this->currentSize--;

        return temp;
        
      }
    }

    throw "Key not found";    
  }

};


int main() {
  auto hm = HashMapStringToInt(4);

  hm.put("dog", 1);
  hm.put("cat", 2);
  hm.put("bird", 3);
  hm.put("serpent", 4);
  hm.put("horse", 5);
  hm.put("dolphin", 6);
  hm.put("human", 7);

  cout << hm.get("cat") << endl;
  cout << hm.get("serpent") << endl;
  cout << hm.get("dog") << endl;
  cout << hm.get("human") << endl;
  cout << hm.get("horse") << endl;
  cout << hm.get("bird") << endl;
  cout << hm.get("dolphin") << endl;

  cout << "Contains cat: " << hm.containsKey("cat") << endl;
  cout << "Size: " << hm.size() << endl;
  hm.remove("cat");
  cout << "Contains cat: " << hm.containsKey("cat") << endl;
  cout << "Size: " << hm.size() << endl;

  hm.clear();
  cout << "Size: " << hm.size() << endl;

  return 0;
}