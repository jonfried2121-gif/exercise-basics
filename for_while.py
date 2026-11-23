import random

#1
# count = 1
# while count <11:
#     print(count)
#     count += 1

#2
# count = 10
# while count !=0:
#     print(count)
#     count -= 1
# print("strart!!")

#3
# count = 1
# while count <= 50:
#     if count % 2 == 0:
#         print(count)
#     count += 1

#4
# num = int(input("enter a number"))
# for i in range(1,6):
#     print(num * i)
#5
# count = 0
# for i in range(101):
#     count += i
# print(count)

#6
# fla = True
# password = "Python123"
# while fla:
#     user = input("enter password: ")
#     if password == user:
#         fla = False
# print("welcom")

#7
# secret_number = 27

# flag =True
# while flag:
#     nnumber = int(input("enter a  umber : "))
#     if nnumber == secret_number:
#         flag = False
# print("succes")


#8
# flag = True
# count = 0
# while flag:
#     numner = int(input("enter a  umber : "))
#     if numner == 0:
#         flag = False
#     else:
#          count += numner
# print(count)

#9
# count_grades =0
# sum_graddes = 0
# avg =0
# flag = True
# while flag:
#     grade = int(input("enter a  grade : "))
#     if grade == 999:
#         flag = False
#     else:
#         count_grades+=1
#         sum_graddes += grade
# print("the number of grdes is : ",count_grades)
# print( "the sum of grddes is:",sum_graddes)
# print("the average is: ",sum_graddes / count_grades)

#11
# num = int(input("enyer a number "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")
    
#12
# number = int(input("enyer a number "))
# count = 0
# while number != 0:
#     count += 1
#     number = number // 10
# print(count)

#13
# number = int(input("enter a number "))
# new_num= 0
# while number != 0:
#     new_num = new_num *10 + number % 10
#     number = number //10
# print(new_num)

#14
# number = int(input("enter a number "))
# count = 2
# flag = True
# while count < number and flag:
#     if number % count == 0:
#         print("is nor first")
#         flag = False
#     else:
#         count += 1
# if flag:
#     print("is first")

#15
# balance = 5000
# flag = True
# while flag:
#     pick = input("""1. see balance
# 2.deposit
# 3.withdraw
# 4.exit""")
#     if pick == "1":
#         print(balance)
#     if pick == "2":
#         number = int(input("enter money to deposit: "))
#         if number < 0:
#             print("number has to be positive")
#         else:
#             balance += number
#             print("deposit succesfully")
#     if pick == "3":
#         number = int(input("enter money to withdraw: "))
#         if number < 0 or number > balance:
#             print("number has to be positive")
#         else:
#             balance -= number
#             print("you withdrawed: ",number)
#     if pick == "4":
#         flag = False

#16
# count = 1
# while True:
#     if count == 15:
#         break
#     print(count)
#     count +=1 

#17
# count = 1
# while count < 30:
#     if count % 3 == 0:
#         count += 1
#         continue
#     else:
#         print(count)
#         count +=1

#18
# while True:
#     number = int(input("enter a number "))
#     if number == 100:
#         print("succes")
#         break

#19
# for i in range(1,21):
#     print(i)
    
#20
# for i in range(0,101,5):
#     print(i)

#21
# count = 0
# for i in range(101):
#     count += i
# print(count)
    
#22
# num = int(input("enyer a number "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

#23
# n1=   int(input("enyer a number "))
# n2 =  int(input("enyer a number "))
# count = 0
# for i in range(n1,n2+1):
#     count += i
# print(count)

#24
# for i in range(100):
#     if i % 3 == 0 and i % 5== 0:
#         print(i)

#25
row =  int(input("enyer a number of rows "))
collum =  int(input("enyer a number of soluum "))

for i in range(row):
    for j in range(collum):
        print("*",end="")
    print()

#26
# for i in range(1,7):
#     for j in range(i):                                                                
#         print("*",end="")
#     print()

#27
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")
    
#28
# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i}, {j}")
    
flag = True
while flag:
    print("""===== MATH GAME =====

1. Start Game
2. View Instructions
3. Exit

Choose:
""")
    pick = input("enter a number: ")
    if not pick: 
        continue
    if pick == "1":
        count = 0
        for i in range(1,10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            ans = int(input(f"{num1} + {num2} ="))
            if ans == num1+num2:
                count += 1
        print("answered right: ",count)

    if pick == "2":
        print("answer all 10 questions and get the sumerise at the end")

    if pick == "3":
        flag = False



