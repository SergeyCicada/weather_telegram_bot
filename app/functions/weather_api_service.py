import requests
from typing import NamedTuple
from config import OPENWEATHER_KEY

Celsius = float  # type - Literal


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str


def get_weather(city_name: str) -> Weather:
    """Requests weather in OpenWeather API and return weather"""
    w = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_KEY}&'
                     f'units=metric', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                                                            "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"},
                     timeout=5)

    weather = w.json()
    return Weather(
        temperature=weather['main']['temp'],
        weather_type=weather['weather'][0]['main']
        )


