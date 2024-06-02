def multiply(n1, n2):
    return n1 * n2

def square(n):
    # invoke multiply() with same numbers
    return multiply(n, n)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True