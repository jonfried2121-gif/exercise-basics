#1
# numbers = (10,20,30,40,50)
# print(numbers)
# print(numbers[0],numbers[-1])
# print(len(numbers))
# print(numbers[2])

#2
# students = ("shlomi","avi","hanan","itamar","ronen")
# for student in students:
#     print(student)
# name = input("enter a name to search: ")
# if name in students:
#     print("found moshe")
# else:
#     print("not found")
# print(len(students))

#3

# numbers = (10,20,30,40,50)
# print(*numbers[:3])
# print(*numbers[-3:])
# print(*numbers[::-1])

#4,5
# product=("milk",23,56,"groceries")
# print("the productis: ",product[0])
# print("the price is: ",product[1])
# print("hte quantity is: ",product[2])
# print("the category is: ",product[-1])

#6
# summ =0 
# numbers = (10,20,30,40,50)
# maxx = numbers[0]
# zoog  =0
# for num in numbers:
#     summ += num
#     if maxx < num:
#         maxx = num
#     if num % 2 == 0:
#         zoog += 1
# print("the sum of all numbers is: ",summ)
# print("the biggest number is: ",maxx)
# print("the number of even numbers is: ",zoog)

#7
# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# first_three = products[0:3]
# last_two = products[-2:]
# new = first_three + last_two
# print(*new)

#7
# students={"name":"yakov","age":23,"grade":89,"city":"tlv"}
# for key,val in students.items():
#     print(key, val)
#8
# car = {"brand":"volvo","model":"xf22","year": 2025,"price":123000}
# car["price"] = 430000
# car["year"] = 2026
# car["color"] = "black"
# for key,val in car.items():
#     print(key,val)

#9
# salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
# for key,val in salaries.items():
#     print(key,val)
# salaries["Dana"] =1200
# salaries["jon"] = 34400
# for key,val in salaries.items():
#     print(key,val)

#10
# items = {    "huose": 12000,    "car": 15000,    "necklas": 13500}
# search = input("enter an item to search: ")
# flag = False
# for key in items:
#     if key == search:
#         flag = True
# if flag:
#     print("the price is: ",items[search])
# else:
#     print("not found")

#11
# grades = {    "David": 91,    "Moshe": 59,    "Dana": 93, "catz":84,"shtoolie":96}
# for key, val in grades.items():
#     print("Student: ",key," | ",val)

#12
# grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
# summ =0
# maxx = 0
# name =""
# fail  =0
# for key,val in grades.items():
#     if grades[key] >= 80: 
#         print(key,val)
#     elif grades[key] < 60:
#         fail += grades[key]
#     if val > maxx:
#         maxx = val
#         name = key
#     summ += grades[key]
# print("the best score is: ",name)
# print("the number of fails is: ",fail)
# print("the sversge is : ",summ / len(grades))
    
#13
# items = {    "huose": 12000,    "car": 15000,    "necklas": 13500}
# search = input("enter item to serach: ")
# update = input("entre your new price: ")
# items[search] = update
# for key ,val in items:
#     print(key,val)

#14
students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# summ = 0
# maxx = 0
# for dic in students:
#     print(dic["name"])
# for dic in students:
#     print(dic["grade"])
#     summ += dic["grade"]
#     if maxx< dic["grade"]:
#         name = dic["name"]
#         max = dic["grade"]
# print("the average is : ",summ / len(students))
# print("the highest score is: ",name)

#15
# students.append({"name":"noam","age":22,"grdae":88})
# students[1]["grade"] = 10
# name = input("enyer a name to remove: ")
# for student in students:
#     if student["name"] == name:
#         students.remove(student)
# print(students)

#16
# classroom = {    "Class A": ["David", "Moshe", "Dana"],    "Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
# for clas in classroom:
#     print(clas)
# for student in classroom["Class A"]:
#     print(student)
# classroom["Class B"].append("omer")
# classroom['Class C'].remove("Shir")
# print(len(classroom["Class A"]),len(classroom["Class B"]),len(classroom["Class C"]))

#17
# products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
# for product in products:
#     print(products[product]["price"],end=" , ")
#     print(products[product]["stock"])
# products["Laptop"]["stock"]+= 1
# products["pc"] ={"price": 230,"stock":20}
# for product in products:
#     if products[product]["price"] > 100:
#         print(products[product])

#18
# employees = [    ("David", "Development", 15000),    ("Moshe", "Marketing", 12000),    ("Dana", "Development", 18000),    ("Noa", "HR", 11000)]
# for employe in employees:
#     print(employe[0], end=" ")
# maxx = 0
# name =""
# summ= 0
# for employe in employees:
#     summ += employe[2]
#     if employe[2] > maxx:
#         maxx = employe[2]
#         name = employe[0]
#     if employe[1] == "Development":
#         print(employe)
# print("the highest paid worker is: ",name)
# print("the average salary is: ",summ / len(employees))

