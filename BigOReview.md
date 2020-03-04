## Links
* [BigO Cheatsheet](https://www.bigocheatsheet.com)

## O(1)

* Executes in the same time
* Execution time is independent of size of input

```javascript
const arr = [1, 2, 3];

console.log(arr[0]) // prints 1 in O(1) time
```

## O(n)

* Execution time is directly proportional to the input size <i>n</i>

```javascript
const arr = [1, 2, 3];

for (let index = 0; index < arr.length; index++) {
  console.log(arr[index]);
}
```

## O(log n)

* An algorithm has logarithmic time complexity if the time it takes to run the algorithm is proportional to the logarithm of the input size <i>n</i>
* Example:
  * Binary Search

## O(n<sup>2</sup>)

* An algorithm has quadratic time complexity if the time to execution it is proportional to the square of the input size
* Nested for loops
* Examples:
  * Bubble sort, Insert sort, Selection Sort
* Links
  * https://hackernoon.com/what-does-the-time-complexity-o-log-n-actually-mean-45f94bb5bfbf


