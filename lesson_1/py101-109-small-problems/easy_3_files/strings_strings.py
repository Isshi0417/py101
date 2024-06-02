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
    
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True