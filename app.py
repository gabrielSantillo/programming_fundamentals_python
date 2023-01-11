# print("Hello World")

# print('   /|')
# print('  / |')
# print(' /  |')
# print('/___|')

# character_name = "Gabriel"
# character_age = 26
# is_male = True

# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old.")

# character_name = "Mike"

# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")

# phrase = "Coding in Python"
# print(phrase.index("o"))

# from math import *

# print(3 * 4.5 )

# name = input("Enter your name: ")
# print("Hello " + name + "!")

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")

# result = float(num1) + float(num2)
# print(result)

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are red " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# friends = ["Kevin," "Karen", "Jim", "Oscar", "Toby"]

# print(friends[1:])

# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
# # friends.extend(lucky_numbers)
# friends.insert(0, "Gabriel")
# name = "Jim"
# # friends.remove(name)
# # friends.clear()
# friends.sort()
# lucky_numbers.reverse()
# friends_ = friends.copy()

# print(friends)
# print(friends_)

# coordinates = (4, 5)
# coordinates[0] = 8
# print(coordinates)

# def say_hi(name):
#     print("Hello " + name)

# say_hi("Gabriel")

# def cube(num):
#     result = num * num * num
#     return result

# print(cube(3))

# is_male = False
# is_tall = False

# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a male nor tall")


# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter first number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

# month_conversations = {
#     "Jan": "Janury",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE")
else:
    print("You win!!!")