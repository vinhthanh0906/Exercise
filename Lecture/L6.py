'''-----L6 LIST OF LECTURE------
- OOP (Object Oriented Programming) 
- Class Variable (included OOP)
- Inheritance (ke thua)
- Multilevels inheritance
- Multiple inheritance
- Method Overriding
- Method Chaining



'''

#-----INHERITANCE------
'''
- A parents class will pass all its attribute to others subclass
- No need to copy and paste the parent code
- (self) will keep the own attribute of class for itself
- Change class in () if u want other class inherit 
'''

# class Animals:# parent class
    
#     alive = True
    
#     def eat(self):
#         print("this animal is eating ")
        
#     def sleep(self):
#         print("this animal is sleeping")
        
# class Rabbit(Animals): #child class, inherit everything in Animals class
    
#     def speed(self):
#         print("Rabbit is fast")
# class Hawk(Animals):
#     def sight(self):
#         print("Hawk has good sight")
# class Cat(Animals):
    
#     def steady(self):
#         print("Cat is steady")
    
    
# #Creat object
# rabbit = Rabbit()
# cat = Cat()
# hawk = Hawk()


#rabbit.speed() #no need to use print because its function







#------MULTI-LEVELS INHERITANCE-----
'''
- When a derived (child) inherited another derived (child) class

'''


# class Organism:
    
#     alive= True
    
# class Animal(Organism):
#     def food(self):
#         print("Animal need food to stay alive")
        
# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")
        
# class Cat(Animal):
#     def mew(self):
#         print("Cat is mewing")
        
        
# dog = Dog()          
# print(dog.alive)      # Inherited from Organism class
# dog.food()            # Inherited from Dog class
# dog.bark()            # define in Dog class

# print(" ")
# cat = Cat()
# print(cat.alive)
# cat.mew()
# cat.food()





#-----MULTIPLE INHERITANCE------
'''
- When a child class is derived from more than one parent class


'''

# class Predator:
#     def hunt(self):
#         print("The predator is hunting ")

# class Prey:
#     def flee(self):
#         print("The prey is fleeing")
        
        
# class Rabbit(Prey):
#     def run():
#         print("Rabbit is running")

# class Wolf(Predator):
#     def chase():
#         print("the wolf is chasing the rabbit")

# class Fish(Prey, Predator):
#     pass
# rabbit = Rabbit()
# wolf = Wolf()
# fish = Fish()



# fish.flee()
# fish.hunt()



#------METHOD OVERIDING------
'''
- A new method will be overrode on the recents one (even its the parent class)

'''
# class Vehicle:
#     def wheels(self):
#         print("This car has 8 wheels")

# class Car(Vehicle):
#     def wheels(self):
#         print("Car has 4 wheels")

# car = Car()
# car.wheels() # the wheels method in Car() overrode the wheels method from Vehicle()






#-----METHOD CHAINNING------
'''
- Calling multiple method sequentiall each call performs an action on the same object and retrns self

'''

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
        
    def drive(self):
        print("You are driving a car")
        return self
        
    def brake(self):
        print("You step on the brake ")
        return self
    def turn_off(self):
        print("You tuen off the engine")
        return self
car = Car()
# Return funtion will reset the car into itself without any attribute follow its
car.turn_on().drive().brake() # Method chaining


    
    