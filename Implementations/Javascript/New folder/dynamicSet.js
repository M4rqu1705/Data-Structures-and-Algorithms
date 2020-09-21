// set: dynamic - cant repeat
/*
bool add(value)
bool remove(value)
void clear()
bool contains(value)
int getSize()
bool empty()
bool isSubset(set2)
set union(set2)
set intersection(set2)
set difference(set2)
*/

class Set {
  constructor() {
    this.values = [];
  }

  printAll() {
    console.log("[");
    for (let i = 0; i < this.getSize(); i++) {
      console.log(this.values[i]);
    }
    console.log("]");
  }

  add(value) {
    if (!this.values.includes(value)) {
      this.values.push(value)
    }
    else {
      return false;
    }
  }

  remove(value) {
    for (let i = 0; i < this.getSize(); i++) {
      if (this.values[i] === value) {
        this.values = this.values.filter(function(v){
          return v !== value; 
        } );
        return true;
        // values.splice(start 0, index value)
      }
    }
    return false;
  }

  clear() {
    this.values = [];
  }

  contains(value) {
    return this.values.includes(value);
  }

  getSize() {
    return this.values.length;
  }

  isEmpty() {
    return 0 === this.getSize();
  }

  isSubset(s2) {
    for (let val1 of this.values) {
      if (!s2.contains(val1)) {
        return false;
      }
    }
    return true;
  }
  
  union(s2) {
    let new_set = new Set();
    for (let val1 of this.values){
      if (!new_set.contains(val1)){
        new_set.add(val1);
      }
    }
    for (let val2 of s2.values){
      if (!new_set.contains(val2)){
        new_set.add(val2);
      }
    }
    return new_set;
  }

  intersection(s2) {
    // all common values into new set
    let new_set = new Set();
    for (let val1 of this.values) {
      if (s2.contains(val1)) {
        new_set.add(val1);
      }
    }
    return new_set;
  }

  // delete all common values
  difference(s2) {
    let new_set = new Set();
    for (let val1 of this.values) {
      if (!s2.contains(val1)){
        new_set.add(val1);
      }
    }
    return new_set;
  }
    
  
  
}

let test = new Set();


test.add("Marcos");
test.printAll()
test.add("Marcos");
test.printAll()
test.add("Sofía");
test.add("Paco");
test.printAll();
test.remove("Marcos");
test.printAll();

let subs_test = new Set();
subs_test.add("Paco");
subs_test.add("Sofía")


let t2 = new Set();
t2.add("aaaa");
t2.add("Marcos");
t2.add("Jorge");
t2.add("Sofía")

console.log("START:")
test.printAll();
t2.printAll();

let t3 = test.union(t2)
console.log("Union:");
t3.printAll();

console.log("clear t3:");
t3.clear();
t3.printAll();

console.log("contains:");
console.log(t2.contains("Jorge"));
console.log(t2.contains("no"));


console.log("Get size: ");
console.log(t2.getSize());
t2.printAll()

console.log("is empty");
console.log(t3.isEmpty());
t3.printAll();
console.log(t2.isEmpty());
t2.printAll();

console.log("is subset")
console.log(subs_test.isSubset(test));

t4 = test.intersection(t2)
console.log("intersection:");
t4.printAll();
test.printAll();
t2.printAll();

t5 = test.difference(t2)
console.log("difference")
test.printAll();
t2.printAll();
t5.printAll();




/*
bool add(value)
bool remove(value)
void clear()
bool contains(value)
int getSize()
bool empty()
bool isSubset(set2)
set union(set2)
set intersection(set2)
set difference(set2)
*/