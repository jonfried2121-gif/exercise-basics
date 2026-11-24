#1
# def say_hello():
#     print("wello")

# say_hello()
# say_hello()
# say_hello()

#2
# def show_welcome():
    # print("welcome to system")

#3
# def show_menu():
#     print("""=== main menu ===
# 1. start
# 2.settings
# 3. exit""")

#4
# def show_numbers():
#     for n in range(1,11):
#         print(n, end=" ")

#5
# def show_even_numbers():
#     for i in range(2,100,2):
#         print(i)

#6
# def show_stars():
#     for i in range(1,6):
#         for j in range(1,11):
#             print("*",end=" ")
#         print()
# show_stars()

#7
# def greet(name):
#     print("Hello", name)
# greet("David")
# greet("Moshe")

#8
# def show_age(age):
#     print("the user is ",age," years old")
# show_age(7)


#9
# def calculate_sum(n1,n2):
#     print("the sum is: ",n1 +n2)
# calculate_sum(3,5)

#10
# def calculate_average(n1,n2,n3):
#     summ = n1+n2+n3
#     print(summ/ 3)
#11
# def check_even(num):
#     if num % 2 == 0:
#         print("is even")
#     else:
#         print("not even")

#12
# def check_password(password):
#     if password == 123456:
#         print("acces granted")
#     else:
#         print("acses denied")

#13
# def calculate_discount(price, persent):
#     print(price - price *persent/ 100)

#14
# def show_range(n1,n2):
#     for i in range(n1+1,n2):
#         print(i,end=" ")

#15
# def print_rectangle(high,width):
#     for i in range(high):
#         for j in range(width):
#             print("*", end = " ")
#         print()

#16
# def multiply(n1,n2):
#     return n1 * n2

#17
# def get_full_name(first,last):
#     return first + " " +last 

# a=get_full_name("mordi", "shtoolz") 
# print(a)

#18
# def get_max(n1,n2):
#     if n1 > n2:
#         return n1   
#     return n2

#19
# def is_positive(n):
#     return n > 0

#20
# def calaulate_tax(price, tax):
#     return price + price * tax/100

# print(calaulate_tax(200,17))

#21
# def get_grade_status(grade):
#     if grade > 90:
#         return "EXCELLENT"
#     if grade > 75:
#         return "Good"
#     if grade > 60:
#         return "Average"
#     return "Failed"
#22
# def count_digits(number):
#     count = 0
#     while number:
#         number = number // 10
#         count += 1
#     return count
# print(count_digits(345))

#23
# def calculate_power(num,p):
#     total =1
#     for i in range(p):
#         total *= num
#     return total

# print(calculate_power(2,3))
#24
# def print_list(lll):
#     for l in lll:
#         print(l,end=" ")
#25
# def get_list_sum(lll):
#     summ = 0
#     for i in lll:
#         summ += i
#     return summ
#26
# def get_list_average(arr):
#     summ = 0
#     for a in arr:
#         summ += a
#     return summ / len(arr)
#27
# def find_number(arr,n):
#     for a in arr:
#         if a == n:
#             return True
#     return

#28
# def find_max(arr):
#     maxx =0
#     for a in arr:
#         if a > maxx:
#             maxx = a
#     return maxx

#29
# def get_even_numbers(arr):
#     zoog = [num for num in arr if num % 2 == 0]
#     return zoog
# print(get_even_numbers([1,22,32,4,345,6,67,88]))

#30
# def get_long_names(arr):
#     long = [name for name in arr if len(name) > 4]
#     return long

#31
# def reverse_list(arr):
#     return arr[::-1]
#32
# def count_occurensies(arr:list,n):
#     numbers = arr.count(n)
#     return numbers
# print(count_occurensies([1,1,1,2,32,1],1))
#33
# def remove_duplicates(arr):
#     new =[]
#     for n in arr:
#         if n not in new:
#             new.append(n)
#     return new
#34
# def calculate_final_price(price,persent):
#     final = price - price * persent /100
#     return more_5(final)

# def more_5(price):
#     if price > 500:
#         return price *0.95
#     return price
# calculate_discount(600,10)

#35
# def check_list(arr):
#     return zoogie(arr),even(arr),sum(arr)
# def zoogie(arr):
#     return len([n for n in arr if n % 2 == 0])

# def even(arr):
#     return len([n for n in arr if n%2 != 0])

# print(check_list([1,2,3,4,5,6,7,8]))

