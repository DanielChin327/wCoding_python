import requests

example_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=tokyo&appid=89638d41ac4d76e85c0eca18872b79bb"


# city = input("Write a City Name: ")
url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="
api_key = '89638d41ac4d76e85c0eca18872b79bb'

while True:
    # Prompt user for city name
    city = input("Write a City Name (or type 'end' to quit): ")

    # Check if the user wants to end the loop
    if city.lower() == 'end':
        print("Exiting the program.")
        break

    # Construct the full URL
    full_url = f"{url}{city}&appid={api_key}"

    # Make the HTTP request
    response = requests.get(full_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
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
