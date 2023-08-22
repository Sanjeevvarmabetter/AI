name = input("Enter your name: ")
print("Hello " + name + ", it's time to play!")

print("Start guessing")
turns = 10
guesses = " "

# Secret word
secret_word = "hello"
while turns > 0:
    failed = 0
    for char in secret_word:
        if char in guesses:
            print("You guessed correctly")
            print(char, end=" ")  # Print the character with a space
        else:
            print("-", end=" ")   # Print a dash with a space
            failed += 1           # Increment failed count

    if failed == 0:
        print("\nYou won!")
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in secret_word:
        turns -= 1
        print("Wrong guess")
    print("You have " + str(turns) + " more guesses")  # Convert turns to string
    if turns == 0:
        print("Game is over, you lost!!")
