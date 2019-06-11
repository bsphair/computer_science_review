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

### Capitalize

* Converts first character of a string to uppercase letter and lowercases all other characters
* Doesn't modify original string

```
string = 'hello, How are you doing?'

fixedString = string.capitalize()

print(fixedString)    # Hello, how are you doing?

```


### Count

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





