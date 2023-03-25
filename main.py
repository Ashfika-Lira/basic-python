# import cv2
# import math

# print("Hello World\n")
# print(math.gcd(3,6))
# print(5+7)
# print(5-7)

''' 
This is a multi line comment
This is a multi line comment
This is a multi line comment

'''
""" 
This is also a multi line comment
This is also a multi line comment
This is also a multi line comment

"""

# if(age<18) :
#     print('hello') 

a = 56
b = "Ashfi"
c = 78.65
d = 2

""" print(a + c)
print(a + d)
print(a - d)
print(a * d)
print(a / d) """
# print(a ** d)
# print(c // a)
# print(a % d)

# Quiz: Try these operators:
# 1. ** Exponentiation operator
# 2. // Floor division operator
# 3. %  Modulo operator

# Wrong syntax
# harry project = 45 
# Rules for creating variables

# 1. variable should start with a letter or an underscore
# 2. variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensitive. Harry and harry are two different variables

# typeA = type(a)
# typeB = type(b)
# print(typeA)
# print(typeB)
e = '31'
# e = 3.14
# e = int(31)
# e = int(e)
e = float(e)
# e = str(489)
# e = int("56")
# print(type(e))
# print(e)
# print(e+3)
a = float(a)
a = str(a)
# print(a)

# name = '''Lira
# is a good girl'''
name = "Lira"
name1 = "Lira, Ariana, Insiya"
# print(name)
# print(name[0])
# print(name[0:2])
name2 = "     Anaya     "
""" print(name2)
print(name2.strip())
print(len(name)) """
var = name.lower()
var = name.upper()
var = name.replace("r", "y")
var = name.replace("ra", "y")
var = name1.replace(",", '')
var = name1.replace(", ", '\n')

# print(var)

stri = "This is a "
name3 = "Ela"
name4 = "Alfiya"
stri1 = "This is not a"
# print(stri + stri1)
temp = "This is a {} and he is a good boy named {}".format(name3, name4)
temp = "This is a {1} and he is a good boy named {0}".format(name3, name4)
temp = f"this is a {name3} and he is a good boy named {name4}"
temp = f"this is a {name4} and he is a good boy named {name3}"
# print(temp)

'''
Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary

'''
# List
lst = [81, 2, 3, 4, 6, 41 ]
# var = type(lst)
# lst[3] = 61
# var = lst[3]
# lst.append(100)
# lst.insert(1,100)
# lst.remove(61)
# lst.pop()
# del lst[3]
# del lst
lst.clear()
var = lst
# var = len(lst)
# var = lst[1:4]
# print(lst)
# print(var)


# Tuple
a = ("Harry", "Shubh", "Rohan")
var = a
a = list(a)
var = type(a)
# Cannot do this
a[0] = "Vikrant"
# print(var)
# print(a)

# Set
s1 ={23, 3, 5, 6, 8, 2, 3, 6, 8, 10, 3, 4, 12,}
# s1.add(44444)
# s1.update([12, 12, 345, 6789, 1233, 34567])
# print(len(s1))
s1.remove(12)
s1.discard(1672)
s1.pop()
s1.clear()
# del s1
# Using the intersection() method
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
# print(intersection_set)
# s1.remove(152) --- error
# Using the union() method
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
# print(union_set)
# .pop, .clear, del, intersection, union
# print(s1)

# dictionary
harryDict = {
    "Name": "Harry",
    "Class": "6th",
    "Marks": 56.88,
    "Hours in school": 6
}
# harryDict["Marks"] = 73
# print(harryDict)
harryDict["Marks"] = 73
# print(harryDict["Marks"])
harryDict.pop("Marks")
# del, clear, update
# print(harryDict)


# age = 34
# age = input("Enter Your Age\n")
# print(age)
# age = int(age)
# print(type(age))
# if(age>18):
#     print("You can drive a car")

# elif(age==18):
#     print("You are an awesome teen")

# else:
#     print("You cannot drive")

# Loops:
# Scenario: you have to print numbers between 1 to 1000
# for i in range(0, 1000):
#     print(i)

# li = [1, 432, "this"]
# for item in li:
#     print(item)
# # Quiz: Use for loop to iterate dictionary, set and tuples  
# i = 0
# while(i<100):
#     # print(i)
#     i = i + 1
#     if i == 78:
#         break
#         continue
#     print(i+1)

# Functions:
# def greet():
#     print("Good morning sir")
#     print("Good morning mam")
#     print("Good morning Uncle")

# greet()     
     

# def sum(a, b):
#     print("Running sum")
#     c = a + b
#     return c

# d = sum(34, 45)
# print(d)

class Employee:
    def __init__(self, gname, gsalary):
        self.name = gname
        self.salary = gsalary

harry = Employee("harry", 34)
print(harry.name)
print(harry.salary)
