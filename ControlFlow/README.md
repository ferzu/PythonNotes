### Summary of useful control flow techniques: 

## CREATE LIST
```python
#names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
```


## MODIFY LIST 
```python
#usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)) :
    usernames[index] = usernames[index].lower().replace(" ", "_")
```


## BUILDING A COUNTER DICTIONARY 
```python
#book_title =  ['great', 'expectations','the', 'adventures', 'of',...]
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
```


## BUILDING A COUNTER DICTIONARY METHOD 2 (get)
```python
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
```
    

## ITERATING DICTIONARY
```python
for key in cast:
    print(key)
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
```


## CREATE LIST: List comprehension
```python
capitalized_cities = [city.title() for city in cities]  
# List comprehension
# idem:
# capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())
```

## Conditionals in list comprehensions:
```python
squares = [x**2 for x in range(9) if x % 2 == 0]
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
```

## ZIP
```python
# letters = ['a', 'b', 'c']
# nums = [1, 2, 3]
for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
```

## UNZIP
```python
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
```


## UNZIP 2
```python
points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
```

## Transpose
```python
data_transpose = tuple(zip(*data))
print(data_transpose)
```

## ENUMERATE
```python
# letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# using enumerate you have an index to access the iterables
# cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
# heights = [72, 68, 72, 66, 76]
for i, actor in enumerate(cast):
    cast[i] = actor + " " + str(heights[i])
```

---
*From Udacity course*

