from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


    
  

print(logo)
bid_log = {}
bid_finished = False

def find_highest_bidder(bidding_log):
  highest_bid = 0
  winner = ""
  for bidder in bidding_log:
    bid_amount = bidding_log[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bid_finished:
  name = input("What is your name?: ").lower()
  bid = int(input("What is your bid?: $"))
  bid_log[name] = bid
  new_bid_choice = input("Are there any other bidders? Type 'yes or 'no'.\n").lower() 
  if new_bid_choice == "no":
    bid_finished = True
    find_highest_bidder(bid_log)
  elif new_bid_choice == "yes":
    clear()
  
 
  
  
  
  





