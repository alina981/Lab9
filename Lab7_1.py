import requests
import json

key = "662fbdf4d369847a1f4cacba09e5d6b0"
city_name = "Tambov"
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
result = json.loads(response.text)
print(f"Сейчас в {cgit ity_name} \nтемпература: {result['main']['temp'] - 273.15} \nвлажность: {result['main']['humidity']} \nдавление: {result['main']['pressure']}")