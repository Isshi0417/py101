def oddities(full_list):
    # initialize empty list
    odd_list = []
    # each even index (odd position)
    for index in range(0, len(full_list), 2):
        # append to empty list
        odd_list.append(full_list[index])
    return odd_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True