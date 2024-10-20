import tkinter as tk

# Function to be executed when the button is pressed
def button_click():
    label.config(text="Button was pressed")

# Create the main tkinter window
root = tk.Tk()
root.title("Button with Enter Key Example")

# Create a button and bind the <Return> event to it
button = tk.Button(root, text="Press Me", command=button_click)
button.pack()

# Function to simulate a button click when Enter key is pressed
def on_enter_key(event):
    button_click()

# Bind the <Return> event to the button
root.bind('<Return>', on_enter_key)

# Create a label to display the output
label = tk.Label(root, text="")
label.pack()

# Run the main tkinter event loop
root.mainloop()