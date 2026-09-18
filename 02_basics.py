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

# expressions
length: float = 5.5
width: float = 9.25
area: float = length * width 
print(f'{area = }')

# types
msg_type = type(message)
print(f'{msg_type = }')
print(f'{type(area) = }')
hungry: bool = True 
print(f'{type(hungry) = }')

# conditionals
hour: int = 20
if hour >= 22:
    print('It is late.  Please keep it down.')

age: int = 11
if age <= 8:
    print('Docked mode')
else:
    print('Handheld mode')

mark: float = 95
if mark >= 80:
    print('A')
elif mark >= 70:
    print('B')
elif mark >= 60:
    print('C')
elif mark >= 50:
    print('D')
else:
    print('F')

# loops

# for loops - used for when you know the number of iterations
#             or when iterating over data
# while loops - can be used in any situation, but are best for
#               when you don't know the number of iterations
#               e.g. hill climbing
balance: float = 1000
interest_rate: float = 0.035

for year in range(50):
    interest: float = balance * interest_rate
    balance = balance + interest 

print(f'{balance = }')

for x in [1,2,3,4,5]:
    print(f'{x = }')

# range(start, end, step)
# start - initial number (0)
# end - exit number (*)
# step - how to go to the next number (x = x + step) (1)
# all numbers from start up to (but not including) end, increasing by step

for i in range(5, 15, 2):
    print(f'{i = }')

for j in range(10, 0, -1):
    print(f'{j = }')

num: int = 1
while num <= 5:
    print(f'{num = }')




