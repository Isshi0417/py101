name = input("What's your name? ")

# if ! is in input
if '!' in name:
    # print message and capitalize name
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')