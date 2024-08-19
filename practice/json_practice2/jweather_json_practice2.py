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
