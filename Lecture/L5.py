'''-----L5 LECTURE LIST-----
- Random number 
- Exception handling 
- File Detection
- Reading a file
- Write a file
- Copy a file
- Move a file
- Delete a file
- Module 

'''


#-----RANDOM NUMBER----
# import random 
# x = random.randint(0,3)
# # Take every random number include int, float,...
# y = random.random()

# option = ["Rock","Paper","Scissor"]
# #z = random.choice(option)
# card =[1,2,3,4,5,"J","Q","K"]

# random.shuffle(card)
# print(card)





#-----EXCEPTION HANDLING-----
'''
- Events detected duibng execution that interrupt
- Prevent to abuse exception handleing because it make your project heavier and slower
'''
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
    
## Can handle multiple exception 
## Got many exception (eg. Valuerror, Zerodivisionerror, FilenotFounderror,...)
## as e mean as exception


# except ZeroDivisionError as e:
#     print("Cant divide 0!! ")
    
# except ValueError as e:
#     print("Invalid input")  
        
# except Exception as e:
#     print("Somthing went wrong")
    
# else:
#     print(result) 
# finally:
#     print("This is always execute even has a result or detected a exception")   


#----FILE DETECTION----
'''
- A tool help you to find a file path 
- Alway 'import os' if you want to use it
- Some checking syntax (eg. isfile, isdir,...)
'''


# # It will interat with your computer's operation system
# import os 
# path = "/Users/nguyenthanhvinh/Documents/PYTHON/Excercise/Practice.py"


# if os.path.exists(path):
#     print("True")
    
#     if os.path.isfile(path):
#         print("A file")
#     else:
#         print("It is not a file") 
# else:
#     print("Its not existed")



#-----READING A FILE-----
'''
- Read a file and display the file's content in the terminal window
'''
# try:
#     with open('basic1.py') as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not Found")




#----WRITE A FILE----
'''
- Only blank text file is unable to write in
'''

# text = "Elle Lee\n"
# with open("/Users/nguyenthanhvinh/Documents/PYTHON/Excercise/Practice.py") as file:
#     file.write(text)



#-----COPY A FILE-----
'''
copyfile() --> Copy contents of file

copy() --> copyfile() + permission mode + destination can be a directory

copy2() --> copy() + copies metadata (file's creation modification time)

'''

# # Shutil module is high level module which allow u to copy, create, remote operation
# import shutil 

# shutil.copy2('','/Users/nguyenthanhvinh/Documents/PYTHON/Excercise/Practice.py')#src.dst





#----MOVE A FILE----
'''
- Moving a file to the new destination we want
- A file can only be moved to a folder which can capacitating a file

'''

# import os

# source = "hint mario pset.png" # source file
# destination = " /Users/nguyenthanhvinh/Documents/PYTHON/Testing field" # place a file come to

# try:
#     if os.path.exists(destination):
#         print("This file is already there")
#     else:
#         os.replace(source,destination)
#         print("Source was moved")
        
# except FileNotFoundError:
#     print("Can not find a source file")






#----DELETE A FILE-----
'''
- Remove a file from a folder
- Use 'rmdir' to remove a folder
- To delete folder included file, U need use 'shutil module'
- 'rmtree' mean remove all folder include file inside it
'''
# import os
# import shutil # higher levels than 'os opertion'

# try:
#     path = ("/Users/nguyenthanhvinh/Documents/PYTHON/Excercise/test")
# #   os.path() --> remove a file
# #   os.rmdir() --> remove a directory
# #   shutil.rmtree(path) --> Delete a folder containing file 

# except FileNotFoundError:
#     print("File not found")
    
# # U cant remove a folder with 'remove'   
# except PermissionError:
#     print("Access denied")

# else: 
#     print("test was removed")






#----MODULE----
'''
- A file containing python code, function ,classes etc.
- Used with modulatr programming, which is to seperate a program into parts
- Use 'help("modules")' to search more module

'''
# #Import to shortage name
# import messages 
# def hello():
#     print("Bulul Lmao")
    
# def bye():
#     print("Tuong ot thoi")

# help('module')