#1
# numbers =[10,20,30,40,50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])

#2
# students = ["avi","lolo","gad","yehuda"]
# print(len(students))
# print(students[0], students[-1])
# students[1] = "yael"
# print(*students)

#3
# grades =[88,93,83,90,55]
# grades.append(97)
# grades[2] = 78
# print(*grades)

#4
# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers.pop(0)
# print(*numbers)
# numbers.pop()
# print(*numbers)
# numbers.pop(2)
# print(*numbers)

#5
# products =["milk","table","chair","ball"]
# if "milk" in products:
#     print("milk is in products")
# if "computer" not in products:
#     print("computer is not in products")

#6
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     print(num)

#7
# for num in numbers:
#     if num %2 == 0:
#         print(num)

#8
# grades =[88,93,83,90,55]
# count = 0
# for grade in grades:
#     count += grades
# print(count)

#9
# numbers = [71,26,35,84,445,236,17,338,99,100]
# max = 0
# for num in numbers:
#     if num > max:
#         max = num
# print(max)

#10
# names = ["tzvi","avi","lolo","gad","yehuda"]
# for name in names:
#     if "shlomo" == name:
#         print("found")
# print("not found")

#11
# numbers = [71,26,35,84,445,236,17,338,99,100]
# num = int(input("enter a number: "))
# for i,n in enumerate(numbers):
#     if n == num:
#         print(i)

#12
# numbers = [71,26,35,84,445,236,17,338,99,100]
# count = 0
# for num in numbers:
#     if num > 50:
#         count += 1
# print("numbers of numbers bigger than 50 : ",count)

#13
# numbers = [71,26,35,84,445,236,17,338,99,100]
# even = []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
# print(*even)
    
#14
# names = ["tzvi","avi","lolo","gad","yehuda"]
# count =0
# while count < len(names):
#     print(count ,names[count])
#     count += 1


#15
# numbers = [71,26,35,84,445,236,17,338,99,100]
# print(*numbers[:3])
# print(*numbers[-3:])
# print(*numbers[2:7])
# print(*numbers[::-1])

#16
# names = ["tzvi","avi","lolo","gad","yehuda","shtooli","meir","shlomo","haim","yedidya"]
# for i in range(len(names)):
#     if i % 2 == 0:
#         print(names[i])

# for i in range(len(names)):
#     if i % 2 != 0:
#         print(names[i])
# print(*names[::-2])

#17
# numbers = [71,26,35,84,445,236,17,338,99,100,101,231,45,65,43,878,90,54,129]
# frist = numbers[:11]
# last = numbers[-10:]
# new = numbers[5:15]
# print(new)

#18
# numbers = [71,26,35,84,445,236,17,338,99,100]
# half1 = numbers[:len(numbers)//2]
# print(half1)
# half2 = numbers[len(numbers)//2:]
# print(half2)

#19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# multipy = [num *2 for num in numbers]
# power =[num**num for num in numbers]
# even = [num for num in numbers if num % 2== 0]
# odd = [num for num in numbers if num % 2 == 0 ]
# bigger5= [num for num in numbers if num > 5]

#20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# passed = [grade for grade in grades if grade > 60]
# failed = [grade for grade in grades if grade < 60]
# plus5 = [grade + 5 for grade in grades]

#21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# more_than_4 = [name for name in names if len(name) > 4]
# capital_letters = [name.upper() for name in names]
# start_with_d = [name for name in names if name.startswith("d")]

#22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new = [num for num in numbers if num % 3 == 0 and num > 10]

#23
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers)
# maxx = 0
# for num in numbers:
#     if num > maxx:
#         maxx = num
# print("the biggestnumber is: ",maxx)

# minn  =1000
# for num in numbers:
#     if num < minn:
#         minn = num
# print("the smallest number is: ",minn)

# summ =0
# for num in numbers:
#     summ += num
# print("aversge is: ",summ / len(numbers))

#24
# names = ["Moshe", "David", "Dana", "Noa", "Michael"]
# search = input("enterva name to search: ")
# if search in names:
#     names.remove(search)
#     print(*names)
# else:
#     print("name not found")

#25
# numbers = [12, 7, 25, 30, 9, 44, 18, 3,17,22]
# even = [num for num in numbers if num %2 ==0]
# odd = [num for num in numbers if num%2 != 0]
# bigger_than_20 = [num for num in  numbers if num > 20]

#26
# numbers = [12, 7, 25, 30, 9, 44, 18, 3,17,22]
# search = int(input("enter a number: "))
# summ = 0
# for i in range(len(numbers)):
#     if numbers[i] == search:
#         summ += 1
#         [print(i)]
# print("number of times the numbers appears: ",summ)

#27
# numbers1 = [12, 7, 25, 30, 9, 44, 18, 3,17,22]
# numbers2 = [98, 17, 2, 56, 99, 44, 14, 3,27,29]
# new = numbers1 + numbers2
# print(new)
# print(new[:6])
# print(new[-5:])
# print(new[::-1])

#28
# numbers = [98, 17, 2, 56, 99, 44, 14, 3,27,29]
# search = int(input("enter a number: "))
# flag = True
# for num in numbers:
#     if search == num:
#         flag = False
#         print("the number is in the list already")
# if flag:
#     numbers.append(search)
#     print(*numbers)

#project
grades = [85, 72, 90, 55, 100, 63, 48, 77]
flag = True
while flag:
    print("""===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
""")
    pick = input("enter you pick: ")
    if pick == "1":
        for n in grades:
            print(n)

    if pick == "2":
        grade = int(input("enter a new grade: "))
        grades.append(grade)

    if pick == "3":
        search = int(input("enter a grade to search: "))
        for i,n in enumerate(grades):
            if n == search:
                print(i)

    if pick == "4":
        grad = int(input("enter a grade to remove: "))
        sign  = True
        for grade in grades:
            if grade == grad:
                grades.remove(grade)
                sign = False
        if sign:
            print("number not found")

    if pick == "5":
        passed = [grade for grade in grades if grade > 60]
        print(*passed)

    if pick == "6":
        failed = [grade for grade in grades if grade < 60]
        print(*failed)

    if pick == "7":
        maxx = 0
        low = 101
        for grade in grades:
            if grade > maxx:
                maxx = grade
            else:
                if grade < low:
                    low = grade
        print("biggest : ",maxx)
        print("smallest : ",low)

    if pick == "8":
        summ = 0
        for grdae in grades:
            summ+= grdae
        print("average : ",summ / len(grades))

    if pick == "9":
        print(*grades[:3])

    if pick == "10":
        print(*grades[::-1])

    if pick == "0":
        flag = False





