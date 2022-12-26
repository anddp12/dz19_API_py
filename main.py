import json, requests
from keys import API_KEY

URL ='https://api.openweathermap.org/data/2.5/weather'
QUERY_CITY = "?q={0}&appid={1}"

city = input('City: ')
request = URL + QUERY_CITY.format(city, API_KEY)
response = requests.get(request)

json_w = json.loads(response.text)
print(json_w)
temp = json_w['main']['temp'] - 273.15
temp1 = json_w['main']['feels_like'] - 273.15
humidity = json_w['main']['humidity']
pressure = json_w['main']['pressure']

print(f"🌡 Температура воздуха в городе {city} составляет : {round(temp,1)} ℃ \n🌡 Ощущается как {round(temp1,1)} ℃")
print(f"💧 Влажность : {humidity} %")
print(f"☁ Давление : {pressure} гПа")
