import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 5
print("Guess A Number Between 1 and 9")

while chances > 0:
    guess = int(input("Enter number again: "))

    if guess == number:
        print("Congratulations You Won!!! ")
        break
    elif guess < number:
        print("Your guess was too low. Guess a number higher than " , guess)
    else:
        print("Your guess was too high. Guess a number lower than ", guess)
    chances += 1

if not chances > 5:
    print("You loss! the Number was" , number)
    