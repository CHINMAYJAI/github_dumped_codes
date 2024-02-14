# Password generator
# Created by: CHINMAY JAIN 
# Dated: 12/02/24

import random

string1 = ""
string2 = ""

# Characters that we can use to create a strong password
characters = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_"
# For getting the strong passcode we use some special characters
necessary_characters_in_the_password = "!@#$%^&*_"

# The length of the passcode that the user wants to generate 
length_of_password = int(input("Enter the length of the passcode: "))

for i in range(0,(length_of_password-3)):
    string1 = random.choice(characters) # Random module has a function "choice" which Returns a random element from the given sequence.
    string2+=string1 # Concatination of the string.
for a in range(0,3):
    string1 = random.choice(necessary_characters_in_the_password)
    string2+=string1

with open("passcode_generator.txt","w") as file:
    file = file.write(f"Suggested passcode:\n{string2}\nBy: CHINMAY JAIN")

print("Passcode has been written successfully!")
