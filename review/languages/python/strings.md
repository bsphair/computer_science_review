# Python Strings

## Basics

* Create string with either " or '

```
computerBrand = 'Apple'

print(computerBrand[0])     # A

print(len(computerBrand))   # 5

```

* Strings are immutable (can't be changed after they're created)

```
computerBrand = 'Apple'

computerBrand[0] = 'B'    # error
```

## Methods

### Capitalize()

* Converts first character of a string to uppercase letter and lowercases all other characters
* Doesn't modify original string

```
string = 'hello, How are you doing?'

fixedString = string.capitalize()

print(fixedString)    # Hello, how are you doing?

```

---

### Count()

* Returns the number of occurences of a substring in the given string
* Optional parameters 'start' and 'end', specify the start/end positions in the string

```
string.count(substring, start=...,end...)
```

##### Parameters
Only requires a single parameter (substring)

* substring - string whose count is to be found
* start (optional) - starting index in string where the search starts
* end (optional) - ending index in string where search ends

```
string = "I have an Apple computer"
substring = "h"

print(string.count(substring))   # 1
print(string.count("a"))         # 2
print(string.count("a", 0, 5))   # 1
```
---

### Find()
* Returns index of first occurence of substring
* If not found, returns -1

Syntax
```
string.find(substring[, start[, end]])
```

Parameters
* substring - string to be searched
* start/end (optional)

```
string = 'Hello there. hello how are you doing?'

print(string.find('hello'))     # 13 
print(string.find('Hello'))     # 0 
```

## References
* https://www.programiz.com/python-programming/methods/string
