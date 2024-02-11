#-----OOP------
'''
- A computer programming model that organizes software design around data, or objects, rather than functions and logic
- An object can be defined as a data field that has unique attributes and behavior.

'''




#import by name of module from Class
from car import Car

car_1 = Car("Ford","Mustang",1978,"Silver")
car_2 = Car("Chevolett","Camoro",1990,"Black and Gold") 

car_1.wheels = 2 #can change class variable 
car_2.wheels = 4

Car.wheels = 2 # Can change variable globally

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
print(car_1.wheels)
print(car_2.wheels)



# car_1.drive()
# car_1.stop()