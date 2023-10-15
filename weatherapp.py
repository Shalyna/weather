import requests

apiKey = "a1a5542c4d6454ba273f76c9c270ba4b"
city = input("Enter city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = round((data["main"]["temp"] - 273.15) * 1.8 + 32)
    feels = round((data["main"]["feels_like"]  - 273.15) * 1.8 + 32)
    minTemp = round((data["main"]["temp_min"]  - 273.15) * 1.8 + 32)
    maxTemp = round((data["main"]["temp_max"]  - 273.15) * 1.8 + 32)
    desc = data["weather"][0]["description"].capitalize()
    currentData = (f"Current temperature: {temp}°F\nFeels like: {feels}°F\nMinimum temperature: {minTemp}°F\nMaximum temperature: {maxTemp}°F\nDesription: {desc}")
    print(currentData)


