import string
import random
import sys

string.ascii_letters

numberOfCharacters = int(input("Počet písmen: "))




for x in range(numberOfCharacters):
    randomInt = int(random.randint(0, 9));
    randomString = random.choice(string.ascii_letters)

    randomVariable = int(random.randint(0, 2));
    if(randomVariable == 0):
        print(randomString, end="")
    else:
        print(randomInt, end="")
    
    