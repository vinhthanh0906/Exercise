''' L2 LIST OF LECTURE 
- Logical Operator
- While Loop
- For loop
- Nested Loop
- Break, pass, continue

'''
#-----LOGICAL OPERATORS--------
# - Include 'and' , 'or' , 'not' ---> used to check if two or more conditional statement

#degree = int(input("What is temperature today?: "))

#Two conditional statement
#if degree >= 0 and degree <= 15:
   # pass 
    #print("Cold weather")
    
# Not is flip conditional statement (True <-<>-> False)
#elif not(degree > 45 or degree < 0):
    #pass
    #print("Acceptable")
#else:
    #pass
    #print("OK")
    
    
    
    
    
#-----WHILE LOOP-----
'''
* NOTE !* 

- A statement that will execute it's block of code, as long as it's condition remains TRUE
- '1==1' mean True in while loop
- While loop is unlimited loop
'''
#name = None 
#while not name: # reverse True while loop 
    
    #name = str(input(("What your name: ")))
    
#print("Hello" + name)
    
    
    
#----FOR LOOP---
'''
- A statement taht weill execute it's block of code 
- A limited amount of time 
- if use for loop in string , we got a string printed in different line
- Remember to import time directory 
'''
import time
# Can limited the range of for loop by format '(start , end)'
#for seconds in range (10,0,-1):
# A loop rundown from 10 to 0 by -1 step
    #print(seconds)
    #time.sleep(1)
#Loop will wait for 1 sec before print the string 
#print("Happy New Year!!")





#-----NESTED LOOP-----
'''
- The 'inner loop' will finish all of it's iteration before
finish one iteration oof the "outer loop"

- end="" is syntax to prevent to print in the next line

'''

#width = int(input("width: "))
#height= int(input("height: "))
##symbol = input("Symbol: ")

#for i in range(width):
    #for j in range(height):
        #print(symbol, end="")
   # print()

    
    
    
#----BREAK, countinue, pass----
'''
- A Loop control Statements: change a loop execution from its normal sequence
    + break --> used terminate the loop entirely
    + continue --> skips to the next iteration of the loop
    + pass --> pass the loop to the next line

'''
#while True:
    #name = input("What your name: ")
    #if name != "":
        #break
        
        
#phone_number = "094-745-6078"
#Run a loop through each char of string 
#After using for loop , i become a variable
#for i in phone_number: 
    #if i == "-":
        #continue
    #print(i, end=" ")






    