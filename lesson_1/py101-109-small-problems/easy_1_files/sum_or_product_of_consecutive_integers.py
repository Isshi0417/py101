# initialize variables
n = int(input('Please enter an integer greater than 0: '))
op = input('Enter "s" to compute the sum, or "p" to compute the product. ')

# if addition
if op == 's':
    sum = 0
    # for each number from 1 through n
    for i in range(1, n + 1):
        # add to total
        sum += i
    print(f'\nThe sum of the integers between 1 and {n} is {sum}.')
else:
    product = 1
    # for each number from 1 through n
    for i in range(1, n + 1):
        # multiply to total
        product *= i
    print(f'\nThe product of the integers between 1 and {n} is {product}.')