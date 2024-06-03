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

