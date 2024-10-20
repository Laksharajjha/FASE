import customtkinter

# To figure out how to make moving panels in tkinter

root = customtkinter.CTk()
root.geometry("400x400")
root.title("Sliding screens")

canvas = customtkinter.CTkCanvas(root, bg = 'pink', width = 600, height = 600)
canvas.pack()

hello = customtkinter.CTkLabel(canvas, text = 'hello', font=('Arial',25))
hello.place(x = 25, y = 25)

x = 0
y = 0

def move(canvas):

    global x
    global y

    x+=1
    y+=1
    canvas.place(x = x, y = y)
    canvas.update()
    root.after(100, move,canvas)

move(canvas=canvas)

root.mainloop()