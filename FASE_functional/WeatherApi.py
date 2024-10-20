import requests

class WeatherApi:

    def __init__(self,city):

        self.unavailable = False

        api_endpoint = 'https://api.weatherapi.com/v1/current.json'
        api_key = '093e8dd1b9634bf8906152344231309' 

        params = {
            'key': api_key,
            'q': city, 
            'units': 'metric', 
        }

        response = requests.get(api_endpoint, params=params)

        data = response.json()
        print(data)

        if response.status_code != 200 or data == []:
            self.unavailable = True
            return
        
        self.rainfall = response.json()['current']['precip_mm']

    def getRainfall(self):

        if self.unavailable:
            return "Unavailable"
        else:   
            return format(self.rainfall,".1f") + " mm"

def main():

    # Replace with your actual weather API endpoint and API key (if required)
    api_endpoint = 'https://api.weatherapi.com/v1/current.json'  # Example endpoint
    api_key = '093e8dd1b9634bf8906152344231309'  # Replace with your API key

    # Parameters for the API request (e.g., location, units, etc.)
    params = {
        'key': api_key,
        'q': 'London',  # Replace with the desired location
        'units': 'metric',  # Replace with the desired units (e.g., metric, imperial)
    }

    try:
        # Make the GET request to the weather API
        response = requests.get(api_endpoint, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract and print relevant weather information
            location = data['location']['name']
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']

            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {condition}")

            print(data)
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except KeyError as e:
        print(f"Failed to parse response data. KeyError: {e}")

if __name__ == '__main__':
    main()
