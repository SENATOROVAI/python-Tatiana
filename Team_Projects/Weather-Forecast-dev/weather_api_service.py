''' Implement the core functionality of the weather application.
Integrate the functionalities from coordinates.py, weather_api_service.py, and weather_formatter.py'''

""" API-ключ для сервиса OpenWeather лучше сохранить в переменной окружения и не
хранить в исходном коде проекта (тогда значение константы будет получаться как-то так: os.getenv("OPENWEATHER_API_KEY") , но сейчас мы этого делать не будем для
упрощения запуска приложения."""

# Логику парсинга каждой нужной нам единицы информации
# выносим в отдельные небольшие функции — отдельно парсинг температуры,
# отдельно парсинг типа погоды и времени восхода и заката

# Ипорт библиотек
from datetime import datetime # модуль позволяет управлять датами и временем, представляя их в таком виде, в котором пользователи смогут их понимать
from dataclasses import dataclass # классы данных (Data classes). Они призваны автоматизировать генерацию кода классов, которые используются для хранения данных
from enum import Enum # содержит в себе тип для перечисления значений с возможностью итерирования и сравнения https://habr.com/ru/companies/timeweb/articles/564826/
import json
from json.decoder import JSONDecodeError # проверка json на ошибку JSONDecodeError
import ssl # модуль для обеспечения безопасного соединения между клиентом и сервером
from typing import Literal, TypeAlias
import urllib.request
from urllib.error import URLError
from coordinates import Coordinates
import config
from exceptions import ApiServiceError

Celsius: TypeAlias = int
class WeatherType(str, Enum):
THUNDERSTORM = "Гроза"
DRIZZLE = "Изморось"
RAIN = "Дождь"
SNOW = "Снег"
CLEAR = "Ясно"
FOG = "Туман"
CLOUDS = "Облачно"
@dataclass(slots=True, frozen=True)
class Weather:
temperature: Celsius
weather_type: WeatherType
sunrise: datetime
sunset: datetime
city: str
def get_weather(coordinates: Coordinates) -> Weather:
"""Requests weather in OpenWeather API and returns it"""
openweather_response = _get_openweather_response(
longitude=coordinates.longitude, latitude=coordinates.latitude)
weather = _parse_openweather_response(openweather_response)
return weather
def _get_openweather_response(latitude: float, longitude: float) -> str:
ssl._create_default_https_context = ssl._create_unverified_contexturl = config.OPENWEATHER_URL.format(
latitude=latitude, longitude=longitude)
try:
return urllib.request.urlopen(url).read()
except URLError:
raise ApiServiceError
def _parse_openweather_response(openweather_response: str) -> Weather:
try:
openweather_dict = json.loads(openweather_response)
except JSONDecodeError:
raise ApiServiceError
return Weather(
temperature=_parse_temperature(openweather_dict),
weather_type=_parse_weather_type(openweather_dict),
sunrise=_parse_sun_time(openweather_dict, "sunrise"),
sunset=_parse_sun_time(openweather_dict, "sunset"),
city=_parse_city(openweather_dict)
)
def _parse_temperature(openweather_dict: dict) -> Celsius:
return round(openweather_dict["main"]["temp"])
def _parse_weather_type(openweather_dict: dict) -> WeatherType:
try:
weather_type_id = str(openweather_dict["weather"][0]["id"])
except (IndexError, KeyError):
raise ApiServiceError
weather_types = {
"1": WeatherType.THUNDERSTORM,
"3": WeatherType.DRIZZLE,
"5": WeatherType.RAIN,
"6": WeatherType.SNOW,
"7": WeatherType.FOG,
"800": WeatherType.CLEAR,
"80": WeatherType.CLOUDS
}
for _id, _weather_type in weather_types.items():
if weather_type_id.startswith(_id):
return _weather_type
raise ApiServiceError
def _parse_sun_time(
openweather_dict: dict,
time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
return datetime.fromtimestamp(openweather_dict["sys"][time])
def _parse_city(openweather_dict: dict) -> str:return openweather_dict["name"]
if __name__ == "__main__":
print(get_weather(Coordinates(latitude=55.7, longitude=37.6)))