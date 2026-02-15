import random
user_choose = int(input("what so you choose? Type 0 for Rock, 1 for Paper or 2 for Scissorsa\n"))
list = ["Rock", "Paper", "Scissorsa"]
if user_choose == 0 or user_choose == 1 or user_choose == 2:
	print(f"{list[user_choose]}")
	maching_choose = random.randint(0, 2)
	print(f"Computer Choose:\n{list[maching_choose]}")
	if maching_choose == user_choose:
		print("It's a draw")
	elif user_choose == 0 and maching_choose == 2:
		print("You win")
	elif user_choose == 1 and maching_choose == 0:
		print("You win")
	elif user_choose == 2 and maching_choose == 1:
		print("You win")
	else:
		print("You lose")
else:
	print(f"Error: Your choose is not valid.")
