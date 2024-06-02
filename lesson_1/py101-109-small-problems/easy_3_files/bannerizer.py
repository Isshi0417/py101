def print_in_box(string):
    width = len(string)
    border = '-'
    box = f'''
    +{border * (width + 2)}+
    | {' ' * width} |
    | {string} |
    | {' ' * width} |
    +{border * (width + 2)}+
    '''
    print(box)
    
print_in_box('To boldly go where no one has gone before.')
print_in_box('')