#-----L11 List ogg Lecture ----
'''
- GUI
- Label
- Button
- Entrybox
- Knot button 
'''


#----GUI-----

'''
- Definition
    + Widget = GUI elements: button, textbox, label, image
    + Window = serves as a container to hold or contain these widget
'''
'''
from tkinter import *
window = Tk() # Create a window

window.geometry("540x540") #Res
window.title("Frostpunk")

#Create an icon
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

#Background color
# Can use hex value to display color
window.config(background='black')

window.mainloop() # Listen for event, = Whie true
'''


#----LABELS----
'''
- Labels is an area widget that holds text and/or an image within a window
- Some type of border : RAISED, SUNKEN
'''
'''
from tkinter import *



window = Tk()

window.geometry("540x540") #Res
window.title("Frostpunk")



photo = PhotoImage(file='logo.png')

# Create lable
# Label(container,text=" ")
label = Label(window,
              text="Frostpunk",
              foreground='cyan',
              bg='black',
              font=('Time New Roman',40,'italic'),
              border='5px',
              relief=RAISED,
              padx = 20,
              pady= 20,
              image= photo,
              compound='bottom')

label.pack() # Alway at top 

# label.place(x=100,y=200)

window.mainloop()
'''



#-----BUTTON----

'''
from tkinter import*
count = 0
def click():
    print("Gta 6 will dominate game industry")
    global count
    count += 1
    print(count)

window = Tk()
button = Button(window,
                text="Click me",
                command=click,
                font=("Arial",40,'bold'),
                fg='gray',
                bg='white',
                activebackground='black',
                activeforeground='gray',
                state=ACTIVE,
                compound='bottom') # Active/Disable

#Same to labels
button.pack()

window.mainloop()
'''


#---Entrybox---

'''
# entry widget = textbox that accepts a single line of user input 

from tkinter import *

def submit():
    username = entry.get()
    print("hello " + username)
    entry.config(state=DISABLED) # Execute when get an event
def delete():
    entry.delete(0,END)    

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()
entry = Entry(window,
              font= ("Time New Roman ",50),
              fg = "cyan",
              bg = "black",
              show = "*") # Show it instead of text

#Insert a default text 
# entry.insert(0,"Frostpunk")


entry.pack(side=LEFT)

sub_button = Button(window,text="Submit",command=submit)
del_button = Button(window,text= "Delete",command=delete)
bs_button  = Button(window,text= "Backspace",command=backspace)

sub_button.pack(side=RIGHT)
del_button.pack(side=RIGHT)
bs_button.pack(side = RIGHT)

window.mainloop()
'''


#----CHECK BUTTON----

'''
from tkinter import *

def check():
    if (x.get()):
        print("Nice job")
    else:
        print("Stay hard")

window = Tk()

# We can change the data type (Depend on below attribute )
x = BooleanVar()


#make a check button

check_button = Checkbutton(window, 
                           text="Do 100 push ups",
                           font=("Time New Roman",40,'bold'),
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=check,
                           foreground='cyan',
                           background='black',
                           activebackground='black',
                           padx= 20,pady=20,
                           border = '25px',
                           relief=RAISED,
                           )


check_button.pack(side=LEFT)
window.mainloop()

'''


#----- radio-button ------
'''
- Similar to checkbox, but you can only select one from a group
'''

# from tkinter import * 

# guns = ["Ak-47","M4A4"]


# window = Tk()
# ak_pic = PhotoImage(window,file='ak47.png') 

# icon = [ak_pic]

# x = IntVar()
# for i in range(len(guns)):
#     knot_button = Radiobutton(window,
#                               text=guns[i], # Add text to radio button 
#                               variable=x, # Group radiobutton together if they shared the same variable
#                               value=i, # Assign each radiobutton to different value 
#                               padx = 25,
#                               pady= 20,
#                               font=("Impact",30,'underline'),
#                               bg='black',
#                               foreground='green',
#                               activebackground= 'cyan',
#                               activeforeground='yellow',
#                               image = icon[i] # Add inmage to radiobutton
#                               )
    
     
#     knot_button.pack(anchor=W) # line up all radiobutton

# window.mainloop()