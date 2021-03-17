
print("Rock, Paper or Scissors?")
user = input("").lower()

if user == "rock":
    ai = "paper"
elif user == "paper":
    ai = "scissors"
elif user == "scissors":
    ai = "rock"
else:
    ai = "idk"


print("You fool, you never stood a chance!")
print("I pick " + ai)