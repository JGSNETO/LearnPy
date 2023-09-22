import tkinter as tk

def get_side_selection(window, side_var, chosen_side):
    chosen_side.set(side_var.get())
    window.destroy()

def single_activation_medium():
    # Variable to store the chosen side
    chosen_side = tk.StringVar()
    side_var = tk.StringVar()
    
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("Choose Side")
    new_window.geometry("500x500")
    
    # Variable to store the selected side
    side_var = tk.StringVar()
    
    # Create a Checkbutton for "Left" option
    left_checkbutton = tk.Checkbutton(new_window, text="Left", variable=side_var, onvalue="Left", offvalue="")
    left_checkbutton.pack()
    
    # Create a Checkbutton for "Right" option (fixed typo here)
    right_checkbutton = tk.Checkbutton(new_window, text="Right", variable=side_var, onvalue="Right", offvalue="")
    right_checkbutton.pack()
    
    # Create a button to confirm the selection
    confirm_button = tk.Button(new_window, text="Confirm", command=lambda: get_side_selection(new_window, side_var, chosen_side))
    confirm_button.pack(pady=10)
    
    # Start new window
    new_window.mainloop()

# Create the root page
root = tk.Tk()
root.geometry("200x200")

# Create a button widget
button = tk.Button(root, text="Open new page", command=single_activation_medium)
button.pack()

# Start the main page
root.mainloop()
