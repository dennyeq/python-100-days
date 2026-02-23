letters = []
for i in range(97, 123):
	letters.append(chr(i))

def encode(message, shift):
	i = 0
	res = ""
	for l in message:
		if l in letters:
			i = letters.index(l)
		if l == "z":
			res += letters[25 - i]
		elif l in letters:
			res += letters[i + shift ]
		else:
			res += l
	return res

def dencode(message, shift):
	res = ""
	for l in message:
		if l in letters:
			i = letters.index(l)
		if l == "a":
			res += letters[i + 25]
		elif l in letters:
			res += letters[i-shift]
		else:
			res += l
	return res