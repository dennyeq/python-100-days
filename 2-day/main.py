total_bill = float(input("What wos the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
many_people = int(input("How many people to split the bill? "))
person_pay = (total_bill * (tip / 100 + 1)) / many_people
print(f"Each person should pay: ${round(person_pay, 2)}")

