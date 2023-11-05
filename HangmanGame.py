import os
import random
from hangman_art import logo, stages

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



print(logo)
print("Wlecome to the game of Hangman! Let's start!")

#This is the word (to try it)
print(f"The word: {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    
    if guess in display:
      print(f"You have already guessed {guess}")
   
    for position in range(word_length):
        letter = chosen_word[position]
      
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
      
        
        lives -= 1
        print(f"You have guessed {guess}, and that is not in the word! You lose a life. You have {lives} tries left!")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    
    print(stages[lives])