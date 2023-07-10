# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
name = input('what is your name: ')
if name.lower() == 'bob':
  print('Welcome Bob!')
else:
  print('Your name is not Bob')
  
# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
name = input('what is your name: ')
if name.lower != 'alice':
  print("You're not Alice")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
password = input('Password: ')

if password == 'qwerty123':
  print('You have successfully logged in')
else:
  print('Password failure')


# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
num_input = input()
if num_input % 2 == 0 :
  print('even')
else:
  print('odd')


# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
num_input_1 = input()
num_input_2 = input()
if num_input_1 + num_input_2 > 21:
  print('bust')
else:
  print('safe')


# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
length = input()
width = input()
if length == width and length > 0:
  print('square')
else:
  print('not a square')


# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
years_of_service = input()
salary = input()

if years_of_service < 3:
  print('no bonus')
else:
  bonus = int(salary) * .1
  print(f'your bonus is {bonus}')
  


# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
num_input = input()

if num_input > 0:
  print(num_input**3)
else:
  print(num_input/2)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
name_input = input()

if name_input.lower() == 'alice':
  print('Hey Alice')
elif name_input.lower() == 'bob':
  print("You're not Bob! I'm Bob")
else:
  print('you must be Charlie')

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
import numbers

def print_age(age_input):
  if age_input == 0:
    print("You're not born yet!")
  elif age_input < 11:
    print("You're too young to go to this school")
  elif age_input < 16:
    print("You can can come to this school")
  else:
    print("You're too old for school")

age_input = input("Please enter your age: ")

try:
  age_input = int(age_input)
  print_age(age_input)

except ValueError:
  print("Please provide a valid integer value.")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
months_to_seasons = {
        "March": "Spring",
        "April": "Spring",
        "May": "Spring",
        "June": "Summer",
        "July": "Summer",
        "August": "Summer",
        "September": "Autumn",
        "October": "Autumn",
        "November": "Autumn",
        "December": "Winter",
        "January": "Winter",
        "February": "Winter"
    }

month_input = input()

if month_input in months_to_seasons:
  print(f"{month_input} is in {months_to_seasons[month_input]}")
else:
  print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
num_input_1 = input()
num_input_2 = input()

if num_input_1 % 2 ==0 and num_input_2 % 2 ==0:
  print('even')
else:
  print('odd')

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
num_input_1 = input()
num_input_2 = input()

if num_input_1 > num_input_2:
  print(num_input_1)
else:
  print(num_input_2)

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

years_of_services = int(input())
salary = int(input())

if years_of_services < 3:
  print('No bonus')
elif years_of_services < 7:
  bonus = salary * 0.15
  print(bonus)
else:
  bonus = salary * 0.2
  print(bonus)


# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
value_dict = {}

for i in range(3):
  print(f'Loop {i+1}')
  name = input('Name: ')
  age = int(input('age: '))

  value_dict[name] = age

max_key = max(value_dict, key=value_dict.get)
print(f"The variable with the maximum value is: {max_key}")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

