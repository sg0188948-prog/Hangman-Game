import random

# List of predefined words
words = ["python", "computer", "laptop", "coding", "program"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while incorrect_guesses < max_incorrect:
    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_incorrect - incorrect_guesses)

# Game Over
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
