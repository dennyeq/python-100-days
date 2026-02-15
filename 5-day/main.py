import random
list_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

list_numbers = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

list_symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}','~'
]

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers you like?\n"))

list_aux = []
password = ""

for i in range(0, letters):
	choose = random.choice(list_letters)
	list_aux.append(choose)

for i in range(0, numbers):
	choose = random.choice(list_numbers)
	list_aux.append(choose)

for i in range(0, symbols):
	choose = random.choice(list_symbols)
	list_aux.append(choose)

print(list_aux)
random.shuffle(list_aux)
print(list_aux)

for char in list_aux:
	password = password + char
print(f"Yor password is: {password}")