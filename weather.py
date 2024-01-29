import os
import urllib.request
import json

# "weather":[{"id":804,"main":"Clouds","description":"пасмурно","icon":"04n"}] только "description"?
#
#
#
#

def getWeather(city, apiKey):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appId={apiKey}&units=metric&lang=ru"
    with urllib.request.urlopen(url) as result:
        weacherJson = json.loads(result.read())
        #print(weacherJson)
        return {
            "city": city,
            "Описание": weacherJson["weather"][0]["description"],
            "feels_like": weacherJson["main"]["feels_like"],
            "wind_speed": weacherJson["wind"]["speed"],
        }

if __name__ == "__main__":
    city = "Minsk"
    apiKey = os.getenv("W_API_KEY")
    weatherData = getWeather(city, apiKey)
    print(weatherData)
# https://api.openweathermap.org/data/2.5/weather?q=Minsk&appId=bd5e378503939ddaee76f12ad7a97608&units=metric&lang=ru