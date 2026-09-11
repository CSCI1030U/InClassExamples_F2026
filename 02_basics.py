# input and output

# name: str = input('What is your name? ')
# age_string: str = input('How old are you? ')
# age: int = int(age_string)
# age = int(input('How old are you? '))
# str(18)
# float('3.14159')
# float(18)
# above is commented out since testing code with input() is tedious
name: str ='Kumar'
age: int = 9

# an awkward way to create a multi-line string
message1: str = 'Hello\nGoodbye'

# multi-line strings
message2: str = '''
Line 1
Another line
Again...
'''

# format strings - let you add dynamic data (variables and computed values) to a string
message: str = f'In 5 years, {name} will be {age + 5} years old.'
print(message)

# all in one line
print(f'In 5 years, {name} will be {age + 5} years old.')
