import customtkinter as ctk
import math
import time


def lengthen_widget(root,widget, init_height, final_height,speed,ms = 10):

    height = init_height

    #lengthen_widget_child(root,widget,height,speed,final_height,ms)

    while(height <= final_height):

        print("hi")
        
        change = speed * (math.sqrt(math.pow(math.sin(height/final_height * math.pi),2)))
        height+=change
        widget.configure(height=height)
        time.sleep(1)


def lengthen_widget_child(root,widget, height, speed, final_height, ms = 10):

    if(height <= final_height):

        change = speed * (math.sqrt(math.pow(math.sin(height/final_height * math.pi),2)))
        height+=change
        widget.configure(height=height)
        root.after(ms, lambda : lengthen_widget_child(root,widget,height, speed, final_height,ms))

def main():

    root = ctk.CTk()
    root.geometry("500x500")
    root.title("Animation Test")

    frame = ctk.CTkFrame(root,width = 500, height = 500, bg_color='pink')
    frame.pack()

    height = 20
    increment = 1

    canvas = ctk.CTkFrame(frame, width = 50, height = height, fg_color='red')
    canvas.place(x = 250, y = 0)

    lengthen_widget(root,canvas,1,498,10,1)

    root.mainloop()

if __name__ == '__main__':
    main()