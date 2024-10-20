import customtkinter
from frameExpandFinal import lengthen_widget

root = customtkinter.CTk()
root.geometry("200x200")
root.title("Testing sin")

def canvas_expand(root):

    canvas = customtkinter.CTkCanvas(height = 20, width = 300, bg = 'pink')
    canvas.pack()

    lengthen_widget(root,canvas, 1, 300, 10, 10)

def frame_expand(root):

    frame = customtkinter.CTkCanvas(height = 20, width = 300, bg = 'blue')
    frame.pack()

    lengthen_widget(root,frame, 1, 300, 10, 10)

#canvas_expand(root)
frame_expand(root)

#lengthen_widget(root, frame, 20, 200, 2,1)

root.mainloop()