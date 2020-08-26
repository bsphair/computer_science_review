# General Data Structures

## Array
* Contiguously-allocated data structure
* Advantages:
  *  Constant-time access given the index
  *  Space efficiency 
  *  No space is wasted with links/formatting information
  *  Memory locality
  *  Physical continuity btw data helps exploit high-speed cache memory

### Dynamic Array
* Double each time size becomes too small
* The total work of managing the dynamic array is the same O(n) as it would have been if a single array of sufficient size had been allocated in advance
* Worst part of dynamic array
* Guarantee that each array access takes constant time is LOST in worst case due to resizing
* All queries will be fast except the few queries that trigger array size doubling
* In the end, the total effort will still be O(n)

Links
[http://www.fredosaurus.com/notes-cpp/newdelete/55dynexample.html
](http://www.fredosaurus.com/notes-cpp/newdelete/55dynexample.html
)

## Stack vs Heap
* Static Memory Allocation -> stack
* Dynamic Memory Allocation -> heap

### Stack
* Stores variables created by each function
* Variable allocated on the stack are stored directly into memory
* Fast access to this
* When a function or a method calls another function which in turn calls another function, the execution of all those functions remains suspended until the very last function returns its value

#### Stack in LIFO order
* Advantages:
  *  Memory is managed for you
  *  Don’t have to allocate memory by hand or free it

#### Summary
* Stack grows/shrinks as functions push/pop local variables
* No need to manage memory yourself, variables are allocated/freed automatically
* Stack has size limits
* Stack variables only exist while function that created them is running

### Heap
* Variables allocated can be accessed randomly at any time, no dependencies on each other
* Allocate/free at any time
* Memory is NOT managed for you
* To allocate memory, must use malloc() or calloc()
* Responsible for then freeing that memory

#### When to use the Heap
* If you need to allocate large block of memory (large array, big struct), and you need to keep that variable around a long time, allocate it on the heap
* If you need variables (arrays, structs) that can change dynamically, use the heap
* If you need smaller variables that only need to persists as long as the function using them is alive, use the stack

