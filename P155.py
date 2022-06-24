# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:12:23 2022

@author: Beautiful Mishika
"""

from tkinter import *
root = Tk()
root.title("Color CHanging Game")
root.geometry("600x600")

label_mutable = Label(root)
label_immutable = Label(root)
label_tkinter = Label(root)

dictionary = {'color' : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}
    
 def bg_change() :
     random_no = random.randint(0,7)
     print(dictionary['color'][random_no])
     root.configure(background = dictionary['color'][random_no])
     
btn = Button(root, text="click me", command=bg_change) 
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()