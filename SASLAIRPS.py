rps = ["rock", "paper", "scissors"]
while True:
    try: print("\nI pick " + rps[(rps.index(input("Rock, Paper or Scissors?\n").lower()) + 1) % 3] + "\n")
    except ValueError: print("No cheating!!\n")