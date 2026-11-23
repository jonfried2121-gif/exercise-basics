#1
# age = int(input("enter yoyr age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

#2
# number = int(input("enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

#3

# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

#4
# number1 = int(input("enter a number: "))
# number2 = int(input("enter a number: "))
# if number1 > number2:
#     print(number1," is bigger")
# elif number2 > number1:
#     print(number1," is bigger")
# else:
#     print("Equal")

#5
# password = "Python123"
# user_input = input("enter password: ")
# if user_input == password:
#     print("Acsses Granted")
# else:
#     print("Acsses Denied")

#6
# number = int(input("enter a number: "))
# if 1 < number < 10:
#     print("1- 10")
# elif 10 < number < 51:
#     print("10-50")
# elif 50 < number < 101:
#     print("50 -100")
# else:
#     print("out of bounds")

#7
# grade = int(input("enter a grade betweem 0 - 100 : "))
# if 90 < grade < 101:
#     print("excellent")
# elif 89 < grade < 91:
#     print("Very Good")
# elif 79 < grade <81:
#     print("Good")
# elif 59  <grade < 71:
#     print("Passed")
# elif  0 < grade < 60 :
#     print("Failed")
# else:
#     print("invalild grade")

#8
# correct_username = "admin"
# correct_password = "123456"
# username = input("enter username: ")
# password  = int(input("enter password: "))
# if correct_username == username and password == correct_username:
#     print("login succesfuly")
# elif correct_username == username and password != correct_password:
#     print("wrong passoword")
# else:
#     print("unknown user")

#9
# age = int(input("enter age: "))
# price = int(input("enter product price: "))
# if age > 60:
#     price *= 0.80
#     print("price is ",price)
# elif age <18:
#     price *= 0.90
#     print("price is ",price)
# else:
#     print("no discount")

#10
# number = int(input("enter a number: "))
# if number % 15:
#     print("devide in 3 and 5")
# elif number %3 == 0 and number %5 !=0:
#     print("the number devides in three")
# elif number % 5 == 0 and number % 3 != 0:
#     print("the number devides in five")

# #11
# age = int(input("enter age: "))
# grown_up = bool(input("if you are escorted by a grown up:"))
# if age >=16 and grown_up:
#     print("can acces")
# elif age >= 18:
#     print("can acces")
# else:
#     print("acces denied")
# #12
# average= int(input("enter your average: "))
# income = int(input("enter your income"))
# if average > 90:
#     print("entitle to scolharship")
# elif average > 85 and income < 5000:
#     print("entitle to scolharship")
# else:
#     print("not entitled")

# 13

# correct_username = "admin"
# correct_password = "123456"
# active = bool(input("enter if the account is active : "))
# username = input("enter username: ")
# password  = input("enter password: ")
# if correct_username == username and password == correct_username and active:
#     print("login succesfuly")
# elif correct_username == username and password != correct_password:
#     print("wrong passoword")
# elif username != username:
#     print("unknown user")
# elif not active:
#     print("the account is not active")
#14
# n1 = int(input("enter a number: "))
# if 20 <= n1 and n1 <= 80:
#     print("is in range")
# else:
#     print("not in range")

# if not (n1 < 20 or n1 > 80):
#     print("in range")
# else:
#     print("not in range")

#15
# balance = int(input("enter balance : "))
# withdraw = int((input("enter price to withdraw ")))
# bank = 12333
# if balance > 0:
#     if balance < withdraw:
#         print("cant do withdraw")
#     else:
#         print("can withdraw")
# else:
#     print("error the sum is not positive")

#16
# age = int(input("enter age: "))
# member = input("enter if you are a member: ")
# if age < 14:
#     price  = 25
# elif age < 18:
#     price = 35
# else:
#     price = 50

# if member:
#     price *= 0.90
# print("the price is ",price)

#17
# age = int(input("enter age: "))
# oncome = int(input("enter income: "))
# time = int(input("how much time are you working: "))
# if age >=21 and oncome >= 7000 and time >= 1:
#     print("entitled to loan")
# if age < 21:
#     print("no valid age")
# if oncome <7000:
#     print("invalid income")
# if time < 1:
#     print("invalid time in job")


#18
# vehicle = input("enter your vehicle: ")
# time = int(input("how much time are you parking: "))
# if vehicle == "bike":
#     price = 10 * time
# elif vehicle == "car":
#     price = 20 * time
# else:
#     price = 30 * time
# if time <5:
#     price *= 0.90
# elif time >= 5:
#     price *= 0.85

# print("the final price is: ",price)

# n1 = int(input("enter a number: "))
# n2 = int(input("enter a number: "))
# operator = input("enter operator: ")
# if operator == "+":
#     res = n1 + n2
# elif operator == "-":
#     res = n1 - n2
# elif operator == "*":
#     res = n1 * n2
# elif operator == "/":
#     if n2 != 0: 
#         res = n1 / n2
#     else:
#         res = "error the second number is 0"
# else:
#     res = "no valid operator"

# print(res)
#20
# year = int(input("enter year: "))
# if year % 400 == 0:
#     print("meuberet")
# elif year % 100 == 0:
#     print("not meuberet")
# elif year % 4 == 0:
#     print("meuberet")
# else:
#     print("not meuberet")




#21
# hours = int(input("enter work hours: "))
# if hours < 182:
#     salary = 50 * hours
# else:
#     extra=  hours - 182
#     if extra <= 2:
#         salary = 50 * 182 + extra * 50 * 1.25
#     else:
#         salary = 50 * 182 + extra * 50 * 1.50
# print("the salary is : ",salary)

#project
# def get_input(thing):
#     user_input = input(f"enter {thing}: ")
#     return user_input

# age = int(get_input("age"))
# purchas = int(get_input("purchas"))
# member = get_input("if member")
# open = get_input("if the product is open")
# recit = get_input("if there is recit")
# days = int(get_input("how much days passed"))

# if recit:
#     if  not open:
#         if purchas > 0:
#             if member:
#                 if days < 30 :
#                     print("returned")
#                 else:
#                     print("it is too late")
#             else:
#                 if days < 14:
#                        print("returned")
#                 else:
#                     print("it is too late")
#         else:
#             print("purchas has to be positive")
#     else:
#         print("cant return an open product")
# else:
#     print("cant return with no recit")



