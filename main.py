from datetime import datetime

name = input("what is your name?")

while True:
	age = input("How old are you?")
	
	try:
		age = int(age)
		
		if age < 0 or age > 120:
			print("Invalid age. Please enter between 0 and 120.")
		else:
			break
	except ValueError:
		print("Invalid input. Please enter a number.")

def calculate_birth_year(age):
	year = datetime.now().year - age
	return year

year_until_adult = 18 - age

def say_hello(name):
	print("Hello,", name)

say_hello(name)

birth_year = calculate_birth_year(age)
print("You were born around", birth_year)

if age >= 18:
	print("You are an adult")
else:
	print("You are a minor")
	print("You have", year_until_adult, "years until you are an adult")
