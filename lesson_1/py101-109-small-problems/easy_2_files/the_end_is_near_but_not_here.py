def penultimate(s):
    # split string into list
    l = s.split()
    # return the second last element from list
    return l[-2]
    
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")