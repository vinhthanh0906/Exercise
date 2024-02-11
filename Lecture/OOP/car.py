class Car:
  
    wheels = 4 #class variable
    
    
    # Contructing a core show can add feature on it
    # Function like a part of structure
    def __init__(self,make,model, year, color):
        
        
        #Connect feature to constructor
        
        self.make = make # an instance variable
        self.model = model
        self.year = year
        self.color = color
    
    
    def drive(self):
        print("This " + self.model + " is driving")
        
    def stop(self):
        print("This " + self.model +  " was stop")
        
