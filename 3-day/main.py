print("Welcome to Treasure Island")
print("You're at a cross road. Were do you wont to go?")
type = input('	Type "left" or "right"\n').lower()
if type == "left":
	print("You've come to a loke. There is on island in the middle of the loke.")
	type = input('	Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
	if type == "wait":
		print("You arrive at the island unharmed. There is a house with 3 doors")
		type = input("	One red, one yellow and one blue. Which colour do you choose?\n").lower()
		if type == "yellow":
			print("You win")
		elif type == "red" or type == "blue":
			print("Game Over")
		else:
			print("Erro: Choose red, blue or yellow")
	elif type == "swim":
		print("Game Over")
	else:
		print("Erro: Choose wait or swim")
elif type == "right":
	print("Game Over")
else:
	print("Erro: Choose left or right")