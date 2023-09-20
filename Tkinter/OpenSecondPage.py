import tkinter as tk


#Create the root page
root = tk.Tk()

def new_page():
    #Create a new window
    new_window = tk.Toplevel(root)
    #Add the widgets that you want to display on the new page
    label = tk.Label(new_window, text ="This is the new page")
    label.pack()
    
    #Start new window
    new_window.mainloop()
    

#Create a button widget
button = tk.Button(root, text="Open new page", command=new_page)
button.pack()

#Start the main page
root.mainloop()