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

### Question 4

*What will the following two lines of code output?*

```python
print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)
```

The first line prints `0.8999` because floating point representations lack minuscule amounts of precision. This means that the calculated value is not truly equal to `0.9`, which is why the second line prints `False`. 

### Question 5

*What do you think the following code will output?*

```python
nan_value = float("nan")

print(nan_value == float("nan"))
```

The code will output `False` because `nan` refers to data type that is not a number. In Python, `==` operator can’t be used to check if a value is `nan`.

***Bonus Question***

*How can you reliably test if a value is `nan`*?

You can use `math.isnan()` to check for these values.

```python
import math

nan_value = float("nan")
print(math.isnan(nan_value))	# True
```

### Question 6

*What is the output of the following code?*

```python
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)
```

The code will output `34`. This is because the value returned by the function is assigned to `new_answer` but `print` uses `answer`, which was used as the initial argument.

### Question 7

*One day, Spot was playing with the Munster family’s home computer, and he wrote a small program to mess with their demographic data:*

```python
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
```

*After writing this function, he typed the following code:*

```python
mess_with_demographics(munsters)
```

*Before Grandpa could stop him,  Spot hit the enter key with his tail. Did the family’s data get ransacked? Why or why not?*

The family data is ruined because dictionaries are mutable in Python, and the original data is lost because the changes were not reassigned to a new variable. It instead modifies the original object instance of the `munsters` data.

### Question 8

*Function and method calls can take expressions as arguments. Suppose we define a function named `rps` as follows, which follows the classic rules of the rock-paper-scissors game, but with a slight twist: in the event of a tie, it just returns the choice made by both players.*

```python
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
```

*What does the following code output?*

```python
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
```

The code prints out `paper`. This is because the first two invocations (nested in the deepest call) returns `paper` and `rock` respectively. The second invocation compares these two, which returns `paper`. Finally, the last invocation compares `paper` with `rock`, which — again — returns `paper`.

### Question 9

*Consider these two simple functions:*

```python
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"
```

*What will the following function invocation return?*

```python
bar(foo())
```

The invocation will return `no`. `foo()` initially returns `yes`, which is passed as the argument in `bar()`. The `==` operator returns `False` after evaluating the statement. It skips over `foo` because it is part of the evaluation that involves the `==` operator. Since `no` is a truthy, the `or` operator will return `no` when compared with `param == “no”`.

### Question 10

*In Python, every object has a unique identifier that can be accessed using the `id()` function. This function returns the identity of an object which is guaranteed to be unique for the object’s lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as “interning”.*

*Given the following code, predict the output:*

```python
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
```

The code will return true. In this case, Python uses the same memory as `a` and `b` because `42` is an integer (which is immutable), and it shares the same value.
