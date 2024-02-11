'''-----L7 LIST OF LECTURE-----
- Super Function
- Abstract class
- Object as arguments
- Duck typing




'''



#------SUPER FUNCTION--------
'''
- Function used to gice access to the method of a parent class
- Return a temporary object of a parent class when used

'''
# class Rectangle:
#       def __init__(self,length,width):
#         self.lenght = length
#         self.width = width

# class Square(Rectangle):
    
#     def __init__(self,length,width):
#         super().__init__(length,width)
        
#     def area(self):
#         return self.lenght * self.width

# class Cube(Rectangle):
#     def __init__(self,length,width,height):
#         super().__init__(length,width)
#         self.height = height
        
#     def volume(self):
#         return self.lenght * self.width * self.height
       
# square = Square(3,3)
# cube = Cube(3,3,3)       
    
# print(square.area())
# print(cube.volume())





#-----Abstract class-------

'''
- Prevents a user from creating an object of that class 
- compels a user to override abstract merthods in a child class

# abstract class = a class which contains one or more abstract methods.

#abstract method = a method that has a declaration but does not have an implementation


'''

# from abc import ABC, abstractclassmethod


 
# class Vehicle(ABC):
    
#     @abstractmethod
#     def go(self):
#         print("You drive the car")
#         pass

#     @abstractclassmethod
#     def stop(self):
#         pass
        

# class Car(Vehicle):
   
#     def go(self):
#         print("You drive the car")
        
#     def stop(self):
#         print("This car was stopped")
        
        
# class Motorcycle(Vehicle):
#     def go(self):
#         print("You are riding a motorcycle")
        
#     def stop(self):
#         print("This bike was stopped")
        
        
        
# vehicle = Vehicle()
# car  = Car()
# motorcycle = Motorcycle()

# vehicle.go()
# car.go()
# motorcycle.go()

# car.stop()
# motorcycle.stop()





#-----OBJECT AS ARGUMENTS-----
'''
- Can turn an object to arguments to add attribute to it
'''
# # No color, need to return
# class Star:
#     color = None
    
# # No color, need to return
# class planet:
#     color = None
        
# def change_color(star,color):
#         star.color = color

# earth_1 = planet()        
# star_1 = Star()
# star_2 = Star()
# star_3 = Star()

# # return color value to change_color function
# change_color(star_1,"red")
# change_color(star_2,"blue")
# change_color(star_3,"red")
# change_color(earth_1,"green")

# print(star_1.color)
# print(star_2.color)
# print(star_3.color)
# print(earth_1.color)





#-----DUCK TYPING-----
'''
- Concept where the class of an object is less important than the methods
- Class type is not checked if minimum methods/attributes are present
- If it walks like a duck, and it quack like a duck, then it must be a duck

'''

# class Duck:
#     def walk(self):
#         print("This is walking")
        
#     def talk(self):
#         print("This Duck is qwuacking")
        
# class Chicken:
    
#     def walk(self):
#         print("this chicken is walking")
        
#     def talk(self):
#         print("this chicken is clucking")

# class Person():
#     def catch(self, chicken):
#         chicken.walk()
#         chicken.talk()
#         print("You caught the critter")
        
# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(chicken)