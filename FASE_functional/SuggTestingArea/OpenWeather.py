import requests

class Stats:

    def __init__(self,city_name):
        
        api_key = '5f0ccfa4ac7421ca9388ae704b47aa99'
        base_url = 'https://api.openweathermap.org/data/2.5/'

        endpoint = 'weather'

        url = f'{base_url}{endpoint}?q={city_name}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            self.data = response.json()  
        else:
            print('Error:', response.status_code)

    def gettemp(self):
        return float(self.data['main']['temp'])
    
    def gethumidity(self):
        return float(self.data['main']['humidity'])
    
    def getwindspeed(self):
        return float(self.data['wind']['speed'])
    
    def getweather(self):
        return str(self.data['weather'][0]['main'])

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
    print(int(values['main']['temp']))



if __name__ == '__main__':
    main()