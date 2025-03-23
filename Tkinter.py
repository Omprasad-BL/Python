from tkinter import *
import tkinter as tk
root = Tk()
root.geometry("1250x720")

# given label to window
w = Label(root, text='GeeksForGeeks.org!')
w.pack()

# create button
button= Button(root,text="You can close it " ,command=root.destroy)
button.pack()

# giving label to button
w=Label(root,text="new Text ",padx=20)
w.pack(pady=10)

text_entry=Entry(root,width=30)
text_entry.pack(pady=10)

# create list
Lb= Listbox(root)
Lb.insert(1,"Python")
Lb.insert(2,"Java")
Lb.insert(3,"Go")
Lb.insert(4,"Rust")
Lb.pack()

# create scale
w=Scale(root,from_=0 , to=42)
w.pack()
w=Scale(root,from_=0,to=200,orient=HORIZONTAL)
w.pack()

root.mainloop()

