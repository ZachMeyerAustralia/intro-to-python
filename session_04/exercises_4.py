# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
print('Section A - Q1')
fruit_list = ['Apples', 'Cherries', 'Pears', 'Pineapple', 'Peaches', 'Mango']
print(fruit_list)

# 2. Add "Grapes" to the list and print the list.
print('\nSection A - Q2')
fruit_list.append('Grapes')
print(fruit_list)

# 3. Change "Pears" to "Strawberries" and print the list.
print('\nSection A - Q3')
pears_index = fruit_list.index('Pears') 
fruit_list[pears_index] = 'Strawberries' 
print(fruit_list)

# 4. Remove "Apples" from the list and print the list.
print('\nSection A - Q4')
fruit_list.remove('Apples')
print(fruit_list) 


# 5. Print out the current length of the list.
print('\nSection A - Q5')
length_of_list = len(fruit_list)
print(f"The length of the list is: {length_of_list}")


# 6. Order the list alphabetically.
print('\nSection A - Q6')
fruit_list.sort()


# 7. Print out the list again.
print('\nSection A - Q7')
print(fruit_list)





# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
print('\nSection B - Q1')
for fruit in fruit_list:
  print(fruit)

# 2. Print the numbers 1 to 100 (including the number 100).
print('\nSection B - Q2')
for i in range(1,101):
  print(i)


# 3. Print all odd numbers from 1 to 100.
print('\nSection B - Q2')
for i in range(100):
  number = i + 1
  if number % 2 != 0:
    print(number)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
print('\nSection B - Q4')
#Years which olmypics werent  held
no_olympics_these_years = [1916, 1940, 1944, 2020]

for olympic_year in range(1896,2024,4):
  if olympic_year not in no_olympics_these_years:
    print(olympic_year)





# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
print('\nSection B - Q5')
num_list = [5,5,5,5,6,6,6,6,6,6]

odd_count = 0
even_count = 0

for num in num_list:
  if num % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print(f'Even count: {even_count} and odd count: {odd_count}')




# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
print('\nSection B - Q6')
name_list = ['Zach', 'Taylor', 'Sarah','Fred','Bob']

for names in name_list:
  print(f'Hello {names}')



# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
print('\nSection B - Q7')
word = "supercalifragilisticexpialidocious"

for letters in word:
  print (letters)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
print('\nSection B - Q8')

num_list = [1,2,3,4,5]
new_list = [num**2 for num in num_list]

print(new_list)


# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
print('\nSection B - Q9')
name_list = ['Zach', 'Reginald', 'Meyer','Hoppy','Carrots']
new_list = []

for names in name_list:
  dr_name = 'Dr. ' + names
  new_list.append(dr_name)

print(new_list)
  


# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```


print('\nSection B - Q2')
for i in range(1,101):
  if i % 3 == 0 and i % 5 ==0:
    print('fizzbuzz')
  elif i % 3 == 0:
    print('fizz')
  elif i % 5 == 0:
    print('buzz')
  else:
    print(i)

#for i in range(1, 101):
#    output = ""
#    if i % 3 == 0:
#        output += "Fizz"
#    if i % 5 == 0:
#        output += "Buzz"
#    print(output or i)