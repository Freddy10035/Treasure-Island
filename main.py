#################################################################################
# Roller-Coaster payment
#################################################################################

# print("Welcome to the RollerCoaster!")
# height = int(input("Please input your height in cm to continue:\n"))
# name = str(input("How should we call you?\n"))
# bill = 0
#
# if height >= 120:
#
#     print("Welcome! " + name)
#     age = int(input("Please stage your age to proceed:\n"))
#     if age <= 5:
#         print("You are too young for this!")
#         exit()
#     elif age <= 10:
#         bill = 200
#         print("You will pay KES200.")
#     elif age <= 15:
#         bill = 300
#         print("You will pay KES300.")
#     elif age <= 20:
#         bill = 500
#         print("You will pay KES500.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be fine. Get a free ride!")
#     else:
#         bill = 700
#         print("Pay KES700.")
#
#     wants_photos = input("Do you want your photo taken? answer with Y or N \n")
#     if wants_photos == "y":
#         bill += 3
#         print(f"Your Total bill now is KES{bill}")
#     else:
#         print(f"Your Total bill now is KES{bill}")
# else:
#     print("You need to grow first bud.")

#################################################################################
# Even / Odd check
#################################################################################


# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# check = number % 2
#
# if check == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

#################################################################################
# BMI 2.0
#################################################################################


# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# bmi = weight/(height**2)
# bmi_rounded = round(bmi, 0)
# bmi_int = int(bmi_rounded)
#
# if bmi_rounded < 18.5:
#     print(f"Your BMI is {bmi_int}, you are underweight.")
# elif bmi_rounded < 25:
#     print(f"Your BMI is {bmi_int}, you have a normal weight.")
# elif bmi_rounded < 30:
#     print(f"Your BMI is {bmi_int}, you are slightly overweight.")
# elif bmi_rounded < 35:
#     print(f"Your BMI is {bmi_int}, you are obese.")
# else:
#     print(f"Your BMI is {bmi_int}, you are clinically obese.")

#################################################################################
# LEAP YEAR CHECKER
#################################################################################

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# div_by4 = year % 4
# div_by100 = year % 100
# div_by400 = year % 400
#
#
# if div_by4 == 0 or div_by100 == 1 and div_by400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

#################################################################################
# automatic pizza order program.
#################################################################################

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# bill = 0
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
# elif size == "L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}")

#################################################################################
# testing the compatibility between two people
#################################################################################

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# name1_to_lower = name1.lower()
# name2_to_lower = name2.lower()
# T = name1_to_lower.count("t") + name2_to_lower.count("t")
# R = name1_to_lower.count("r") + name2_to_lower.count("r")
# U = name1_to_lower.count("u") + name2_to_lower.count("u")
# E = name1_to_lower.count("e") + name2_to_lower.count("e")
#
# L = name1_to_lower.count("l") + name2_to_lower.count("l")
# O = name1_to_lower.count("o") + name2_to_lower.count("o")
# V = name1_to_lower.count("v") + name2_to_lower.count("v")
# E = name1_to_lower.count("e") + name2_to_lower.count("e")
#
# true = T + R + U + E
# love = L + O + V + E
#
# true_to_string = str(true)
# love_to_string = str(love)
# score = true_to_string + love_to_string
# score_to_int = int(score)
#
# if score_to_int < 10 or score_to_int > 90:
#     print(f"Your score is {score_to_int}, you go together like coke and mentos.")
# elif 40 <= score_to_int <= 50:
#     print(f"Your score is {score_to_int}, you are alright together.")
# else:
#     print(f"Your score is {score_to_int}.")

#################################################################################
# automatic pizza order program.
#################################################################################

