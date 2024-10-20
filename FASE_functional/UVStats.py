import requests
import time

class UVStats:

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

        self.lon = data[0]['lon']
        self.lat = data[0]['lat']

        self.prepUV()

    def prepUV(self):

        url = "https://api.openuv.io/api/v1/uv"
    
        headers = {
            "x-access-token": "openuv-cmwcayrlmhu3195-io",
            "Content-Type": "application/json"
        }

        params = {
            "lat": self.lat,
            "lng": self.lon,
            "alt": 100,
            "dt": ""
        }

        response = requests.get(url, headers=headers, params=params)

        data = response.json()

        if response.status_code != 200 or data == []:
             self.unavailable = True
             return

        self.uv_index = data['result']['uv']

    def getUV(self):

        if self.unavailable == True:
            return "Unavailable"
        else:
            return format(self.uv_index,".2f")

def main_():

    UV = UVStats("London")
    print(UV.getUV())

if __name__ == '__main__':
    main_()