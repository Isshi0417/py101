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