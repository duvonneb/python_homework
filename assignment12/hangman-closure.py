# Task 4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        result = ""
        for char in secret_word:
            if char in guesses:
                result = result + char
            else:
                result = result + "_"
        print("Current word:", result)

        for char in secret_word:
            if char not in guesses:
                return False
        return True

    return hangman_closure


# game starts here
secret = input("Type the secret word: ").lower()
print("\n" * 100)  # try to hide the word

game = make_hangman(secret)
done = False

while not done:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1:
        print("Only one letter at a time!")
        continue
    done = game(guess)

print("You got it! The word was:", secret)