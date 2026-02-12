import random
c = int(input("what so you choose? Type 0 for Rock, 1 for Paper or 2 for Scissorsa\n"))
lista = [0, 1, 2]
i = random.randint(0, 2)
print(f"Computer Choose:\n{i}")
if i == c:
	print("It's a draw")
elif c == 0:
	if i == 2:
		print("You win")
	else:
		print("You lose")
elif c == 1:
	if i == 0:
		print("You win")
	else:
		print("You lose")
elif c == 2:
	if i == 1:
		print("You win")
	else:
		print("You lose")
else:
	print("Error: Write 0, 1 or 2")

