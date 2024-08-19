import requests


example_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=tokyo&appid=89638d41ac4d76e85c0eca18872b79bb"


city = input("Write a City Name: ")
url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="
api_key = '89638d41ac4d76e85c0eca18872b79bb'

full_url = f"{url}{city}&appid={api_key}"

print(full_url)
