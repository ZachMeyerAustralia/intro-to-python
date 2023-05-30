# Session 1 Exercises

# Please have a look at the best_practices.md file beforehand.
# Don't forget to comment out any piece of code that you dont want to be executed when running the file.

# Commenting out shortcut:
# Select the lines you want to comment and press:
#     - Windows: ```Ctrl + / ```
#     - Mac: ```Command + /```


## Section A
# 1. Write code that prints ‘Hello world’.
print('Hello World!')


# 2. Print the numbers 1 to 5 on a single line.
print('Q2:')
for i in range(5):
  print(i+1, end=' ')
  
  


# 3. Write a script where ‘Hello’ and ‘World’ are printed on two separate lines.
print('\n\nQ3')
print('Hello')
print('World')



# 4. Write a script that prints a list of names, tabbed on separate lines, e.g.
#     ```My List of Names:
#             Alice
#             Bob
#             Charlie
#     ```
print('\n Q4')
list = ['Alice', 'Bob', 'Charlie']
print('My List of Names:')
for name in list:
  print(f'\t {name}')




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write code that prints the value of 2 + 2.
print('\n S2-Q1')
answer = 2 + 2
print(answer)


# 2. Write code that prints the value of 5.7 subtracted from 3.4.
print('\n S2-Q2')
answer = 5.7 - 3.4
print(answer)



# 3. Write code that prints the value of 8 multiplied by 7.
print('\n S2-Q3')
answer = 8 * 7
print(answer)


# 4. Write code that prints the value of 144 divided by 12.
print('\n S2-Q4')
answer = 144 * 12
print(answer)


# 5. Write code that prints the value of the remainder of 67 divided by 12.
import numpy as np
print('\n S2-Q4')
answer = np.mod(67, 12)
print(answer)



# 6. Write code that finds the value of 20 from `4 - 2 * 6 / 3 * 5`. Hint: you might need brackets.
print('\n S2-Q6')
answer = (4 - 2) * (6 / 3) * 5
print(answer)