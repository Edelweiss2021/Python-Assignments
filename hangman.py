import random, string


def hangman():
    words = ["CROW", "OWL", "EAGLE", "PIGEON", "SWALLOW", "FALCON", "PARROT",
             "SPARROW", "SWAN", "FLAMINGO", "PELICAN"]

    word = random.choice(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    chance = 10

    while len(word_letters) > 0 and chance > 0:
        print("You have used these words: ", " ".join(used_letters))
        print(f"You have {chance} chances!")

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Write a letter: ").upper().strip()
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                chance -= 1
        elif user_letter in used_letters:
            print("You have already used this letter...")
        else:
            print("Invalid character...")
    if chance == 0:
        print(f"You failed.. The word was {word}")
    else:
        print(f"Congrats... You won.. The word was {word}")


print("Welcome to hangman game. You should guess a bird species. Good Luck!!1")
hangman()