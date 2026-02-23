import code

print("Welcome to Caesar Cipher")

while True:
	type_crypt = input("Type 'encode' to encrypt, type dencode to decrypt:\n").lower()
	if type_crypt == "encode" or type_crypt == "dencode":
		message = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))
		if type_crypt == "encode":
			new_message = code.encode(message, shift)
			print(f"Here's the encoded result: {new_message}")
		elif type_crypt == "dencode":
			new_message = code.dencode(message, shift)
			print(f"Here's the dencoded result: {new_message}")
		stop = input("which do you want?, Yes to contine or any char to finish: ").lower()
		if stop != "yes":
			break
	else:
		print(f"Error: {type_crypt} is not 'encode or dencode'")
	