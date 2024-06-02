def multisum(n):
    sum = 0
    # for each number from 0 through n
    for i in range(n + 1):
        # if divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # add to sum
            sum += i
    return sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)