# Data Structures  

## Lists
Mutable, ordered data type.
When using slicing the lower index is inclusive and the upper index is exclusive. 

```python
list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[1:2]
[3.4]
```

## Tuples 
Immutable, ordered data type.
To group elements that come together in order, latitude, longitude; dimensions, etc. Immutable ordered sequences of elements.

```python
location = (13.4125, 103.866667)
dimensions = 52, 40, 100
length, width, height = dimensions  # tuple unpacking
```

The parentheses are optional when defining tuples, frequently omited.

## Sets
Mutable, unordered data type.
To collect unique elements. Collections of unique elements. Unordered, it can’t be indexed nor sliced.

```python
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers) # define a set
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit) # False
fruit.pop() # removes a random element
fruit.add("watermelon") # it uses add instead of append
```

## Dictionaries:
Mutable, unordered data type.

**Mutable data type** that stores mappings of unique keys to values. ***Keys are of any immutable type***, like integers or tuples, not just strings. It's not even necessary for every key to have the same type. We can look up values or insert new values in the dictionary using square brackets that enclose the key. Values can be both mutable and immutable types.

***Mutable data type = { Immutable_key : mutable_or_immutable_value, key2 : value2, etc. }***
Unordered data structure. Keys are unique and immutable.

```python
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print("carbon" in elements) 		# True
n = elements.get("dilithium")		
print(n is None)					      # True
print(n is not None)			    	# False
```


## Compound Data Structures: (nested dictionaries)


```python
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
```
Adding new key:

```python
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
```

Adding new values:

```python
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
```

## Remarks:

For data structures, it is very useful to understand how you index, are they mutable, and are they ordered. Data structures will have different methods depending on these properties.  Why you would use one data structure vs. another is largely dependent on these properties.

## Summary:

| Data Structure | Ordered | Mutable | Constructor | Example |
| -------------- | ------- | ------- | ----------- | ------- |
| List | Yes | Yes | ```[ ] or list ()``` | [5.7, 4, 'yes', 5.7] |
| Tuple | Yes | No | ```() or tuple()``` | (5.7, 4, 'yes', 5.7) |
| Set | No | Yes | ```{1,2,3} or set()``` | {5.7, 4, 'yes'} |
| Dictionary | No | No** | ```{} or dict ()``` | {'Jun': 75, 'Jul':89}|

** a dictionary itself is mutable, but each of its individual yes must be immutable



---
*From Udacity Course*

<a href="https://github.com/ferzu/PythonNotes">Home</a>












￼



