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