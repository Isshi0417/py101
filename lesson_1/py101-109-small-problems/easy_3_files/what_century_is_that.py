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
    

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True