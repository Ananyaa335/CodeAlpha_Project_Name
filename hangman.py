import random

def get_word():
    words = ["python", "hangman", "challenge", "programming", "computer", "science"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = get_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, {guess} is not in the word. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
            guessed_letters.add(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nYou've run out of guesses. The word was: {word}. Better luck next time!")

if __name__ == "__main__":
    play_hangman()
