import requests

class Stats:

    def __init__(self,city):
        
        API_key = '5f0ccfa4ac7421ca9388ae704b47aa99'
        limit = 1

        self.unavailable = False

        URL = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_key}'

        response = requests.get(URL)
        data = response.json()

        if response.status_code != 200 or data == []:
             self.unavailable = True
             return

        lon = data[0]['lon']
        lat = data[0]['lat']

        URL = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}'

        response = requests.get(URL)
        data = response.json()

        if response.status_code != 200 or data == []:
            self.unavailable = True
            return

        self.ammonia = data['list'][0]['components']['nh3']
        self.aqi = data['list'][0]['main']['aqi']

    def getAmmonia(self):
         
        if(self.unavailable == True):
            return 'Unavailable'
        else:
            return (str(self.ammonia) + ' μg/m3')
    
    def getAirQualityIndex(self):
         
        Qualitative = {1:'Good',2:'Fair',3:'Moderate',4:'Poor',5:'Very Poor'}

        if(self.unavailable == True):
            return 'Unavailable'
        else:
            return Qualitative[self.aqi]

def main():

    
        API_key = '5f0ccfa4ac7421ca9388ae704b47aa99'
        city = 'Trichy'
        limit = 1


        URL = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_key}'

        response = requests.get(URL)
        data = response.json()

        print(data)

        lon = data[0]['lon']
        lat = data[0]['lat']

        URL = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}'

        response = requests.get(URL)
        data = response.json()

        print(data)

        print("\n" + str(data['list'][0]['main']['aqi']))
        print("\n" + str(data['list'][0]['components']['nh3']))

        S = Stats(city)
        print(S.getAmmonia())
        print(S.getAirQualityIndex())

if __name__ == "__main__":
    main()