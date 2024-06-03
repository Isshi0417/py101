# Practice Problems: Medium 1

### Question 1

*Let’s do some “ASCII Art”: a stone-age form of nerd artwork from back in the days before computers had video screens.*

*For this practice problem, write a program that outputs `The Flintstones Rock!` 10 times, with each specific line prefixed by one more hyphen than the line above it. The output should start out like this:*

```python
-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
```

A combination of for loop and concatenation does this trick:

```python
message = "The Flintstones Rock!"

for row in range(1, 11):
    print("-" * row + message)
```

### Question 2

*Alan wrote the following function, which was intended to return all of the factors of `number`:*

```python
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
```

*Alyssa noticed that this code will fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we’re not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.*

Alan can simply change the operator in the while loop to make sure the parameter is not a negative number:

```python
while divisor > 0:
```

By doing this, the function doesn’t trigger the while loop and returns the `result`.

***Bonus Question**: What is the purpose of `number % divisor == 0` in that code?*

The expression checks if the `number` can be divided without remainders by the `divisor`. If there are no remainders, that means the `divisor` is a factor.

### Question 3

*Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.*

*She wrote two implementations of the code for adding elements to the buffer:*

```python
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
```

*Is there a difference between these implementations, other than the way she is adding an element to the buffer?*

Yes because the first function mutates `buffer` while the second one creates a new list and assigns it to `buffer`, which is the value getting returned at the end of the function.
