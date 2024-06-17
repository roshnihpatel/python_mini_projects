import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)

correct_guess = False
guesses = 0

while not correct_guess:
    guesses += 1
    guess = input("Please guess a number between 0 and %d: " % top_of_range)
    if guess.isdigit():
        guess = int(guess)
        
        if guess == random_number:
            print("Congratulations! You guessed correctly, you made %d guesses" % guesses)
            correct_guess = True
        elif guess < 0 | guess > top_of_range:
            print("Please type a number between 0 and %d" % top_of_range)
        elif guess < random_number:
            print("Too low, try again!")
        else:
            print("Too high, try again!")
    
    else:
        print("Please type a number")



