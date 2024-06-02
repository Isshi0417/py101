def center_of(s):
    # determine center position
    position = len(s) // 2
    # if length of s is even
    if len(s) % 2 == 0:
        # concatenate the middle point and the character before
        return s[position - 1] + s[position]
    else:
        return s[position]
        
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True