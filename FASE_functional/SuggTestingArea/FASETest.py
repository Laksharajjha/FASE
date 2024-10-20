# Weather Monitor program

import json
import extrakinter
import customtkinter
import tkinter
from PIL import Image
import OpenWeather
import SuggestionBoxes2

SHORT_FRAME = 122
TALL_FRAME = 650
STEPS = 2

# Old FGCOLOUR = '#8C52FF'
# Old BGCOLOUR = '#CDC2FE'

FGCOLOUR = '#9C38FF'
BGCOLOUR = '#1B0D52'

weatherImagePrep = {'Clouds':'clouds','Clear':'clear','Rain':'rain','Drizzle':'drizzle','Mist':'mist','Haze':'mist'}

class BeeFASE:

    def __init__(self, master):

        with open('cities.json','r') as infile:
            self.cities = json.load(infile)

        self.root = master
        self.root.geometry('500x700')
        self.root.title('FaseTest')

        self.input = ''

        self.set_frame(SHORT_FRAME)
        self.frame_height = SHORT_FRAME

        self.place_sbar(self.input)
        self.place_button()

        self.replace_suggestions()

    def replace_suggestions(self):

        self.Sugg = SuggestionBoxes2.SuggestionBox(self.root,x=52,y=33,widget=self.search_bar,options=self.cities,textsize=16)
        self.Sugg.update_suggestions()


    def set_frame(self, height):

        self.search_frame = customtkinter.CTkFrame(self.root, width=449, height=height, bg_color=BGCOLOUR, fg_color=FGCOLOUR, corner_radius=25)
        self.search_frame.place(y=23, x=29)

    def place_sbar(self,input):

        self.search_bar = customtkinter.CTkEntry(self.search_frame, width=314, height=62, corner_radius=25, bg_color=FGCOLOUR, border_width=0, font=('Arial',18))
        self.search_bar.insert(0,self.input)
        self.search_bar.place(y=27, x=23)

    def place_button(self):

        self.button_image = customtkinter.CTkImage(light_image=Image.open("Button2.png"), dark_image=Image.open("Button2.png"), size=(23, 23))
        self.button = customtkinter.CTkButton(self.root, command=self.button_press, height=50, width=10,corner_radius=65, bg_color=FGCOLOUR, fg_color='white', text='', image=self.button_image)
        self.button.place(x=382, y=57)

    def place_stats(self, weather, temperature,city, windspeed,humidity):

        weather = customtkinter.CTkImage(light_image=Image.open('Website\images\\' + str(weather) + '.png'), dark_image=Image.open('Website\images\\' + str(weather) + '.png'), size=(206, 195))

        weather_label = customtkinter.CTkLabel(self.search_frame, image=weather, text='')
        weather_label.place(x=122, y=102)

        temperature_label = customtkinter.CTkLabel(self.root, bg_color=FGCOLOUR, fg_color=FGCOLOUR, font=('Arial', 52), text = str(temperature) + "°C", text_color='white', anchor = 'center', width = 400)
        temperature_label.place(x=54, y=305)

        city_label = customtkinter.CTkLabel(self.root, bg_color=FGCOLOUR, fg_color=FGCOLOUR, font=('Arial', 35), text = city.capitalize(), text_color='white',anchor = 'center', width = 400)
        city_label.place(x = 51, y = 359)

        humidity_image = customtkinter.CTkImage(light_image=Image.open('Website/images/humidity.png'),dark_image=Image.open('Website/images/humidity.png'),size = (40,40))
        humidity_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = humidity_image, text = '')
        humidity_image_label.place(x = 40, y = 430)

        wind_image = customtkinter.CTkImage(light_image=Image.open('Website\images\wind.png'),dark_image=Image.open('Website\images\wind.png'),size = (40,40))
        wind_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR, fg_color= FGCOLOUR, image = wind_image, text = '')
        wind_image_label.place(x = 265, y = 426)

        wind_speed_label1 = customtkinter.CTkLabel(self.search_frame, text = str(windspeed) + " kmph", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), anchor = 'w', width = 100)
        wind_speed_label1.place(x = 315, y = 424)

        wind_speed_label2 = customtkinter.CTkLabel(self.search_frame, text = "Wind Speed", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        wind_speed_label2.place(x = 317, y = 447)

        humidity_label1 = customtkinter.CTkLabel(self.search_frame, text = str(humidity) + " %", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), width = 100, anchor = 'w')
        humidity_label1.place(x = 90, y = 425)

        humidity_label2 = customtkinter.CTkLabel(self.search_frame, text = "Humidity", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        humidity_label2.place(x = 92, y = 448)
        
        #extrakinter.widget_move(self.root,self.temperature_label,115,305)
    
    def button_press(self):

        self.Sugg.Stop = True
        del self.Sugg

        self.input = self.search_bar.get()
        #print(self.cities)

        if (self.input.casefold() not in self.cities):
                return

        if (self.frame_height < TALL_FRAME):

            self.search_bar.destroy()
            self.button.destroy()

            self.search_frame.configure(height = TALL_FRAME)

            self.place_sbar(self.input)
            self.place_button()

        self.frame_height = TALL_FRAME
        Stats = OpenWeather.Stats(self.input)

        self.replace_suggestions()

        self.place_stats(weatherImagePrep[Stats.getweather()],int(Stats.gettemp() - 273.15),self.input,Stats.getwindspeed() ,Stats.gethumidity())



def main():

    root = customtkinter.CTk(fg_color=BGCOLOUR)
    Window = BeeFASE(root)
    
    root.mainloop()


if __name__ == '__main__':
    main()
