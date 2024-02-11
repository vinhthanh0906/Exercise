''' ------ L3 LIST OF LECTURE ------
- List            
- 2D list          
- Tuple            
- Sets             
- Dictionary    
- Indexing 

'''


#----LIST----
'''
- Can use name.[n] to chang the element in list 
- print(name[n]) to find the location of elements in list\
    
'''
food = [1,2,3,"pizza",4.6]
#print(food[2]) 


# Some function related to list 
'''
- append
- remove
- pop : remove the last elements in list
- insert : add an element to location we want 
eg. food.insert(0, "Noodle")

- sort: sort the list  alphabetically
- clear: remove all elements in the list 

'''

food.append("Ice cream ")
#for i in food:
    #print(i)
    
    


#----2D LISTS----
'''
- A list of list
- Also called multi-dimension list

'''

Triple_A = ["Uncharted 4","Tomb Raider","GoW","DS"]
Esports = ["CS:GO", "Valorant","LOL"]
Indle = ["Minecraft", "Raft", "GTFO"]
# List is just element of others  bigger lists 
Games = [Triple_A, Esports, Indle]

# Display the element of inner list and itself
#print(Games[2][0])





#----TUPLE-----
'''
- Collection which is ordered and unchangeable 
- Used to group together ralated data
'''


info = ("Vinh", 21, "first year","male")
#print(info.count(21))
# Index the location of elements in tuple
#print(info.index("male"))

for x in info:
    pass
    
if "Bro" in info:
    pass
    #print("Bro is here")
    
else:
    pass
    ##print("No is Vinh")




#-----SETS-----
'''
- Collection which is unordered, unindexed
- No duplicate

'''

utensils = {"Spoons", "Forks", "Knives","Chopsticks"}
dishes = {"Steak", "Chips", "Rice"}

#utensils.add("Napkins")
#utensils.remove("forks")
#utensils.clear()
#utensils.update(dishes) <=> dished.update(utenils)
dinner_table = utensils.union(dishes)
#Combine 2 ists together

#//print(utensils.difference(dishes))
#Compare the 2 lists to find the different elements

for x in dishes:
    pass
    #print(x)




#----DICTIONARIES----
'''
- A changeable, unordered collection of unique (key:value) pairs
- Fast because they are using hashing, allow to access value quickly

'''


capitals = {'USA':'Washington D.C',
            'Vietnam':'Hanoi',
            'China':'Beijing',
            'Korea':'Seoul'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA' : 'New York'})
capitals.pop('China')
capitals.clear()


# To index the value in dictionary, we use key to access
# We use square bracket to with key     
#print(capitals['Korea'])


#print(capitals.get('Germany'))
# If the key not existed, it will output NONE


#print(capitals.keys())
#print(capitals.values())
#print(capitals.item())->print key and value

for key,value in capitals.items():
    pass
    #print(key,value)
    
    



#----------INDEXING---------
'''
- Give a access to a sequence's element (str,list,tuple)

'''    



#name = "Nguyen Thanh Vinh"
#if (name[0].upper()):
    
    #name = name.upper()
#print(name)
    
first_name = "Thanh Vinh"
name2 = first_name[0:6].upper()
last_name = first_name[-1]
print(last_name)
print(name2)