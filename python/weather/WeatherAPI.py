import requests
api_key='b1121fd60d32d8514e909efef420124f'
UserInput = input("Enter the City : ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={UserInput}&appid={api_key}")
if weather_data.json()['cod'] == '404':
    print("No Ciyt Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = round(weather_data.json()['main']['temp'])
    print(f"The weather in {UserInput} is : {weather}")
    print(f"The temperature in {UserInput} is : {temperature}°F")