# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
name = input('Input name: ')

def print_name(name):
  print(name)

#print_name(name)

# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".

def print_name(name):
  print(f'Hello {name}')

#print_name(name)


# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.

name_list = ["Alice", "Bob", "Charlie"]

for name in name_list:
  print_name(name)



# 4. Write a function that prints the area of two passed in parameters.

def distance(x,y):
  print(x - y)


distance(10,5)

# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.

def print_list(list):
  for i in list:
    print(i)

#print_list(name_list)


# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

age = 26

def age_checker(age):

  if age != type(int):
    print('Error')
  else:
    age = int(age)

    if age == 0:
      print('You are not born yet')
    elif age < 11:
      print('')
  
#age_checker(age)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).



def is_odd(number):

  if int(number) % 2 == 0:
    return True
  else:
    return False


number = 5
print(is_odd(number))






# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.

def return_word_backwards(word):
  answer = ''
  for letter in word :
    answer = letter + answer

  print(answer)

word = 'hello'
return_word_backwards(word)



# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```

def print_stars(n):
  if n > 0:
    print('*' * n)
    print_stars(n - 1)

print_stars(5)


# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".


def padlock():
  password_entered = input('Enter password: ')

  if password_entered == 'abc':
    print('unlocked')
  else:
    print('locked')
  

padlock()



# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def multiples(num):

  answer = 0

  for i in range(num+1):
    if i % 3 == 0 or i % 5 == 0:
      answer += i

  print(answer)

multiples(9)



# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.

def is_prime(number):

  for i in range(2,number):
    if number % i == 0:
      print('Not Prime')
      break

  print('Prime')

is_prime(5)
is_prime(6)

 
# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.

def is_palindrome(s):
    s = s.replace(' ', '').lower()  # Remove spaces and convert to lower case
    return s == s[::-1]

print(is_palindrome("Able was I ere I saw Elba"))





# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.

def is_palindrome_sentence(sentence):
    sentence = ''.join(c for c in sentence if c.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lower case
    return sentence == sentence[::-1]

print(is_palindrome_sentence("Able was I, ere I saw Elba."))



