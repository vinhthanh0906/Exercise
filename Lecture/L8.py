''' ----- L8 LIST OF LECTURE -------
- Walrus Operator :=
- Functions to variables (IMPORTANT)
- Higher order Function
- Lambda
- Sort
- Map
- Filter 
- Reduce
'''


#-----WALRUS OPERATOR----- 

'''
- New to Python 3.8
- Assignment expression aka walrus operator
- Assigns values to variables as part of a larger expression

'''

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)


# Use walrus function like a cable to connect input to a list

# foods = list()
# while food := input("What food do use like?: ") != "quit":
#     foods.append(food)






#----FUNCTION TO VARIABLES----
'''
- Similar to pointer in C or C++

'''
# def hello():
#     print("Hello")

# #print location of hello function in the memory
# print(hello)
# # No ()
# # Sharing the memory of hello to hi()
# hi = hello
# print(hi)

#Sharing a memory
# say = print
# say("I can print without print")




#----- HIHGER ORDER FUNCTION -------
'''
- a fucntion that either:
    + accepts a function as an argument
                or
    + return a function (In python, function are also treated as object)
'''

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def hello(func):
#     text = func("Hello")
#     print(text)

# #Hello is higher funtion
# hello(loud)
# hello(quiet)

# 
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend

# divide = divisor(2)
# print(divide(10))





#----LAMBDA----
'''
- Functin written in 1 line using lmabda keywoed 
accept any number of arguments, but only has one expression.

- Think is as a shortcut 
- USeful if need for a short period of time, throw-away



Formula: lambda expression : expression 

'''

# Function way 

# def fucn(x):
#     return  x * 2

# print(fucn(5))


#Lmambda way

# double = lambda x:x *2
# multiply = lambda x,y,z : x * y + z

# # Can have string arguments
# name  = lambda first_name, last_name: first_name + last_name

# #Use with conditional statement
# check = lambda age:True if age >= 18 else False

# print(multiply(7,8,8))
# print(double(5))
# print(name('Thanh', ' Vinh'))
# print(check(19))
 
 



#---- SORT ----
'''
- sort() method = used with lists
- sort() function = used with iterables
- Tuple can be matched with sort function (except when you turn it into a list)

'''
# students =('Vinh','Kiet','Trung','Nam')


#Can use with reverse function 
# students.sort(reverse = True)

# sorted_student = sorted(students,reverse=True)

# for i in sorted_student:
#     print(i) 



# Level 2

# students = [("Vinh","A",180),
#             ("Kiet","B",173),
#             ("Nam","C",168),
#             ("Trung","D",169),
#             ]
# grade = lambda grade:grade[1]
# height = lambda height:height[2] 
# students.sort(key=height,reverse=True)

# for i in students:
#     print(i)





#----- MAP ----
'''
- Map() = Appliesw a function to each item in an iterable (list, tuple, etc.)

- map(function, iterable)
'''


# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("coat",30.00),
#          ("Jacket",35.00)]


# to_euro = lambda data: (data[0],data[1]*0.82)
# to_dollar = lambda data: (data[0],data[1]/0.82)

# store_dollars = list(map(to_dollar,store ))

# for i in store_dollars:
#     print(i)



#----FILTER----
'''
- filter() = create a collection of elemrnts from an iterable for whcih function returns

- filter(function, iterable)

'''

# Friends = [("Rachel", 19),
#            ("Monica",18),
#            ("Kiet", 21),
#            ("Trung",22),
#            ("Vinh", 24)]




# check = lambda x:x [1] >= 20
# adult = list(filter(check, Friends))
# for i in adult:
#     print(i)




#---- REDUCE ----

'''
- reduce() = Apply a function to an iterable and reduce it to a single cumulative value
             performs function on first two elemts and repeats proccess until 1 value remain
             
             
- reduce(function, iterable)

'''
# To use reduce we have to import functools library

import functools 

# letters = ["H","E","L","L","L","O"]

# word = functools.reduce(lambda x,y : x + y, letters)
# print(word)


# With list of interger number it will multiply all value in the list

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y: x * y, factorial)
# print(result)