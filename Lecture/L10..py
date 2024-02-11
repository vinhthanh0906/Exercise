#-----List of lecture L10 ---- 
'''
- Multi-threading 
- Daemon Threading
- Multiprocessing
'''

#--- THREADING ---
'''
- Thread = a flow of execution. Like a seperate order of instructions 
            However each thread takes a turn running to achive concurency
            GIL = (global interpreter lock)
            allow only one thread to hold the control of the Python interpreter (No more)
            
- cpu bound = program/task spends most of it's time waiting for internal event (CPU INTENSIVE) use multiprocessing

- i/o bound = program/task spend most of it's time waiting for external event
 (user input) mlutithreading 
 
'''

# Active thread to process

# import threading
# import time

# def breakfast():
#    time.sleep(3) # Time for processing
#    print("You eat breakfast") # Consequence of process
   
# def coffee():
#     time.sleep(4)
#     print("You drank coffee")
    
# def study():
#     time.sleep(5)
#     print("You wrote an essay")

# The process take time to execute
# Take long time because use only 1 thread    
# breakfast()
# coffee()
# study()



# Create thread
# Faster
# x = threading.Thread(target=breakfast,args=())
# x.start()

# y = threading.Thread(target=coffee,args=())
# y.start()

# z = threading.Thread(target=study,args=())
# z.start()

# x.join()
# y.join()
# z.join()

# print(threading.activeCount())
# print(threading.enumerate)
# print(time.perf_counter()) # Count the time of process



#---- Daemon Thread ----
'''
-Thread that rún in the background, not important for program to run your program will not wait for 

daemon thread to complete before existing non-daemon threads cannot normally be killed, stay alive until rask complete 

Ex: background tasks, garbage collection, waiting for input,....
'''

# import threading
# import time

# def timer():
#     print()
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("Logged in for: ", count ,"seconds")
        
# x = threading.Thread(target=timer)
# x.start()

# answers = input("Do you want to exist: \n")


#--- Multiprocescing ---
'''
Multiprocessing  =  Runnign taks in para llel on different cpu core, bypasses Gil used
                multiprocessing --> better for cpu bound tasks (heavy cpu usage)
                multithreading --> better for io bound tasks (waiting around)

'''

# # Need to import multiprocessing 
# from multiprocessing import Process, cpu_count

# import time # need real time to take a process


# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
        
# def main():
#     print(cpu_count())
#     a = Process(target=counter, args=(10,))
#     b = Process(target=counter, args=(2000000000,))
#     c = Process(target=counter, args=(3000000000,))
#     d = Process(target=counter, args=(4000000000,))
#     e = Process(target=counter, args=(5000000000,))
#     f = Process(target=counter, args=(6000000000,))
         
    
    
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
    
    
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     print("Time left",time.perf_counter(),"seconds")
    

# #It will take time to do this 
    
    
# if __name__ == "__main__":
#     main()


#----GUI-----
from tkinter import * 
'''
- Definition
    + Widget = GUI elements: button, textbox, label, image
    + Window = serves as a container to hold or contain these widget
'''

window = Tk() # Create a window

window.geometry("540x540") #Res
window.title("Frostpunk")
#Create an icon

window.mainloop() # Listen for event