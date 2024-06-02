def xor(a1, a2):
    if (a1 and not a2) or (not a1 and a2):
        return True
    return False
      
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)