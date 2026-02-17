import random, art_hangman, name_hangman

list_aux = []
letter = ""
word = ""
life = 5
choice = random.choice(name_hangman.list)

print("Welcome to HANGMAN")

for i in range(len(choice)):
	list_aux.append("_")
for char in list_aux:
	word += char

while True:
	letter_aux = letter
	pos = 0
	print(f"Word to guess: {word}")
	letter = input("Guess a letter: ")
	word =""
	if letter not in choice or letter_aux == letter:
		print(f"You guessed {letter}, thet's not the word, you lose a life")
		life = life - 1
		#break
	for char in choice:	
		if letter == char:
			list_aux[pos] = char
		pos += 1	
	for char in list_aux:
		word += char
	if letter in choice:
		print(word)
	print(art_hangman.hangman_stages[5-life])
	print(f"Your life = {life}")
	if word == choice:
		print("You win")
		break
	if life <= 0:
		print("Game Over")
		break
	
