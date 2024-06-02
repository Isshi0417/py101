# Easy 3

### Repeat Yourself

Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

```python
def repeat(s, n):
    for i in range(n):
        print(s)
```

### ddaaiillyy ddoouubbllee

Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

```python
def crunch(string):
    crunched = ''
    # for each letter in string
    for index in range(len(string)):
        # if letter is not in crunched or the letter before is not the same
        if string[index] not in crunched or string[index - 1] != string[index]:
            crunched += string[index]
    return crunched
```

### Bannerizer

Write a function that takes a short line of text and prints it within a box.

```python
def print_in_box(string):
    width = len(string)
    box_line = '-'
    box = f'''
    +{box_line * (width + 2)}+
    | {' ' * width} |
    | {string} |
    | {' ' * width} |
    +{box_line * (width + 2)}+
    '''
    print(box)
```

### Strings Strings

Write a function that takes one argument, a positive integer, and returns a string of alternating `'1'`s and `'0'`s, always starting with a `'1'`. The length of the string should match the given integer.

```python
def stringy(n):
    string = ''
    # foe each number in n
    for i in range(n):
        # if number is odd
        if i % 2 == 1:
            string += '0'
        else:
            string += '1'
    return string
```

### Right Triangles

Write a function that takes a positive integer, `n`, as an argument and prints a right triangle whose sides each have `n` stars. The hypotenuse of the triangle (diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

```python
def triangle(n):
    for i in range(n):
        print(f'{' ' * (n - i)}{'*' * i}')
```

### Madlibs

Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you can create.

```python
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')

print(f'Do you walk your {adjective} {noun} {adverb}? That\'s hilarious!')
print(f'The {adjective} {noun} {verb}s {adjective} over the lazy dog.')
print(f'The {noun} {adjective} {verb}s up to Joe\'s blue turtle.')
```

### Double Doubles

A double number is an even-length number whose left-side digits are exactly the same as its right-side digits. For example, `44`, `3333`, `103103`, and `7676` are all double numbers, where as `444`, `334433`, and `107` are not.

Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.

```python
def twice(n):
    string = str(n)
    if len(string) % 2 == 0:
        # determine midpoint
        halfway = len(string) // 2
        # compare string value cut at midpoint
        if string[:halfway] == string[halfway:]:
            return n
        else:
            return n * 2
    else:
        return n * 2
```

### Grade Book

Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

- 90 <= score <= 100: 'A'
- 80 <= score < 90: 'B'
- 70 <= score , 80: 'C'
- 60 <= score < 70: 'D'
- 0 <= score < 60: 'F'

Tested values are all between `0` and `100`. There is no need to check for negative values or values greater than 100.

```python
def get_grade(n1, n2, n3):
    average = (n1 + n2 + n3) / 3
    
    if average >= 90 and average <= 100:
        return "A"
    elif average >= 80 and average <= 90:
        return "B"
    elif average >= 70 and average <= 80:
        return "C"
    elif average >= 60 and average <= 70:
        return "D"
    else:
        return "F"
```



### Clean up the words

Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

```python
def clean_up(string):
    space_string = ""
    clean_string = ""
    
    # for each letter in string
    for letter in string:
        # if letter is an alphabet
        if letter.isalpha():
            space_string += letter
        elif not letter.isalpha():
            space_string += " "
    
    # for each index in space_string
    for index in range(len(space_string)):
        # always add first element
        if index == 0:
            clean_string += space_string[index]
        # if element is a duplicate as the previous element
        elif space_string[index] == space_string[index - 1]:
            # do nothing
            continue
        else:
            clean_string += space_string[index]
    
    return clean_string
```

### What Century is That?

Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with `st`, `nd`, `rd`, or `th` as appropriate for that number.

New centuries begin in years that end with `01`. So, the years 1901 - 2000 compromise the 20th century.

```python
def century(year):
    decade = (year // 100) + 1
    
    # if year is ~000
    if year % 100 == 0:
        decade -= 1
        
    tens = decade % 100    
    ones = decade % 10
    
    match tens:
        case 11:
            return f"{decade}th"
        case 12:
            return f"{decade}th"
        case 13:
            return f"{decade}th"
    
    match ones:
        case 1:
            return f"{decade}st"
        case 2:
            return f"{decade}nd"
        case 3:
            return f"{decade}rd"
        case _:
            return f"{decade}th"
```

