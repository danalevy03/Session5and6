name = input("what is your name?")
age = input("how old are you?")
age = int(age)
birth_year = 2023 - age

print(f"OMG {name}, you are {age} years old so you were born in {birth_year}!")
print("OMG", name + ", you are", age, "years old so you were born in ", birth_year)

# faster way:
# age = int(input("What is your age?"))
# print(f"Your age is {age}")