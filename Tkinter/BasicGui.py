import tkinter as tk

# Create the main window
root = tk.Tk()

# Add a label widget
label = tk.Label(root, text = "Hello, world")
label.pack()

# Add a button widget
button = tk.Button(root, text = "Click me", command = root.destroy)
button2 = tk.Button(root, text = "Destroy", command = root.destroy)
button.pack()
button2.pack()

#Start the main event loop
root.mainloop()