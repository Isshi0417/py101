# Practice Problems: Medium 1

### Question 1

Let’s do some “ASCII Art”: a stone-age form of nerd artwork from back in the days before computers had video screens.

For this practice problem, write a program that outputs `The Flintstones Rock!` 10 times, with each specific line prefixed by one more hyphen than the line above it. The output should start out like this:

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

