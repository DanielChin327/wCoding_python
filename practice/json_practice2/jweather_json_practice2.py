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
        print(f"\nWeather Information for {city.capitalize()}:")
        print(f"Longitude: {longitude}")
        print(f"Latitude: {latitude}")
        print(f"Main Weather: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Minimum Temperature: {temp_min}°C")
        print(f"Maximum Temperature: {temp_max}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Cloudiness: {cloudiness}%\n")
    else:
        print("Sorry, couldn't fetch the weather data. Please check the city name and try again.\n")
