import requests                                                            
import os                     
from datetime import datetime                                              
from dotenv import load_dotenv 
                               
load_dotenv()  

# OpenWeather API                                                          
API_KEY = os.getenv("OPENWEATHER_API_KEY")                                 
CITY = "Seoul"                                                             
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"  
# README file route
README_PATH = "/home/user02/weather/README.md"

def get_weather():
    """Get weather data using OpenWeatherAPI"""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        return f"current weather: {weather}, current temperature: {temp}°CC, current humidity: {humidity}%"
    else:
        return "fail to get weather information."

def update_readme():
    """Update README.md"""
    weather_info = get_weather()
    readme_content = f"""
# Weather API Status

This repository updates current seoul weather information automatically, using OpenWeatherAPI.

current seoul weather
> {weather_info}

update-time: {now} (UTC)

---
It is managed by auto update-bot.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()