# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
import random #import python random package
print(random.randint(1, 10))

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .

run = True
while run:
  user_number = input('Enter a number: ')
  if user_number == 7:
    print('Wow lucky number 7!')
    run = False
  else:
    print('Try again -')

run = True
rand_nums = random.randint(1, 10)
while run:
  user_number = input('Enter a number: ')
  if int(user_number) == rand_nums:
    print(f'Wow lucky number {rand_nums}!')
    run = False
  else:
    print('Try again -')






# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

def area_function(width, height):
  area = int(width) * int(height)
  area = round(area,0)/10000
  return area

user_width = input('Width: ')
user_height = input('Height: ')
area = area_function(user_width, user_height)
print(f'The area is {area}m2')

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

password_run = True
attempt = 1
while password_run:
  user_password = input('Enter password: ')
  attempt += 1
  if attempt == 4:
    print('System Locked!')
    password_run = False
  elif user_password == 'qwerty123':
    print('You have successfully logged in')
    password_run = False
  else:
    print('Password failure')
    
# 5. Add up all the numbers from 1 to 500 and print the answer.
added_num = 0
for i in range(1,501):
  added_num += i

print(added_num)

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
num_list = []
print('Enter 10 numbers, one must be 99')
for i in range(10):
  user = int(input('Enter Number'))
  num_list.append(user)

print(num_list.index(99))


# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36

for i in range(1,16):
  answer = 18 * i
  print(f'{i} * 18 = {answer}')



# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.

run_loop = True
start_num = 1
while run_loop:
  if start_num == 100:
    run_loop = False
  print(start_num)
  start_num += 1
  



# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

def return_grade(mark):
  if mark >= 80:
    print('A')
  elif mark >= 60:
    print('B')
  elif mark >= 50:
    print('C')
  elif mark >= 45:
    print('D')
  elif mark >= 25:
    print('E')
  else:
    print('F')


grading_system = True

while grading_system:
  input_grades = int(input('Enter Grades: '))
  return_grade(input_grades)

  flag = input('more lessons Y/N')
  if flag == 'N':
    grading_system = False


# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
import random

entires_list = []

enter_people = True
while enter_people:
  new_entry = input('Enter name: ')
  entires_list.append(new_entry)

  more_names = input('Y/N')
  if more_names == 'N':
    enter_people = False

temp = random.randint(0,len(entires_list)-1)

print(f'Winner is {entires_list[temp]}')
  
# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

def r_p_s_game():

  game = True
  #Check Move
  while game:
    
    ####
    user_move = input('R or P or S: ')
    print(f'User plays: {user_move}')

    #####
    computer_play = random.randint(1,3)
    if computer_play == 1:
      computer_move = 'R'
    elif computer_play == 2:
      computer_move = 'P'
    else:
      computer_move = 'S'
    print(f'Computer plays: {computer_move}')

    ######
    if user_move == computer_move:
      print('Same same')
    elif user_move == 'R' and  computer_move == 'S':
      print('User wins')
      game = False
    elif user_move == 'R' and computer_move == 'P':
      print('Computer wins')
      game = False
    elif user_move == 'P' and  computer_move == 'S':
      print('Computer wins')
      game = False
    elif user_move == 'P' and  computer_move == 'R':
      print('User wins')
      game = False
    else:
      print('ERROR')