#36
# def analyze_grade(grades):
#     return f"average:{average(grades)}, best:{best(grades)}, worst: {worst(grades)}, passed: {passed(grades)}"
# def average(grades):
#     return sum(grades) / len(grades)
# def best(grades):
#     return max(grades)

# def worst(grades):
#     return min(grades)

# def passed(grdaes):
#     return len([n for n in grdaes if n > 60])

# print(analyze_grade([78,34,99,78,50,56,96]))

#37
# def validate_user(name,password):
#     return not is_empty(name) and long(password)

# def is_empty(name):
#     return name.strip() == ""

# def long(password):
#     return len(password) >= 6

# print(validate_user("v","fdsjjj"))

#38
# students = [    {"name": "David", "grade": 90},    {"name": "Moshe", "grade": 75},    {"name": "Dana", "grade": 100}]

# def search_students(arr,name):
#     for student in arr:
#         if student["name"] == name:
#             return student
#     return

#39
# cart = [    {"name": "Laptop", "price": 4500, "quantity": 1},    {"name": "Mouse", "price": 80, "quantity": 2},    {"name": "Keyboard", "price": 150, "quantity": 1}]

# def calculate_total_cart(arr):
#     summ =0
#     for product in arr:
#         summ += product["price"] * product["quantity"]
#     return summ
# print(calculate_total_cart(cart))

#40
# def get_fibonnaci(n):
#     fib = [0,1]
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     for i in range(2,n):
#         fib.append(fib[i-2]+fib[i-1])
#     return fib.pop()
# print(get_fibonnaci(7))

#41,42,43
# number = 12
# def plus_10():
#     global number
#     number += 10
# plus_10()
# print(number)

#44
# arr = [1,2,3,4,5]
# def add_list():
#     arr.append(66)
# add_list()
# print(arr)

#45
# arr =[1,23,4,5,6]
# def change_list(arr):
#     new = arr[:]
#     new.append(88)
#     return new
# a=change_list(arr)
# print(arr)
# print(a)

#project
# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]


# def show_menu():
#     print("""===== Student Management =====
    
# 1. Show all students
# 2. Add student
# 3. Search student
# 4. Update student grade
# 5. Remove student
# 6. Show passing students
# 7. Show class statistics
# 8. Show students above average
# 0. Exit
#     """)
#     return

# def show_all_students():
#     for student in students:
#         print(student["name"]," ",student["age"]," ",student["grade"])

# def add_student(name,age,grade):
#     if search_students(name):
#         new = {"name":name,"age":age,"grade":grade}
#         students.append(new)
#         return
#     return

# def search_students(name):
#     for student in students:
#         if student["name"] == name:
#             return student
#     print("not found")
#     return

# def updrde_grade(name,grade):
#     for student in students:
#         if student["name"] == name:
#             student["grade"] == grade
#             print("grade updated")
#             return
#     print("not found")
#     return

# def remove_student(name):
#     for student in students:
#         if student["name"] == name:
#             students.remove(student)
#             print("student removed")
#             return
#     print("not found")
#     return

# def get_passing_students():
#     passed = [n["name"] for n in students if n["grade"] > 60]
#     return passed

# def get_average():
#     summ = 0
#     for n in students:
#         summ += n["grade"]
#     return summ / len(students)

# def get_heighest_grade():
#     maxx =0
#     for n in students:
#         if n["grade"] > maxx:
#             maxx = n["grade"]
#     return maxx

# def show_statistics():
#     print(f"""passing students: {get_passing_students()}
# average: {get_average()}
# highest grade: {get_heighest_grade()}""")
#     return

# def above_average():
#     above = []
#     avg = get_average()
#     for n in students:
#         if n["grade"] > avg:
#             above.append(n["name"])
#     return above

# flag = True
# while flag:
#     show_menu()
#     pick = input("enter a number: ")
#     if pick == "1":
#         show_all_students()
#     if pick == "2":
#         name = input("enter name: ")
#         age  = int(input("enter age: "))
#         grade = int(input("enter grdae: "))
#         add_student(name,age,grade)

#     if pick == "3":
#         name = input("enter name: ")
#         print(search_students(name))

#     if pick =="4":
#         name = input("enter name: ")
#         grade = int(input("enter grade: "))
#         updrde_grade(name,grade)

#     if pick == "5":
#         name = input("enter name: ")
#         remove_student(name)

#     if pick == "6":
#         print(*get_passing_students())

#     if pick == "7":
#         show_statistics()

#     if pick == "8":
#         print(*above_average())
#     if pick == 0:
#         flag = False

