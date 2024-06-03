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
# pop() can be used to achieve this
list = [1, 2, 3, 4, 5]
list.pop(2)
print(list)	# [1, 2, 4, 5]
```

