# Arrays

## Methods

### forEach()

* Executes a provided function once for each array element in an ascending order
* Doesn't mutate array on which it's called
* Callback is invoked with 3 arguments
* 1. element value
* 2. index value
* 3. Array object being traversed



```
var array1 = ['a', 'b', 'c'];

array1.forEach(x => console.log(x))
```

These are functionally equivalent:
```
for (var i = 0; i < arr.length; i++) {
console.log('Element', i, 'is', arr[i]);
}

arr.forEach(function(element, i) {
console.log('Element', i, 'is', element);
});
```

##### For loop vs forEach
* forEach only works on arrays


***

### for...of

* iterates through the values

```
var arr = ['Mike','Steven'];

for (var person of arr) {
    console.log(person);
}
```

Will print 
```'Mike'
'Steven'
```

***

### for...in

* iterates through the keys

```
var arr = ['Mike','Steven'];

for (var i in arr) {
    console.log(i);
}
```

Will print 
```
0
1
```

***
