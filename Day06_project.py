import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Ask the user how many attempts they would like
    attempts = int(input("How many attempts would you like to guess the number? "))
    
    # Keep track of the current attempt
    attempt_count = 0
    
    print("\nGuess the number between 1 and 100!")
    
    # While loop for the guessing process
    while attempt_count < attempts:
        # Get the user's guess
        guess = int(input(f"Attempt {attempt_count + 1}/{attempts}: Enter your guess: "))
        
        # Increment the attempt count
        attempt_count += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempt_count} attempts.")
            break
        # Provide hints
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    # If the user runs out of attempts
    if guess != secret_number:
        print(f"\nSorry, you've used all {attempts} attempts! The correct number was {secret_number}.")

# Start the game
number_guessing_game()
