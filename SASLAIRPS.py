
print("Rock, Paper or Scissors?")
user = input("").lower()

if user == "rock":
    ai = "Paper"
elif user == "paper":
    ai = "Scissors"
elif user == "scissors":
    ai = "Rock"
else:
    ai = "idk"


print("You fool, you never stood a chance!")
print("I pick " + ai)