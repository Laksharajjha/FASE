import requests

class Stats:

    def __init__(self,city_name):
        
        api_key = '5f0ccfa4ac7421ca9388ae704b47aa99'
        base_url = 'https://api.openweathermap.org/data/2.5/'

        endpoint = 'weather'

        self.unavailable = False
        self.unavailableB = False
        self.unavailableUV = False

        url = f'{base_url}{endpoint}?q={city_name}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()  
            if(data == []):
                self.unavailable = True
                return
        else:
            print('Error:', response.status_code)
            self.unavailable = True
            return

        self.temp = data['main']['temp']
        self.humidity = data['main']['humidity']
        self.windspeed = data['wind']['speed']
        self.weather = data['weather'][0]['main']
        self.feeltemp = data['main']['feels_like']

        lon = data['coord']['lon']
        lat = data['coord']['lat']

        URL = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'

        response = requests.get(URL)
        data = response.json()

        if response.status_code != 200 or data == []:
            self.unavailableB = True
            return

        self.ammonia = data['list'][0]['components']['nh3']
        self.aqi = data['list'][0]['main']['aqi']

        url = "https://api.openuv.io/api/v1/uv"
    
        headers = {
            "x-access-token": "openuv-cmwcayrlmhu3195-io",
            "Content-Type": "application/json"
        }

        params = {
            "lat": lat,
            "lng": lon,
            "alt": 100,
            "dt": ""
        }

        response = requests.get(url, headers=headers, params=params)

        data = response.json()

        if response.status_code != 200 or data == []:
             self.unavailableUV = True
             return

        self.uv_index = data['result']['uv']


    def gettemp(self):
        
        if(self.unavailable == True):
            return 'City Not Found'
        else:
            return (format(self.temp - 273.15,".1f") + " °C")
    
    def getfeeltemp(self):
        
        if(self.unavailable == True):
            return 'City Not Found'
        else:
            return (format(self.feeltemp - 273.15,".1f") + " °C")

    def gethumidity(self):

        if(self.unavailable == True):
            return 'Unavailable'
        else:
            return (str(self.humidity) + " %")
    
    def getwindspeed(self):

        if(self.unavailable == True):
            return 'Unavailable'
        else:
            return (str(self.windspeed) + " kmph")
    
    def getweather(self):

        weatherImagePrep = {
                    'Clouds':'clouds',
                    'Clear':'clear',
                    'Rain':'rain',
                    'Drizzle':'drizzle',
                    'Mist':'mist',
                    'Haze':'mist',
                    'Thunderstorm':'rain'
                    }
        
        if(self.unavailable == True):
            return 'Unavailable'
        else:
            return weatherImagePrep[self.weather]

    def getAmmonia(self):
         
        if((self.unavailable == True) or (self.unavailableB == True)):
            return 'Unavailable'
        else:
            return (str(self.ammonia) + ' μg/m3')
    
    def getAirQualityIndex(self):
         
        Qualitative = {1:'Good',2:'Fair',3:'Moderate',4:'Poor',5:'Very Poor'}

        if((self.unavailable == True) or (self.unavailableB == True)):
            return 'Unavailable'
        else:
            return Qualitative[self.aqi]

    def getUV(self):

        if((self.unavailable == True) or (self.unavailableUV == True)):
            return "Unavailable"
        else:
            return format(self.uv_index,".2f")


def main():

    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = '5f0ccfa4ac7421ca9388ae704b47aa99'
    base_url = 'https://api.openweathermap.org/data/2.5/'

    # Example: Get current weather by city name (London in this case)
    city_name = 'London'
    endpoint = 'weather'

    # Construct the full API URL
    url = f'{base_url}{endpoint}?q={city_name}&appid={api_key}'

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        print(data)
    else:
        print('Error:', response.status_code)

    values = response.json()
    print(values['coord'])
    print(values['coord']['lon'])
    print(values['coord']['lat'])



if __name__ == '__main__':
    main()