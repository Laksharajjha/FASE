# Weather Monitor program

import extrakinter
import customtkinter
import tkinter
from PIL import Image
import SuggTestingArea.SuggestionBoxes2 as SuggestionBoxes2

SHORT_FRAME = 122
TALL_FRAME = 526
STEPS = 2

class BeeFASE:

    def __init__(self, master):

        self.root = master
        self.root.geometry('500x574')
        self.root.title('BeeFase')

        self.input = ''

        self.set_frame(SHORT_FRAME)
        self.frame_height = SHORT_FRAME

        self.place_sbar(self.input)
        self.place_button()

        self.Sugg = SuggestionBoxes2.SuggestionBox(self.root,x = 50,y = 50,widget=self.search_bar,options = ['India'],textsize=18)
        self.Sugg.update_suggestions()
    
    def set_frame(self, height):

        self.search_frame = customtkinter.CTkFrame(self.root, width=449, height=height, bg_color='#8C52FF', fg_color='#CDC2FE', corner_radius=25)
        self.search_frame.place(y=23, x=29)

    def place_sbar(self,input):

        self.search_bar = customtkinter.CTkEntry(self.search_frame, width=314, height=62, corner_radius=25, bg_color='#CDC2FE', border_width=0, font=('Arial',18))
        self.search_bar.insert(0,self.input)
        self.search_bar.place(y=27, x=23)

    def place_button(self):

        self.button_image = customtkinter.CTkImage(light_image=Image.open("Button2.png"), dark_image=Image.open("Button2.png"), size=(23, 23))
        self.button = customtkinter.CTkButton(self.root, command=self.enlarge_frame_setup, height=50, width=10,corner_radius=65, bg_color='#CDC2FE', fg_color='white', text='', image=self.button_image)
        self.button.place(x=382, y=57)

    def enlarge_frame(self):

        if (self.frame_height < TALL_FRAME):

            self.search_frame.destroy()
            self.frame_height += ((TALL_FRAME - SHORT_FRAME) / STEPS)
            self.set_frame(height=self.frame_height)
            self.root.after(10, self.enlarge_frame)

        self.weather_label = customtkinter.CTkLabel(self.search_frame, text='')

    def place_stats(self, weather, temperature,city, windspeed):

        self.weather_label.destroy()
        self.weather = customtkinter.CTkImage(light_image=Image.open('Website\images\\' + str(weather) + '.png'), dark_image=Image.open('Website\images\\' + str(weather) + '.png'), size=(206, 195))

        self.weather_label = customtkinter.CTkLabel(self.search_frame, image=self.weather, text='')
        self.weather_label.place(x=133, y=102)

        self.temperature_label = customtkinter.CTkLabel(self.root, bg_color='#CDC2FE', fg_color='#CDC2FE', font=('Arial', 52), text = str(temperature) + " C", text_color='white')
        self.temperature_label.place(x=209, y=305)

        self.city_label = customtkinter.CTkLabel(self.root, bg_color='#CDC2FE', fg_color='#CDC2FE', font=('Arial', 35), text = city, text_color='white')
        self.city_label.place(x=209, y=363)

        self.humidity_image = customtkinter.CTkImage(light_image=Image.open('Website/images/humidity.png'),dark_image=Image.open('Website/images/humidity.png'),size = (40,40))
        self.humidity_image_label = customtkinter.CTkLabel(self.search_frame, bg_color='#CDC2FE',fg_color='#CDC2FE',text_color='white',image = self.humidity_image, text = '')
        self.humidity_image_label.place(x = 50, y = 430)

        self.wind_image = customtkinter.CTkImage(light_image=Image.open('Website\images\wind.png'),dark_image=Image.open('Website\images\wind.png'),size = (40,40))
        self.wind_image_label = customtkinter.CTkLabel(self.search_frame, bg_color='#CDC2FE', fg_color= '#CDC2FE', image = self.wind_image, text = '')
        self.wind_image_label.place(x = 295, y = 426)

        self.wind_speed_label1 = customtkinter.CTkLabel(self.search_frame, text = str(windspeed) + " kmph", bg_color='#CDC2FE',fg_color='#CDC2FE',text_color='white', font = ('Arial',20))
        self.wind_speed_label1.place(x = 345, y = 426)

        self.wind_speed_label2 = customtkinter.CTkLabel(self.search_frame, text = "Wind Speed", bg_color='#CDC2FE',fg_color='#CDC2FE',text_color='white', font = ('Arial',16))
        self.wind_speed_label2.place(x = 345, y = 450)

    def del_sugg(self):

        del self.Sugg

    def make_sugg(self):
    
        self.Sugg = SuggestionBoxes2.SuggestionBox(self.root,x = 50,y = 50,widget=self.search_bar,options = ['India'],textsize=18)
        self.Sugg.update_suggestions()
    
    def enlarge_frame_setup(self):

        #self.root.after(10,lambda: self.del_sugg)

        self.input = self.search_bar.get()

        if (self.frame_height < TALL_FRAME):

            self.search_bar.destroy()
            self.button.destroy()

        self.enlarge_frame()

        if (self.frame_height < TALL_FRAME):

            self.root.after(10, self.place_sbar,self.input)
            self.root.after(10, self.place_button)


        self.root.after(10, self.place_stats, 'clouds',69,'Sydney', 15)


def main():

    root = customtkinter.CTk(fg_color='#8C52FF')
    Window = BeeFASE(root)

    
    root.mainloop()


if __name__ == '__main__':
    main()
