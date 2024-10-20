import tkinter as tk

# Create a function to handle button clicks
def button_click(action):
    output_label.config(text=f"Button {action} was pressed")

# Create the main tkinter window
root = tk.Tk()
root.title("Button List Example")

# Create a list of button labels
button_labels = ["Button 1", "Button 2", "Button 3", "Button 4"]

# Create a list to store the button widgets
buttons = []

# Create and display buttons based on the button_labels list
for i, label in enumerate(button_labels):
    button = tk.Button(root, text=label, command=lambda i=i: button_click(i+1))
    button.pack()
    buttons.append(button)

# Create a label to display the output
output_label = tk.Label(root, text="")
output_label.pack()

# Run the main tkinter event loop
root.mainloop()