from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Sacramento"):
    try:
        request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'
        print(f"Requesting URL: {request_url}")
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        weather_data = response.json()
        return weather_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return None

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Sacramento"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)