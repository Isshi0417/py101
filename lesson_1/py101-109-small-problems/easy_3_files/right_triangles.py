def triangle(n):
    for i in range(n):
        print(f'{' ' * (n - i)}{'*' * i}')

triangle(9)