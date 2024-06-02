def greetings(l, d):
    # join list into ful name
    name = " ".join(l)
    # concatenate title and occupation
    job = d['title'] + " " + d["occupation"]
    return f'Hello, {name}! Nice to have a {job} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.