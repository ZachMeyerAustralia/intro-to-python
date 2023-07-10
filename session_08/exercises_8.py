# Session 8 Exercises


# All of these questions will use a set of pre-made files with data in. The files are in the text_files directory.
# In order to access the text files from this file, make sure you get into the text_files directory when using read/write.
# Ex: f = open("text_files/austen.txt", "r") OR f = open("text_files/register.txt", "w")
from pandas import DataFrame

f = open("text_files/austen.txt", "r")

df = DataFrame(f)


## Section A
# 1. Read the file 'jabberwocky.txt' and print its content to the screen.




# 2. Read the file 'austen.txt' and print the amount of lines in the file.




# 3. Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file.




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter their name and append this to a file called 'register.txt'.



# 2. Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'.



# 3. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. 
#    Work out what the secret message says.



# 4. Benford’s law states that the leading digits in a collection of data are probably going to be small. 
#   For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
#   Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
#   Work out which of the files contains fake data.
