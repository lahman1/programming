import random
from day7_hangman_art import stages
from day7_hangman_words import word_list

word = random.choice(word_list)
word_len = len(word)
# print(f'Pssst, the solution is {word}.')

blank_word = []
for w in range(word_len):
    blank_word.append("_")

lives = 6
end_of_game = False
while not end_of_game:
    print("Word: " + " ".join(blank_word))
    guess = input("Enter the letter you want to guess:\n# ").lower()
    for position in range(word_len):
        letter = word[position]
        if letter == guess:
            blank_word[position] = letter

    if guess not in word:
        lives -= 1

    print(stages[lives])

    if "_" not in blank_word:
        end_of_game = True
        print("You win! ")

    if lives == 0:
        end_of_game = True
        print("You Lose!")
        print(f"The word was {word}")
