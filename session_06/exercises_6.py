# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".
apple = {
    "Type": "Bramley",
    "Price": 0.39,
    "Colour": "Green"
}

# 2. Add the best before date to the dictionary - print the dictionary.
apple["Best Before"] = "2023-06-30"
print(apple)


# 3. Change the price to 0.41 - print the dictionary.
apple["Price"] = 0.41


# 4. Set the apple to be on offer using a Boolean - print the dictionary.
apple["On Offer"] = True


# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.
del apple["On Offer"]
print(apple)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.

stored_data = {}

ask_for_names = True

while ask_for_names:
    persons_name = input('Enter users name: ')

    if persons_name:
      persons_age = int(input('Enter users age: '))
      stored_data[persons_name] = persons_age
    else:
        break
    
print(stored_data)



# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).

menu = [
    {"name": "Chicken Parmesan", "price": 15.99, "vegetarian": False},
    {"name": "Vegetable Stir Fry", "price": 12.99, "vegetarian": True},
    {"name": "Steak", "price": 20.99, "vegetarian": False},
    {"name": "Pasta Primavera", "price": 14.99, "vegetarian": True},
    {"name": "Fish and Chips", "price": 18.99, "vegetarian": False}
]

# Print out the entire menu
print("Entire Menu:")
for item in menu:
    print(f"Name: {item['name']}, Price: {item['price']}, Vegetarian: {item['vegetarian']}")

# Print out the name of the vegetarian options
print("\nVegetarian Options:")
for item in menu:
    if item["vegetarian"]:
        print(item["name"])




# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

import random

class bug_game:
    
    
    def __init__(self):
        
        self.body = False
        self.head = False
        self.legs = 0
        self.antenna = 0
        self.eyes = 0
        self.mouth = 0
        self.winner = False
        self.counter = 0
           
    
    def roll_dice(self):
        roll = random.randint(1,6)
        return roll
    
    def play_game(self):
        
        while not self.winner:
            print(f'Round {self.counter}')
            self.counter = self.counter + 1

            roll_number = self.roll_dice()
            print(f'You rolled a : {roll_number}')

            if roll_number == 6:   #If you roll a 6, you can draw the body
                self.body = True
            elif roll_number == 5: #If you roll a 5, you can draw the head
                self.head = True
            elif roll_number == 4 and self.body == True: #If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
                self.legs = min(self.legs + 1, 6)
            elif roll_number == 3 and self.head == True:#If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
                self.antenna = min(self.antenna + 1, 2)
            elif roll_number == 2 and self.head == True:#If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
                self.eyes = min(self.eyes + 1, 2)
            elif roll_number == 1 and self.head == True: #If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
                self.mouth = True

            if self.body == True and self.head == True and self.legs >= 6 and self.antenna >= 2 and self.eyes >= 2 and self.mouth == True:
                self.winner = True
                print('Winner')

            self.print_game_board()

        print('Game Over')
              
        
    
    
    def print_game_board(self):#
        
        print(f' Body: {self.body},\
              \n Head: {self.head},\
              \n Legs: {self.legs},\
              \n Antenna: {self.antenna},\
              \n Eyes: {self.eyes},\
              \n Mouth: {self.mouth}\n' )


game = bug_game()
game.play_game()
