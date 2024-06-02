# Small Problems: Easy 1

### Isn't it Odd?

Write a function that takes one integer argument and returns `True` when the number's absolute value is odd, False otherwise.

```python
def is_odd(n):
    return n % 2 == 1
    
print(is_odd(7))    # True
print(is_odd(10))   # False
print(is_odd(5))    # True
```

### Odd Numbers

Print all odd numbers from `1` to `99`, inclusive, with each number on a separate line.

```python
# for each number between 1 and 99
for i in range(1, 100):
    # if remainder is 1
    if i % 2 == 1:
        print(i)
```

Can you solve the problem by iterating over just the odd numbers?

```python
# for each number after 1 added by 2
for i in range(1, 100, 2):
    print(i)
```

### Even Numbers

Print all even numbers from `1` to `99`, inclusive, with each number on a separate line.

```python
# for each number between 1 and 99
for i in range(1, 100):
    # if remainder is 0
    if i % 2 == 0:
        print(i)
```

Can you solve the problem over just the even numbers?

```python
# for each number after 2 added by 2
for i in range(2, 100, 2):
    print(i)
```

### How big is the room?

Build a program that asks the user to enter the length and width of a  room, in meters, then prints the room's area in both square meters and  square feet.

*Note*: 1 square meter == 10.7639 square feet

```python
# ask for user input
l = float(input('Enter the length of the room in meters: '))
w = float(input('Enter the width of the room in meters: '))

# calculate area
area = l * w

# print result
print(f'Area of the room (meters): {area} square meters.')
print(f'Area of the room (sq. ft): {area * 10.7639} square feet.')
```

### Tip Calculator

Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

```python
# ask for input
bill = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

# calculate tip
tip = bill * (tip_percentage / 100)
total = bill + tip

# print results
print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')
```

### Sum or Product of Consecutive Integers

Write a program that asks the user to enter an integer greater than `0`, then asks whether the user wants to determine the sum or the product of all numbers between `1` and the entered integer, inclusive.

```python
# initialize variables
n = int(input('Please enter an integer greater than 0: '))
op = input('Enter "s" to compute the sum, or "p" to compute the product. ')

# if addition
if op == 's':
    sum = 0
    # for each number from 1 through n
    for i in range(1, n + 1):
        # add to total
        sum += i
    print(f'\nThe sum of the integers between 1 and {n} is {sum}.')
else:
    product = 1
    # for each number from 1 through n
    for i in range(1, n + 1):
        # multiply to total
        product *= i
    print(f'\nThe product of the integers between 1 and {n} is {product}.')
```

### Short Long Short

Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

```python
def short_long_short(s1, s2):
    # if length of s1 is shorter than s2
    if len(s1) < len(s2):
        return s1 + s2 + s1
    else:
        return s2 + s1 + s2
```

### Leap Years (Part 1)

Write a function that takes any year greater than `0` as input and returns `True` if the year is a leap year, or `False` if it is not.

For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

- If the year is divisible by 400, it **is** a leap year.
- If the year is divisible by 100 but not by 400, it **is not** a leap year.
- If the year is divisible by 4 but not by 100, it **is** a leap year.
- All other years **are not** leap years.

```python
def is_leap_year(year):
    # if year is divisible by 400
    if year % 400 == 0:
        return True
    # if year is divisible by 4
    elif year % 4 == 0:
        # if year is not divisible by 100
        if year % 100 != 0:
            return True
        else:
            return False
    else: 
        return False
```

### Leap Years (Part 2)

In the previous exercise, we assumed that the Gregorian calendar has been in continuous use since the year 1. However, the Gregorian calendar wasn't adopted until much later; prior to that, much of the world used the Julian calendar, which observed leap year every 4 years. 

In 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. Update the function from the previous exercise so it uses the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

```python
def is_leap_year(year):
    # Gregorian calendar
    if year > 1752:
        if year % 400 == 0:
            return True
        elif year % 4 == 0:
            if year % 100 != 0:
                return True
            else:
                return False
        else: 
            return False
    # Julian calendar
    else:
        if year % 4 == 0:
            return True
        else:
            return False
```

### Multiples of 3 and 5

Write a function that computes the sum of all numbers between `1` and some other number, inclusive, that are multiples of `3` or `5`. For instance, if the supplied number is `20`, the result should be `98`(`3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20`).

You may assume that the number passed in is an integer greater than `1`.

```python
def multisum(n):
    sum = 0
    # for each number from 0 through n
    for i in range(n + 1):
        # if divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # add to sum
            sum += i
    return sum
```

### UTF-16 String Value

Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use `ord` to determine the UTF-16 value of a character.)

```python
def utf16_value(s):
    value = 0
    # for each character in string
    for c in s:
        # add value to total
        value += ord(c)
    return value
```

