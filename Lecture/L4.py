''' ---L4 LIST OF LECTURES---
- Function
- Return statements
- Nested function call
- Scope
- Args
- Keyword arguments
- String format 
'''




#-----FUNCTION----

'''
- a block of code which is only execute when its called
'''

#Define the function 
def hello(first_name,last_name, age):
    #print("Hello " + first_name + " " + last_name + " "+ age)
   # print("Fuck this shit i'm out")
   pass

#hello("Thanh","Vinh", "18")
# With fuction u dont need do def variable 







#----RETURN STATEMENTS-----
'''
- Function send Python values/object back to the caller
- These value/object are known as the function's return value 
'''

def multiply(number_1, number_2):
    return number_1 * number_2

# You can save the result to by variable
#x = multiply(6,8)

#print(x)
    
    
    




    
#-----KEY WORD ARGUMENTS-----
'''
- Arguments preceded by an identifier when we pass them to a fuction

- The order of the arguments does not matter, unlike positional arguments

- Python knows the nams of the arguments that our function receives
'''

def name(first, mid ,last):
    #print(first,mid,last)
    pass
    
# Can use elements to located the return value    
name(last="Nguyen",mid="Thanh",first="Vinh")









#-----NESTED FUNCTION CALLS----
'''
- Function calls inside other function calls

- Innermost function calls are resolved first 

- Returned value is used as argument for the next outer function 

'''


#num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
#num = round(num)
# print(num)

# We can adjust its shorter belike:

# print(round(abs(float(str(num)))))




#-----VARIABLE SCOPE-----
'''
- The region that a variable is regconized
- A variable is only available from inside the region it is called
- A global and locally scoped versios of variable can be created


'''

# Outer  = "Neptune"
# # Neptune can be printed inside inner function

# def helio_inner():
# # Earth is local variable, cant be printed outside fuction
#     inner = "Earth"
#     print(Outer)
    
# helio_inner()
# print(Outer)




#-----ARGS-----
'''

- A parameters that will pack all arguments into a tuple
- Useful so that a function can accept a varying amount of arguments
- Remember to use asterisk because it mean packing to tuple(*)
- Use can use any name after '*'
- if you want to cahnge the value assignment in tuple, you need to chang the data type ---> list
'''


# Use * to follow the number of argument so you dont have to add more parameter

 
# def add(*lmao):
    
#     sum = 0
#     lmao  = list(lmao)
#     #lmao change from tuple to list
#     lmao[0] = 3
#     for i in lmao:
#         sum += i
#     return sum    
        
# print(add(1,2,3,4,5))






#-----**KWARGS-----
'''
- Stand for 'keyword argument'
- Parameter that will pack all argumens into a dictionary (args to tuple)
- Useful so that a function can accept a varying amount of keyword arguments
- Kwargs use 2 asterisk

'''
# def vinh(**Lmao):
#     print("Hello",end=" ")
#     for key,value in Lmao.items():
#         #print the value go equivlent with keyword 
#         print(value, end=" ")
        
# vinh(first="Nguyen", second="Thanh",last="Vinh",third="Lmao")







#----STRING FORMAT----

'''
- Optional method that gives users more control when displaying outpuut
- {} like a placeholder or format field to format the value of variable
- Use can place a locations number in format field (eg. {0}) --> index the value equivlent with position
 '''


animal = "Dog"
item = "hole"

# print("What the " + animal + " doing on the" + item)

# print("What the {} doing in the {}".format(animal,item))
# You can use kwargs instead of define a variable  
# print("What the {animal} doing in the {item}".format(animal="Dog",item="moon"))


# Can use a variable to define a format field
# sheet = "The {} in da {}"
# full = sheet.format(animal,item)
# print(full)


# ten = "Vinh"

# print("Hello my name is {}".format(ten))
# # Creating a padding to add more string value
# print("Hello my name is {:<10}".format(ten)) #left allign
# print("Hello my name is {:>10}".format(ten)) #right allign
# print("Hello my name is {:^10}".format(ten)) #central

# #format a number
# number = 3.1234

# print("The number is {:.2f}".format(number) )