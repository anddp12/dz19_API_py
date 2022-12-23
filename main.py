import json, requests
from keys import API_KEY

URL ='https://api.openweathermap.org/data/2.5/weather'
QUERY_CITY = "?q={0}&appid={1}"

city = input('City: ')
request = URL + QUERY_CITY.format(city, API_KEY)
response = requests.get(request)

json_w = json.loads(response.text)
print(json_w)
