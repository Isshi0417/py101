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