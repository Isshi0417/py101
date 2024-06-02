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
    
print(clean_up("---what's my +*& line?") == " what s my line ")
# True