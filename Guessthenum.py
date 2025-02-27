import random 

def guess_the_number():
    number = random.randint(1, 100)  # Generate a random number
    guesses_left = 7  # Set the number of attempts
    
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100.")
    
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))  # Get user input
        except ValueError:
            print("Invalid input: Please enter a valid number.")
            continue 
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.")
            return  # Exit function if guessed correctly
        
        guesses_left -= 1  # Decrease attempts
    
    # This prints only when the player runs out of guesses
    print(f"\nGame Over! You ran out of guesses. The correct number was {number}.")
    
# Start the game
guess_the_number()
