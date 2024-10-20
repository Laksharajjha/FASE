import customtkinter as ctk
import math

root = ctk.CTk()
root.geometry("500x500")
root.title("Animation Test")

frame = ctk.CTkFrame(root,width = 500, height = 500, bg_color='pink')
frame.pack()

height = 20
increment = 1

canvas = ctk.CTkFrame(frame, width = 50, height = height)
canvas.place(x = 250, y = 0)

def lengthen_widget(widget, init_height, final_height, increment,decrement, ms = 10, change = 1):

    height = init_height

    middle_height = ((final_height - init_height)/2) + init_height

    lengthen_widget_child(widget,height,middle_height,final_height,increment,decrement,ms,change)


def lengthen_widget_child(widget, height, middle_height, final_height, increment,decrement, ms = 10, change = 1):

    if(height <= final_height):

        widget.configure(fg_color = 'blue')

        change = 15 * (math.sqrt(math.pow(math.sin(height/final_height * math.pi),2)))
        height+=change
        #print("Sin : " + str(change))
        #print("Height : " + str(height))
        #print("Middle Height : " + str(middle_height))
        widget.configure(height=height)
        root.after(ms, lambda : lengthen_widget_child(canvas,height, middle_height, final_height,increment,decrement,ms,change))

    elif(height <= final_height):

        widget.configure(fg_color = 'pink')

        change/=decrement
        height+=change
        print(height)
        widget.configure(height=height)
        root.after(ms, lambda : lengthen_widget_child(canvas,height, middle_height, final_height,increment,decrement,ms,change))



lengthen_widget(canvas,1,498,1.05,1.05,1,1)

root.mainloop()