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

### Question 4

*Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., `10.4.5.11`.*

*Alyssa supplied Ben with a function named `is_an_ip_number`. It determines whether a string is a numeric string between `0` and `255` as required for IP numbers and asked Ben to use it. Here’s the code that Ben wrote:*

```python
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True
```

*Alyssia reviewed Ben’s code and said, “It’s a good start, but you missed a few things. You’re not returning a false condition, and you’re not handling the case when the input string has more or less than 4 components, e.g., `4.5.5` or `1.2.3.4.5`: both those values should be invalid.”*

*Help Ben fix his code.*

A simple `if` statement can be implemented to return `False` when the number of components is not exactly 4. Another issue is that if Alyssa’s function returns `False`, it simply breaks of the `if` block and returns `True`.

```python
def is_dot_separated_ip_address(input_string):

    dot_separated_words = input_string.split(".")
    
    # added 'if' statement
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            # return 'False'
            return False

    return True
```

