# Practice Problems: Easy 2

### Question 1

Write two distinct ways of reversing the list without mutating the original list.

```python
numbers = [1, 2, 3, 4, 5]

# Slicing can be used to reverse a list
print(numbers[::-1])	# [5, 4, 3, 2, 1]

# reversed() can also be used
print(list(reversed(numbers)))	# [5, 4, 3, 2, 1]
```

### Question 2

Given a number and a list, determine whether the number is included in the list.

```python
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8 
number2 = 95

# 'in' operator can be used to check for an element
print(number1 in numbers)	# False
print(number2 in numbers)	# True
```

### Question 3

Programmatically  determine whether `42` lies between `10` and `100`, inclusive. Do the same for the values `100` and `101`.

```python
# 42
print(10 < 42 <= 100)	# True

# 100
print(10 < 100 <= 100)	# True

# 101
print(10 < 101 <= 100)	# False
```

### Question 4

Given a list of numbers `[1, 2, 3, 4, 5]`, mutate the list by removing the number at index `1`, so that the list becomes `[1, 2, 4, 5]`.

```python
list = [1, 2, 3, 4, 5]

# pop() can be used to achieve this
list.pop(2)
print(list)	# [1, 2, 4, 5]
```

### Question 5

How would you verify whether the data structures assigned to the variables `numbers` and `table` are of type `list`?

```python
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# type() and 'is' operator can be combined to check data type
print(type(numbers) is list)	# True
print(type(table) is list)		# False
```

### Question 6

Back in the stone age (before CSS), we used spaces to align things on the screen. If we have a 40-character wide table of Flintstone family members, how can we center the following title above the table with spaces?

```python
title = "Flintstone Family Members"
limit = 40

# The amount of spaces can be calculated by dividing by half
spaces = int((limit - len(title)) / 2)
print((" " * spaces) + title)
print("_" * 40)
#        Flintstone Family Members
# ________________________________________
```

### Question 7

Write a one-liner to count the number of lower-case `t` characters in each of the following strings:

```python
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

# count() can be used to count characters
print(statement1.count("t"))	# 2
print(statement2.count("t"))	# 0
```

### Question 8

Determine whether the following dictionary of people and their age contains an entry for ‘Spot’:

```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# 'in' operator can be used
print("Spot" in ages)	# False
```

### Question 9

We have most of the Munster family in our `ages` dictionary:

```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
```

Add entries for Marilyn and Spot to the dictionary:

```python
additional_ages = {'Marilyn': 22, 'Spot': 237}

# update() can be used add multiple items
ages.update(additional_ages)
print(ages)
# => {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10, 'Marilyn': 22, 'Spot': 237}
```

