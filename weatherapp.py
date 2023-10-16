from tkinter import *
import requests
from datetime import datetime

root = Tk()
root.title("Weather App")
root.geometry("400x600")
root.resizable(0,0)
cityValue= StringVar()

def currentWeather():
    apiKey = "a1a5542c4d6454ba273f76c9c270ba4b"
    city = cityValue.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
    response = requests.get(url)
    tfield.delete("1.0", "end")

    if response.status_code == 200:
        data = response.json()
        temp = round((data["main"]["temp"] - 273.15) * 1.8 + 32)
        feels = round((data["main"]["feels_like"]  - 273.15) * 1.8 + 32)
        minTemp = round((data["main"]["temp_min"]  - 273.15) * 1.8 + 32)
        maxTemp = round((data["main"]["temp_max"]  - 273.15) * 1.8 + 32)
        desc = data["weather"][0]["description"].capitalize()
        weatherData = (f"Current temperature: {temp}°F\nFeels like: {feels}°F\nMinimum temperature: {minTemp}°F\nMaximum temperature: {maxTemp}°F\nDesription: {desc}")
    else:
        weatherData = (f"'{city}' was not found! Please enter a valid city name.")

    tfield.insert(INSERT, weatherData) 

city_name = Label(root, text="Enter City Name: ", font="Arial 12 bold").pack(pady=10)
city_inp = Entry(root, textvariable=cityValue, width=24, font="Arial 14 bold").pack()
Button(root, command = currentWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

weather = Label(root, text=f"The current weather is:", font="Arial 12 bold").pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
