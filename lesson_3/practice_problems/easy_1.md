# Practice Problems: Easy 1

### Question 1

Will the code below raise an error?

```python
numbers = [1, 2, 3]
numbers[6] = 5
```

The code will raise an `IndexError` because `numbers` only has an index value of 2. The error will be caught when trying to access an non-existent out of bounds element.

### Question 2

How can you determine whether a given string ends with an exclamation mark(!)? Write some code that prints `True` or `False` depending on whether the string ends with an exclamation mark.

```python
str1 = "Come over here!"
str2 = "What's up, Doc?"

# endswith() can be used to determine the last character
print(str1.endswith("!"))	# True
print(str2.endswith("!"))	# False
```

### Question 3

Starting with the string:

```python
famous_words = "seven years go..."
```

Show two different ways to create a new string with “Four score and” prepended to the front of the string.

```python
# Concatenation
new_string = "Four score and " + famous_words

# Format string
new_string = f"Four score and {famous_words}"
```

### Question 4

Using the following string, print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.

```python
munsters_description = "the Munsters are CREEPY and Spooky."

# capitalize() can be used to capitalize the first character
print(munsters_description.capitalize())
# => 'The munsters are creepy and spooky.'
```

### Question 5

Starting with the string:

```python
munsters_description = "The Munsters are creepy and spooky."
```

print the string with the case of all letters swapped:

```python
"tHE mUNSTERS ARE CREEPY AND SPOOKY."
```

That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase.

```python
munsters_description = "The Munsters are creepy and spooky."

for character in munsters_description:
    if character.islower():
        character = character.upper()
    else:
        character = character.lower()
    
    print(character, end = "")
    # => tHE mUNSTERS ARE CREEPY AND SPOOKY.
```

### Question 6

Determine whether the name `Dino` appears in the strings below — check each string separately:

```python
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# 'in' operator can check if the name appears
print("Dino" in str1)	# False
print("Dino" in str2)	# True
```

### Question 7

How can we add the family pet, `“Dino”` to the following list?

```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# An element can be appended by using append()
flintstones.append("Dino")
```

### Question 8

In the previous problem, our first answer added `Dino` to the list like this:

```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
```

How can we add multiple items to our list (e.g., `‘Dino’` and `‘Hoppy’`)? Replace the call to `append` with another method invocation.

```python
# extend() can be used to append multiple elements
flintstones.extend(["Dino", "Hoppy"])
```

### Question 9

Print a new version of the sentence given by `advice` that ends just before the word `house`. Don’t worry about spaces or punctuation: remove everything starting from the beginning of `house` to the end of the sentence.

```python
advice = "Few things in life are as important as house training your pet dinosaur."

# String slicing can be used to get the result
print(advice[:advice.index("house")])
# => Few things in life are as important as
```

### Question 10

Print the following string with the word `important` replaced by `urgent`:

```python
advice = "Few things in life are as important as house training your pet dinosaur."

# replace() can be used to replace sub-strings
print(advice.replace("important", "urgent"))
# => Few things in life are as urgent as house training your pet dinosaur.
```

