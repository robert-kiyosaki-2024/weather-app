import requests


def get_weather(api_key, city, lang):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang={lang}"

  response = requests.get(url)
  data = response.json()

  if data["cod"] == 200:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
  else:
    print(f"Failed to fetch weather data. Error code: {data['cod']}")


if __name__ == "__main__":
  api_key = "your_api_key_here"
  city = "Stuttgart"
  lang = "de"
  get_weather(api_key, city, lang)

