# ask for input
bill = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

# calculate tip
tip = bill * (tip_percentage / 100)
total = bill + tip

# print results
print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')