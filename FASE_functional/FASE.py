# Weather Monitor program

import json
import extrakinter
import customtkinter
from PIL import Image
import OpenWeather
import OpenWeather2
import UVStats
import SuggestionBoxes
import time

SHORT_FRAME = 122
TALL_FRAME = 680
STEPS = 2

# Old FGCOLOUR = '#8C52FF'
# Old BGCOLOUR = '#CDC2FE'

FGCOLOUR = '#9C38FF'
BGCOLOUR = '#1B0D52'

class FASE:

    def __init__(self, master):

        with open('cities.json','r') as infile:
            self.cities = set(json.load(infile))

        self.root = master
        self.root.geometry('500x730')
        self.root.title('FaseTest')

        self.input = ''

        self.set_frame(SHORT_FRAME)
        self.frame_height = SHORT_FRAME

        self.place_sbar(self.input)
        self.place_button()

        self.replace_suggestions()

        self.root.bind('<Return>',lambda x: self.button_press())

    def replace_suggestions(self):

        self.Sugg = SuggestionBoxes.SuggestionBox(self.root,
                                                  x=48,y=33,
                                                  widget=self.search_bar,
                                                  options=self.cities,
                                                  textsize=16)
        self.Sugg.update_suggestions()


    def set_frame(self, height):

        self.search_frame = customtkinter.CTkFrame(self.root, width=449, height=height, bg_color=BGCOLOUR, fg_color=FGCOLOUR, corner_radius=25)
        self.search_frame.place(y=23, x=25)

    def place_sbar(self,input):

        self.search_bar = customtkinter.CTkEntry(self.search_frame, width=247, height=62, corner_radius=25, bg_color=FGCOLOUR, border_width=0, font=('Arial',18))
        self.search_bar.insert(0,self.input)
        self.search_bar.place(y=27, x=23)

    def place_button(self):

        self.button_image = customtkinter.CTkImage(light_image=Image.open("Button2.png"), dark_image=Image.open("Button2.png"), size=(23, 23))
        self.button = customtkinter.CTkButton(self.root, command=self.button_press, height=45, width=10,corner_radius=65, bg_color=FGCOLOUR, fg_color='white', text='', image=self.button_image, hover_color='#FF66C4')
        self.button.place(x=387, y=59)

        self.button_image = customtkinter.CTkImage(light_image=Image.open("pointer.png"), dark_image=Image.open("pointer.png"), size=(18, 23))
        self.button_2 = customtkinter.CTkButton(self.root, command=self.button_press, height=45, width=10,corner_radius=65, bg_color=FGCOLOUR, fg_color='white', text='', image=self.button_image, hover_color='#FF66C4')
        self.button_2.place(x=309, y=59)


    def place_stats(self, weather, temperature,city, windspeed,humidity,ammonia,aqi, uv, feelslike):

        if(weather != 'Unavailable'):
            weather = customtkinter.CTkImage(light_image=Image.open('Website\images\\' + str(weather) + '.png'), dark_image=Image.open('Website\images\\' + str(weather) + '.png'), size=(206, 195))
            weather_label = customtkinter.CTkLabel(self.search_frame, image=weather, text='')
            weather_label.place(x=122, y=102)
        else:
            empty = customtkinter.CTkFrame(self.search_frame,width = 220, height = 220,bg_color=FGCOLOUR,fg_color=FGCOLOUR)
            empty.place(x = 110,y = 97)

        temperature_label = customtkinter.CTkLabel(self.root, bg_color=FGCOLOUR, fg_color=FGCOLOUR, font=('Arial', 52), text = temperature, text_color='white', anchor = 'center', width = 400)
        temperature_label.place(x=54, y=305)

        city_label = customtkinter.CTkLabel(self.root, bg_color=FGCOLOUR, fg_color=FGCOLOUR, font=('Arial', 35), text = city.title(), text_color='white',anchor = 'center', width = 400)
        city_label.place(x = 54, y = 359)

        humidity_image = customtkinter.CTkImage(light_image=Image.open('Website/images/humidity.png'),dark_image=Image.open('Website/images/humidity.png'),size = (40,40))
        humidity_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = humidity_image, text = '')
        humidity_image_label.place(x = 40, y = 430)

        wind_image = customtkinter.CTkImage(light_image=Image.open('Website\images\wind.png'),dark_image=Image.open('Website\images\wind.png'),size = (40,40))
        wind_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR, fg_color= FGCOLOUR, image = wind_image, text = '')
        wind_image_label.place(x = 265, y = 426)

        wind_speed_label1 = customtkinter.CTkLabel(self.search_frame, text = windspeed, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), anchor = 'w', width = 130)
        wind_speed_label1.place(x = 315, y = 424)

        wind_speed_label2 = customtkinter.CTkLabel(self.search_frame, text = "Wind Speed", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        wind_speed_label2.place(x = 317, y = 447)

        humidity_label1 = customtkinter.CTkLabel(self.search_frame, text = humidity, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), width = 130, anchor = 'w')
        humidity_label1.place(x = 90, y = 425)

        humidity_label2 = customtkinter.CTkLabel(self.search_frame, text = "Humidity", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        humidity_label2.place(x = 92, y = 448)

        #soil_image = customtkinter.CTkImage(light_image=Image.open('soil.png'),dark_image=Image.open('soil.png'),size = (50,50))
        #soil_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = soil_image, text = '')
        #soil_image_label.place(x = 35, y = 506)

        #soil_type_label1 = customtkinter.CTkLabel(self.search_frame, text = "NULL", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), width = 130, anchor = 'w')
        #soil_type_label1.place(x = 92, y = 505)

        #soil_type_label2 = customtkinter.CTkLabel(self.search_frame, text = "Soil Type", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        #soil_type_label2.place(x = 92, y = 528)

        UV_image = customtkinter.CTkImage(light_image=Image.open('UV.png'),dark_image=Image.open('UV.png'),size = (50,50))
        UV_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = UV_image, text = '')
        UV_image_label.place(x = 35, y = 506)

        UV_type_label1 = customtkinter.CTkLabel(self.search_frame, text = uv, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), width = 130, anchor = 'w')
        UV_type_label1.place(x = 92, y = 505)

        UV_type_label2 = customtkinter.CTkLabel(self.search_frame, text = "UV Index", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        UV_type_label2.place(x = 92, y = 528)

        ammonia_image = customtkinter.CTkImage(light_image=Image.open('ammonia.png'),dark_image=Image.open('ammonia.png'),size = (50,50))
        ammonia_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = ammonia_image, text = '')
        ammonia_image_label.place(x = 259, y = 508)

        ammonia_label1 = customtkinter.CTkLabel(self.search_frame, text = ammonia, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), anchor = 'w', width = 130)
        ammonia_label1.place(x = 315, y = 505)

        ammonia_label2 = customtkinter.CTkLabel(self.search_frame, text = "Ammonia", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        ammonia_label2.place(x = 317, y = 529)

        aqi_image = customtkinter.CTkImage(light_image=Image.open('aqi.png'),dark_image=Image.open('aqi.png'),size = (50,50))
        aqi_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = aqi_image, text = '')
        aqi_image_label.place(x = 35, y = 588)

        aqi_label1 = customtkinter.CTkLabel(self.search_frame, text = aqi, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), width = 130, anchor = 'w')
        aqi_label1.place(x = 92, y = 585)

        aqi_label2 = customtkinter.CTkLabel(self.search_frame, text = "Air Quality", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        aqi_label2.place(x = 92, y = 608)

        feelslike_image = customtkinter.CTkImage(light_image=Image.open('rain.png'),dark_image=Image.open('rain.png'),size = (50,50))
        feelslike_image_label = customtkinter.CTkLabel(self.search_frame, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white',image = feelslike_image, text = '')
        feelslike_image_label.place(x = 259, y = 588)

        feelslike_label1 = customtkinter.CTkLabel(self.search_frame, text = feelslike, bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',20), anchor = 'w', width = 130)
        feelslike_label1.place(x = 315, y = 585)

        feelslike_label2 = customtkinter.CTkLabel(self.search_frame, text = "Feels Like", bg_color=FGCOLOUR,fg_color=FGCOLOUR,text_color='white', font = ('Arial',16))
        feelslike_label2.place(x = 317, y = 608)

        
        #extrakinter.widget_move(self.root,ammonia_image_label,265,507)
    
    def button_press(self):

        #print(str(time.localtime().tm_hour) + "-"  + str(time.localtime().tm_min) + "-" + str(time.localtime().tm_sec))
        self.input = self.search_bar.get()
        #print(self.cities)

        if (self.input.casefold() not in self.cities):
                return
        
        self.Sugg.stop_suggestions()
        del self.Sugg

        if (self.frame_height < TALL_FRAME):

            self.search_bar.destroy()
            self.button.destroy()
            self.button_2.destroy()

            self.search_frame.configure(height = TALL_FRAME)

            self.place_sbar(self.input)
            self.place_button()

        self.frame_height = TALL_FRAME

        print(str(time.localtime().tm_hour) + "-"  + str(time.localtime().tm_min) + "-" + str(time.localtime().tm_sec))
        Stats = OpenWeather.Stats(self.input)
        #print(str(time.localtime().tm_hour) + "-"  + str(time.localtime().tm_min) + "-" + str(time.localtime().tm_sec))
        UV = UVStats.UVStats(self.input).getUV()
        print(str(time.localtime().tm_hour) + "-"  + str(time.localtime().tm_min) + "-" + str(time.localtime().tm_sec))
        #rain = WeatherApi.WeatherApi(self.input).getRainfall()


        self.replace_suggestions()

        self.place_stats(
                        Stats.getweather(),
                        Stats.gettemp(),
                        self.input,
                        Stats.getwindspeed(),
                        Stats.gethumidity(),
                        Stats.getAmmonia(),
                        Stats.getAirQualityIndex(),
                        Stats.getUV(),
                        Stats.getfeeltemp()
        )

        #print(str(time.localtime().tm_hour) + "-"  + str(time.localtime().tm_min) + "-" + str(time.localtime().tm_sec))



def main():

    root = customtkinter.CTk(fg_color=BGCOLOUR)
    Window = FASE(root)
    
    root.mainloop()


if __name__ == '__main__':
    main()
