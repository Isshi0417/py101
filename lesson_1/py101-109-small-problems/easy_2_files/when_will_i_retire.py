from datetime import date

# initialize variables
age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))
year = date.today().year
retirement_year = retirement_age - age + year

# print result
print(f"\nIt's {year}. You will retire in {retirement_year}.")
print(f'You only have {retirement_age - age} years of work to go!')