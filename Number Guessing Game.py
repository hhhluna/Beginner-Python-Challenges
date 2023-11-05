
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Checks guess against answer, Returns the number of turns left."""
  if guess < 0 or guess > 100:
    print("You made an invalid guess. Try again.")
  elif guess < answer:
    print("Too low")
    return turns - 1
  elif guess > answer:
    print("Too high")
    return turns - 1
  else:
    print(f"You guessed right! Congratulations!! The answer is {actual_number}")

def difficulty_level():
  level = input("Please choose a difficulty. Type 'easy' or 'hard'.: ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  
  answer = random.randint(1,100)
  print(f"Psst! The answer is : {answer}")
  
  
  turns = difficulty_level()
  
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} guesses remaining.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You have run out of guesses. You lose!")
      return

game()