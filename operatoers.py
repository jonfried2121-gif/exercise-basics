#1
# num1 = 25
# num2 = 7
# print(f"""===== calculator =====
# add: {num1 + num2}
# sub: {num1- num2}
# mul : {num1 * num2}
# dev : {num1 / num2}
# round devide : {num1 // num2}
# modulu devide :{num1 % num2}
# power : {num1 ** num2} """)

#2
# balance = 1000
# print(balance)
# print(balance += 250)
# print(balance *= 2)
# print(balance /= 4)


#3
# price = int(input("enter product price: "))
# discount = int(input("enter discout: "))
# print(f"""discount = {price/ 100 * discount}
# total: {price + price /100 * discount}""")

#4
# amount = int(input("enter money amount: "))
# intrest = int(input("enter intrest amount: "))
# print(f"""intrest is: {amount / 100 * intrest}
# after oone year : {amount + amount / 100 * intrest}""")

#5
# grade1 = float(input("enter grade: "))
# grade2 = float(input("enter grade: "))
# grade3 = float(input("enter grade: "))
# avg = (grade1 + grade2 + grade3) / 3
# print("the average is: ",avg)

#6
# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print("Hello, my name is ",first_name," ",last_name, "and i live in ",city)
# print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")

#7
# full_name = input("enter full name: ")
# print(f"the name is: {full_name}, the lengt is {len(full_name)}, big letters: {full_name.upper()}, small letters: {full_name.lower()}")

#8
# full_sentece = input("enter a full scentence: ")
# print("only big letters: ",full_sentece.upper())
# print("only small letters: ",full_sentece.lower())
# print("with capitle letter: ",full_sentece[0:1].upper() + full_sentece[1:])

# print("evry word eith capital letter: ",full_sentece.title())

#9
# name = input("rnter name: ")
# before = len(name)
# name = name.strip()
# after = len(name)
# print("before clean: ",before)
# print("after clean: ",after)

#10
# sentence = "I love Java programming"
# sentence.replace("java", "python")
# number = sentence.count("love")
# strat_i = sentence.startswith("I")
# endswith_programing = sentence.endswith("programming")

#11
# word = "Programming"
# print(word[0])
# print(word[-1])
# print(word[2])
# print(word[0:3])
# print(word[-4:])
# print(word[::-1])

#12
# a = "100"
# b = "25"
# c = 10
# d = 5.5
# a =int(a)
# print("a: ",a," type: ",type(a))
# b = float(b)
# print("b: ",b," type: ",type(b))
# c = str(c)
# print("c: ",c," type: ",type(c))
# d = int(d)
# print("d: ",d," type: ",type(d))

#13
#age = input("Enter your age: ")
#print(age + 10) cannot make mathematical operators on string type

#14
# price = float(input("enter price before vat"))
# price *= 1.18
# print("the finall price is: ",price)

#15
# name = input("enter first name: ")
# last_name = input("enter last name: ")
# age = int(input("enter age: "))
# monthy_salary =  int(input("enter monthly salary: "))
# years = int(input("enter numbers of yers in job: "))

# print(f"""==== worker ====
# name : {name}
# family : {last_name}
# age {age}
# years in job: {years}""")

# print(f"""===== salary ====
# annualy salary: {monthy_salary * 12}
# afetr 5 %: {monthy_salary * 12 * 1.05}
# number of tav: {len(name+last_name)}""")

#16
# usd_rate = 3.25
# euro = 3.75
# fee =2
# shekel = int((input("enter sum in shekel: ")))
# print("dollars: ",shekel / usd_rate)
# print("euro: ",shekel / euro)
# print("dollar afetr fee: ",shekel / usd_rate * 0.98," euro after fee: ",shekel / euro * 0.98)

#17
# name = input("enter first name: ")
# last_name = input("enter last name: ")
# birth  =int(input("enter year of birth"))
# gmail= f"{name}.{last_name}.{birth}@gamil.com"
# print(gmail.lower())

#18
# scentence = input("enter a scentence: ")
# print(f""" ==== scentence review ====
# all sxentence: {scentence}
# length: {len(scentence)}
# big letters: {scentence.upper()}
# small letters: {scentence.lower()}
# reverse : {scentence[::-1]}
# number of a {scentence.count("a")}
# with slache: {scentence.replace(" ","/")}""")

#19
# def get_input(thing):
#     object = input(f"please enter {thing}: ")
#     return object

# name = get_input("costumer name")
# product = get_input("priduct").upper()
# price = int(get_input("product price"))
# quantity = int(get_input("quantity"))
# total = price * quantity
# discount = int(get_input("discount percent"))
# with_discount = total-(total/100 * discount)
# vat = int(get_input("vat percent"))
# print(f"""==== BILL ====
# name: {name}
# product: {product.upper()}
# price per unit: {price}
# quantity: {quantity}
# subtotal: {total}
# total: {with_discount}
# vat: {vat}
# vat amount : {total* discount / 100 /100 * vat}
# with vat: {with_discount + (with_discount /100 * vat)}
# ============================
#    TANK YOU FOR SHOPPING
# ============================
# """)
