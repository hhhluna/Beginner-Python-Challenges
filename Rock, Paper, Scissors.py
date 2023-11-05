import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images= [rock, paper, scissors]
answer = int(input("Please specify if you want rock with 0, paper with 1, and scissors with 2: "))
if answer >=3 or answer < 0:
  print("You typed an invalid number. You lose!")
else:
  print(game_images[answer])
  
  
  print("Computer chose: ")
  answer2 = random.randint(0,2)
  print(game_images[answer2])
  
  
  
  
  if answer == 0 and answer2 == 2:
    print("You win!")
  elif answer2 == 0 and answer == 2:
    print("You lose!")
  elif answer2 > answer:
    print("You lose!")
  elif answer > answer2:
    print("You win!")
  elif answer == answer2:
    print("It's a draw!")
  
    
