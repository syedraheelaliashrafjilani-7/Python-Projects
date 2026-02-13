import requests

api_key = '411cf9d15f5a093f552bc1f7d12acf17'

user_input = input("Enter City Name: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
weather =  weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"The Weather in {user_input} is: {weather}")
print(f"The Temperature in {user_input} is: {temp}°F")