def crunch(string):
    crunched = ''
    # for each letter in string
    for index in range(len(string)):
        # if letter is not in crunched or the letter before is not the same
        if string[index] not in crunched or string[index - 1] != string[index]:
            crunched += string[index]
    return crunched

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')