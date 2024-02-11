'''-----L9 List of lecture -----
- Comprehension
    + List comprehension 
    + Dictionary comprehension 
    
    
- Zip function
- if_name_ == '_main_'
- Time module




'''

#----LIST COMPREHENSION----
'''
- a way the creat a new list with less syntax
- can mimic certain lambda functions, easier to read 

* Formula (3 methods): 

     1. list = [expression (if/ else) item in iterable]
     
     2. list = [expression for item in iterable if condition]

     3. list = [expression if/else for item in iterable ]
'''


# square = []                   # create an empty list 
# for i in range(1,11):         # create a for loop
#     square.append(i * i)      # define what each loop iteration should do
# print(square)

# # Same result with the function 
# square = [i * i for i in range(1,11 )]      # This is list comprehension 
# print(square)



#Ex: 

# students = [100,90,80,70,60,50,40,30,]

# # Can use lambda like list comprehension 
# # passed_students = list(filter(lambda x: x > 60, students))

# # We can use conditional statements in list comprehension 
# # The line below will replace the 'failed' to any element which lower than the condition
# passed_students = [i if i >= 60 else "failed" for i in students ]

# failed_students = list(filter(lambda y: y < 60, students))
# print(passed_students)
# print("Numbers of failed students",failed_students)



#----DICTIONARY COMPREHENSION -----
'''
- Create dictionaries using an expression 
- Can replace for loops and certain lambda functions

*Formula: 
        1. dictionary = {key:expression for (key, value) in iterable}
        
        2. dictionary = {key:expression for (key, value) in iterable if conditional }
        
        3. dictionary = {key: (if/else) for (key, value) in iterable  } (With this formula it will replace insatisfied value by False)

- It seem lkewe can't use 3 condition fuction in dict comprehension 
'''



# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles':100,'Chicago':50}

# #We can impact all value by this syntax
# cities_in_C = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items( ) }
# print(cities_in_C)


# weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles':'cloudy' ,'Chicago':'Rainny'}
# populity = {'New York':60 , 'Boston':30, 'Los Angeles':70, 'Chicago':50}




# #Can add conditional statement inside dictionary 
# big_city = {key: ("Big city " if value >= 50 else "Med city ") for (key, value) in populity.items()}
# sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
# stat = {key: ("Warm" if value >= 40 else 'Cold') for (key,value) in cities_in_F.items()}


# print(big_city)



#----ZIP FUNCTION----
'''
- Zip (*iterables) = aggregate elements from two more iterable (list, tuples, sets, etc.) 
                     creates a zip object with paired elements strored in tuples for each element
                     

'''

# username = ["Dude","Bro",'Vinh']
# password = ("password", "abc123", ' guest')
# login_date = ["9/6/2005","2/9/1945","3/5/2006"]
# users = dict(zip(username, password))
# print(type(users))

# for key,value in users.items():
#     print(key + " : " + value)

# users = zip(username,login_date)

# for i in users:
#     print(i)




#----if_name_ == '_main_'----

'''
# y tho?
# 1. Module can bbe run as a standalone program
# 2. Module can be imported and used by other module

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code the code found within __main__
'''

# import Test
# print(__name__)
# print(Test.__name__) # this systax will p[rint the imported file name]

# if __name__ == 'L9': # this syntax will run when the file has name in the syntax
#     print("Running this module directly")
# else: 
#     print("Running other module indirectly")


# def main():
#     print('Hello world')

# if __name__ == '__main__': #'main' is the default 
#     main()


#------TIME MODULE-------   
'''
 epoch = a date and time from which a 
         computer measures system time


'''
# import time

# print(time.ctime(0)) # comvert a time expressed in seconds since epoch to readable 
                        # so epoch = when your computer thinks time began (reference point)


# print(time.time()) # return current seconds since epoch
                   # number will change will change when the time change    
                   
# print(time.ctime(time.time())) # Covert from com time to real time


# time_obrs = time.localtime() # base on real time
# print(time_obrs)
# read_time = time.strftime("%B %d %Y %H:%M:%S",time_obrs)
# print(read_time)


# time_tuple = (2020,4,20,4,20,0,0,0,0)
# time_string = time.mktime(time_tuple) # Convert to readable string (asctime) / computer time (mktime) 
# print(time_string)