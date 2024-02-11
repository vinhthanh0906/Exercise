''' L1 LIST OF LECTURE
- Classing
- FLOAT
- MULTI ASSIGNMENT
- Multi assignment
- String method
- Math function 
- String slicing 


'''

#----CLASSING-----

#name = "Lmao"
#age = 18
#print("Hello " + name)
#print("Age: " + str(age))
#print(type(name))

#----FLOAT----



#height = 250.5
#print(height)
#print(type(height))





#---BOOLEAN---


#human = False
#print("Are you a human " + str(human))

#---MULTIPLE ASSIGNMENT----



'''
name, age, detail = "Vinh", 18, False

Spongebob = Patrick = Squidward = Sandy = 30

print(Patrick)
'''


#----STRING METHOD----
#name = "Thanh Vinh"

#print(len(name)) // Length of variable

#print(name.find("i")) // Find unit in var

#print(name.capitalize()) // Capitalize first digit

#print(name.upper()) // Capitalize

#print(name.lower())  

#print(name.count("n"))

#print(name.replace("n","h"))

#print(name * n)


#----TYPE CASTING----
# Convert a varible from current data type to others data type
'''
x = 3
y = 2.5
z = "3"

a = int(y) + 3
print(a)
'''

#----MATH FUNCTION-----
import math
pi = 3.14
x = 1
y = 2
z = 3
#print(round(pi)) // round to the nearest int number 
#print(math.ceil(pi)) // round up to next int number 
#print(math.floor(pi)) // round up to floor int number 
#print(abs(pi)) // Take absolute value 
#print(math.sqrt(6400))
#print(max(x,y,z)) // min to same

#----STRING SLICING-----
'''

- Slicing = create a substring by extracring elements from another string 

-           indexing[] or slice() //

-           [start: stop: step]  // 

'''



#full_name = "Thanh Vinh"
#fisrt_name = full_name[0:6:2]
#last_name = full_name[6:]
#reverse_name = full_name[::-1] # If the step is negative

#print(reverse_name)

#
website1 = "https://www.google.com.vn"
website2 = "https://www.youtube.com/"

# Slice need a variable to use, same step of indexing
# Slice string into parts we want 
slice = slice(7,-4) 

print(website1[slice])
print(website2[slice])
