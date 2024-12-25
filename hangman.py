import random

def hangman():
    words = [
        "python", "programming", "hangman", "challenge", "developer", "function", 
        "algorithm", "variable", "loop", "condition", "debugging", "software",
        "hardware", "compile", "execute", "keyboard", "syntax", "exception", 
        "binary", "decimal", "array", "string", "integer", "floating", "boolean"
    ]
    word = random.choice(words)
    guessed_word = ["_" for _ in word]
    attempts_left = 6
    guessed_letters = []
    print("Welcome to Hangman!")
    print("You have", attempts_left, "incorrect guesses available.")
    while attempts_left > 0 and "_" in guessed_word:
        print("\nWord to guess:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print(f"Attempts remaining: {attempts_left}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print("Wrong guess.")
            attempts_left -= 1
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
