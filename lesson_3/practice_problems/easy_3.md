# Practice Problems: Easy 3

### Question 1

Write two different ways to remove all of the elements from the following list:

```python
numbers = [1, 2, 3, 4]

# clear()
numbers.clear()
print(numbers)	# []

# pop()
while numbers:
    numbers.pop()
    
print(numbers)	# []
```

### Question 2

What will the following code output?

```python
print([1, 2, 3] + [4, 5])
```

The code will output `[1, 2, 3, 4, 5]` because lists can be concatenated in Python.

### Question 3

What will the following code output?

```python
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
```

The code will output `hello there`. This is because the value of `str1` is never modified and only `str2` goes through reassignment. 

### Question 4

What will the following code output?

```python
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
```

The code will output `[{'first': 42}, {'second': 'value2'}, 3, 4, 5]` because a shallow copy only duplicates the outermost instance. This means that while there are two lists, both of them point towards the same object instance. Any changed made to a shallow copy (where the data type is mutable) will also affect the original. To avoid this, deep copies can be made so the two lists reference different object instances.

### Question 5

The following function unnecessarily uses two `return` statements to return boolean values. Can you rewrite this function so it only has one `return` statement and does not explicitly use either `True` or `False`?

```python
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
# Simple '==' operators can replace if statement
def is_color_valid(color):
    return color == "blue" or color == "green"

print(is_color_valid("green"))	# True
print(is_color_valid("red"))	# False

# 'in' operators can also check for conditions
def is_color_valid(color):
    return color in ("blue", "green")

print(is_color_valid("blue"))	# True
print(is_color_valid("red"))	# False
```

