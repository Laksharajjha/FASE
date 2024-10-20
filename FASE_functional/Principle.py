import tkinter
import customtkinter 
from PIL import Image

def increase():
    global i
    global image_label
    global image
    i+=10

    del image

    image = customtkinter.CTkImage(light_image=Image.open('Untitled_design-removebg-preview.png'),dark_image=Image.open('Untitled_design-removebg-preview.png'),size = (200+i,574))
  
    print(200+i)
    image_label.destroy()
    image_label = customtkinter.CTkLabel(root, image = image)
    image_label.pack()

def window():

    global root
    global i
    global image_label
    global image
    i = 0
    root = customtkinter.CTk()
    root.geometry('500x574')

    image = customtkinter.CTkImage(light_image=Image.open('Untitled_design-removebg-preview.png'),dark_image=Image.open('Untitled_design-removebg-preview.png'),size = (200,574))
    
    image_label = customtkinter.CTkLabel(root, image = image)
    image_label.pack()

    increase_button = customtkinter.CTkButton(root, width=20,height=20,corner_radius=6,command=increase)
    increase_button.pack()


def main():

    window()

    root.mainloop()


if __name__ == "__main__":
    main()