#19
# inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
# name = input("enter a product to search: ")
# quantity = int(input("enter quantity: "))
# if name not in inventory:
#     print("not found")
# else:
#     inventory[name] = quantity
# print(inventory[name])

#20
# votes = {    "David": 0,    "Moshe": 0,    "Dana": 0}
# flag = True
# while flag:
#     vote = input("enter name you want to vote to write stop to stop: ")
#     if vote in votes:
#         votes[vote] += 1
#     else:
#         if vote == "stop":
#             flag = False
#         else:
#             print("no such candidte")
# maxx =0
# name = ""
# for vote in votes:
#     if votes[vote] > maxx:
#         maxx = votes[vote]
#         name = vote
# print("the winner is: ",name)

# phones = {"david": "0524547107","yael":"0586300888","shtoolz":"8988643875"}
# flag = True
# while flag:
#     print("""1.add contact
# 2. search contact
# 3. update contact
# 4. delete comtact
# 5. show all contact
# 6.exit""")
#     pick = input("choosea number: ")
#     if pick == "1":
#         new = input("enter new name: ")
#         number = input("enter new phone number: ")
#         phones[new] = number

#     if pick == "2":
#         name = input("enter name: ")
#         if name in phones:
#             print(name," | ",phones[name])
#         else:
#             print("contact not found")

#     if pick == "3":
#         name = input("enter name: ")
#         if name in phones:
#             number  = input("enter new number: ")
#             phones[name] = number
#             print("contact updated")
#         else:
#             print("contact not found") 

#     if pick == "4":
#         name = input("enter name: ")
#         if name in phones:
#             phones.pop(name)
#             print("contact deleted")
#         else:
#              print("contact not found")

#     if pick == "5":
#         for key, val in phones.items():
#             print(key," | ",val)

#     if pick == "6":
#         flag = False

#project
# products = [    {"name": "Laptop", "price": 4500, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 50},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]

# flag = True
# while flag:
#     print("""===== Store Management =====

# 1. Show all products
# 2. Add product
# 3. Search product
# 4. Update product price
# 5. Update product stock
# 6. Sell product
# 7. Show products by price
# 8. Show products with low stock
# 9. Show total inventory value
# 0. Exit
# """)
#     pick = input("choose a number: ")
#     if pick == "1":
#         for product in products:
#             print(product["name"]," ",product["price"]," ",product["stock"])

#     if pick == "2":
#         new = input("enter product name")
#         price = int(input("enter price: "))
#         stock = int(input("enter stock: "))
#         new = {"name":new,"price":price,"stock":stock}
#         products.append(new)
#         print("item added")

#     if pick == "3":
#         new = input("enter product name")
#         name = [p["name"] for p in products]
#         if new not in name:
#             print("not found")
#         else:
#             data = [p for p in products if p["name"] == new]
#             data = iter(data)
#             product = next(data)
#             print(product)

#     if pick == "4":
#         new = input("enter product name: ")
#         price = int(input("enter price: "))
#         products_name = [p["name"] for p in products]
#         if new not in products_name:
#             print("not found")
#         else:
#             for p in products:
#                 if p["name"] == new:
#                     p["price"] = price
#                     print("product updated")

#     if pick == "5":
#         new = input("enter product name: ")
#         stock = int(input("enter stock: "))
#         products_name = [p["name"] for p in products]
#         if new not in products_name:
#             print("not found")
#         else:
#             for p in products:
#                 if p["name"] == new:
#                     p["stock"] = stock
#                     print("product updated")

#     if pick == "6":
#         new = input("enter product name: ")
#         quantity = int(input("enter quantity: "))
#         products_name = [p["name"] for p in products]
#         if new not in products_name:
#             print("not found")
#         else:
#             for p in products:
#                 if p["name"] == new:
#                     if p["stock"] < quantity:
#                         print("not enough in stock")
#                     else:
#                         p["stock"] -= quantity
#                         print("product sold")

#     if pick == "7":
#         price = int(input("enter price to check: "))
#         more = [p for p in products if p["price"] > price]
#         print(more)

#     if pick == "8":
#         low = [p for p in products if p["stock"] < 10]
#         print(low)

#     if pick == "9":
#         summ = 0
#         for item in products:
#             summ+= item["stock"] * item["price"]
#         print(summ)

#     if pick == "0":
#         flag = False
        



        

