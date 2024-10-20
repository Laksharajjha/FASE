import customtkinter
import math

root = customtkinter.CTk()
root.geometry("400x400")
root.title("Sliding screens")

canvas = customtkinter.CTkCanvas(root, bg = 'pink', width = 600, height = 600)
canvas.place(x = 0, y = 0)

hello = customtkinter.CTkLabel(canvas, text = 'hello', font=('Arial',25))
hello.place(x = 25, y = 25)

x = 0
y = 0

def slide_into_view_child(root, canvas, canvas_length, canvas_width, speed, x_pos, init_position_x, init_position_y ,window_length, window_height, horizontal, ms):

    if(horizontal and x_pos>init_position_x):


        canvas.place(x = x_pos, y = init_position_y)
        #   change = speed * (math.sqrt(math.pow(math.sin(((x_pos-window_length+1)/window_length *math.pi)),2)))
        change = speed * math.sqrt(math.pow(math.sin((x_pos-window_length)/canvas_length * math.pi),2))
        x_pos -= change
        print((x_pos-window_length)/window_length * math.pi)
        print(change,speed,(math.sqrt(math.pow(math.sin(((x_pos-window_length+1)/window_length *math.pi)),2))))
        canvas.update()
        root.after(ms, slide_into_view_child,root, canvas, canvas_length, canvas_width, speed, x_pos, init_position_x, init_position_y ,window_length, window_height, horizontal, ms)


def slide_into_view(root, canvas, canvas_length, canvas_width, speed, init_position_x, init_position_y ,window_length, window_height, horizontal, ms):

    if(horizontal):

        x_pos = canvas_length + window_length

        root.after(ms, slide_into_view_child, root, canvas, canvas_length, canvas_width, speed, x_pos, init_position_x, init_position_y ,window_length, window_height, horizontal, ms)

slide_into_view(root, canvas, 600, 600, 50, 1, 1, 600,600, True,5)
    

root.mainloop()