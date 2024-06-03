# Practice Problems: Hard 1

### Question 1

*Will the following functions return the same results?*

```python
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())
```

`first()` will output the actual content (the dictionary), but `second()` will print out nothing. This is because `first` encloses the value to be returned in braces. However, `second()` puts the braces under, which means anything under the `return` statement is not reached.

### Question 2

*What does the last line in the following code output?*

```python
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
```

The last line will output `‘first’ : [1, 2]`. This is because dictionaries are mutable. In this case, a value of `2` is added to the dictionary underneath the `first` key.

### Question 3

*Given the following similar sets of code, what will each code snippet print?*

***A)***

```python
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

The code snippet doesn’t mutate the arguments because the values are simply being reassigned to a variable that is only accessible within the function. Expected output:

```python
one is: ['one']
two is: ['two']
three is: ['three']
```

***B)***

```python
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

The code snippet doesn’t mutate the arguments because the new values are assigned to a newly created local variable within the function. Expected output:

```python
one is: ['one']
two is: ['two']
three is: ['three']
```

***C)***

```python
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

The code snippet mutates the parameters. This is because there are no new variables that are declared and assigned within the function. Instead, it accesses the arguments’ first index and mutates it into the appropriate values. Expected output:

```python
one is: ['two']
two is: ['three']
three is: ['one']
```

