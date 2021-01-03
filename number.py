#import and n = random.randint is copied
import random
n = random.randint(0,10)

guess = int(input("enter your guess: "))

if n == guess:
    print("good job!")
else:
    print("sorry try again")


print(n)