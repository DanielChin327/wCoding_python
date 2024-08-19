import requests

example_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=tokyo&appid=89638d41ac4d76e85c0eca18872b79bb"


# city = input("Write a City Name: ") #not needed with the loop.
url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="
api_key = '89638d41ac4d76e85c0eca18872b79bb'

while True:

    city = input("Write a City Name (or type 'end' or 'quit' to stop): ")

    if city.lower() == 'end' or city.lower() == 'quit':
        print("Exiting the program.")
        break

    full_url = f"{url}{city}&appid={api_key}"

    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        # Extract the required data
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        cloudiness = data['clouds']['all']

        # Print the extracted data

        print(f"\nHere's the weather update for {city.capitalize()}:\n")
        print(f"Today's main weather condition is {main_weather}.")
        print(f"The temperature is {temperature}°C, but will feel like {feels_like}°C.")
        print(f"Expect a high of {temp_max}°C and a low of {temp_min}°C.")
        print(f"Humidity levels are at {humidity}%.")
        print(f"Wind speeds are around {wind_speed} m/s, with cloud coverage at {cloudiness}%.\n")

    else:
        print("Sorry, couldn't fetch the weather data. Please check the city name and try again.\n")


'''
print full data looks like this:

{'coord': {'lon': 139.6917, 'lat': 35.6895}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 34.29, 'feels_like': 41.29, 'temp_min': 32.59, 'temp_max': 34.89, 'pressure': 1010, 'humidity': 64, 'sea_level': 1010, 'grnd_level': 1009}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 210}, 'clouds': {'all': 75}, 'dt': 1724053385, 'sys': {'type': 2, 'id': 2001249, 'country': 'JP', 'sunrise': 1724011401, 'sunset': 1724059605}, 'timezone': 32400, 'id': 1850144, 'name': 'Tokyo', 'cod': 200}
'''
