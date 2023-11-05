from art import vs, logo
from game_data import data
import random
from replit import clear


def get_random_choice():
  return random.choice(data)


def format(account):
  """Takes the account data and returns the printable format"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description} from {country}"


def compare(guess, a_followers, b_followers):
  """Takes the user guess and the follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  if b_followers > a_followers:
    return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = get_random_choice()

while game_should_continue:
  account_a = account_b
  account_b = get_random_choice()
  if account_a == account_b:
    account_b = get_random_choice()

  print(f"Compare A: {format(account_a)}.")
  print(vs)
  print(f"Compare B: {format(account_b)}.")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = compare(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"You're right! Your current score: {score}")

  else:
    game_should_continue = False
    print(f"Sorry, that is wrong! Final score: {score}")
