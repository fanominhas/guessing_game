import random
print("Welcome to brain challange! created by Farhana")
print("Choose Level:")
print("1. Easy (1 to 50, 10 chances)")
print("2. Hard (1 to 100, 5 chances)")
choice =int(input("Enter your choice (1 or 2): "))
if choice == 1:
    secret_number = random.randint(1, 50)
    chances = 10
    print("You selected Easy Level. You have 10 chances.")
else:
    secret_number = random.randint(1, 100)
    chances = 5
    print("You selected Hard Level. only 5 chances. good luck")
attempts = 0
guess = 0
while attempts < chances and guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1
    if guess < secret_number:
        print("Too Low! try again")
    elif guess > secret_number:
        print("Too High! give it another try")
    else:
        print("Woooo! Congratulations! You guessed it right.")
if guess != secret_number:
    print("Ooooo Oooo! Game Over! The correct number was", secret_number)
