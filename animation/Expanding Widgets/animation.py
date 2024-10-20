import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")
root.title("Animation Test")

frame = ctk.CTkFrame(root,width = 500, height = 500, bg_color='pink')
frame.pack()

height = 20
increment = 1

canvas = ctk.CTkFrame(frame, width = 20, height = height)
canvas.place(x = 250, y = 0)

def lengthen_canvas_fast():

    global height
    global increment

    if(height < 250):

        canvas.configure(fg_color = 'blue')

        increment*=1.1
        height+=increment
        print(height)
        canvas.configure(height=height)

        
        root.after(1, lengthen_canvas_fast)

    else:

        canvas.configure(fg_color = 'pink')

        print(1)

        increment/=1.5
        height+=10
        print(height)
        canvas.configure(height=height)

        root.after(1, lengthen_canvas_fast)



def lengthen_canvas_slow():

    global height
    global increment

    canvas.configure(fg_color = 'pink')

    print(1)

    increment/=1.5
    height+=10
    print(height)
    canvas.configure(height=height)

    if(height < 500):
        root.after(50, lengthen_canvas_slow)

lengthen_canvas_fast()
#lengthen_canvas_slow()

root.mainloop()