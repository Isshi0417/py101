def get_grade(n1, n2, n3):
    average = (n1 + n2 + n3) / 3
    
    if average >= 90 and average <= 100:
        return "A"
    elif average >= 80 and average <= 90:
        return "B"
    elif average >= 70 and average <= 80:
        return "C"
    elif average >= 60 and average <= 70:
        return "D"
    else:
        return "F"

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True