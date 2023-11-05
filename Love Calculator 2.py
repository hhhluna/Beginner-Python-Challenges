
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name3=name1.lower()+name2.lower()

t=name3.count("t")
r=name3.count("r")
u=name3.count("u")
e=name3.count("e")

n1=t+r+u+e

l=name3.count("l")
o=name3.count("o")
v=name3.count("v")
e=name3.count("e")

n2=l+o+v+e

love_score= int(str(n1) + str(n2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


