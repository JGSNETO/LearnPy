import tkinter as tk


#Create the root page
root = tk.Tk()
root.geometry("200x200")

def new_page():
    #Create a new window
    new_window = tk.Toplevel(root)
    new_window.geometry("500x500")
    #Add the widgets that you want to display on the new page
    label = tk.Label(new_window, text ="Single Activation Pre2Medium")
    label.pack()
    
    #Start new window
    new_window.mainloop()
    

#Create a button widget
button = tk.Button(root, text="Open new page", command=new_page)
button.pack()

#Start the main page
root.mainloop()