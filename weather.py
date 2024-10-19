import requests
import json

city = input("Enter the city: \n")

url = f"https://api.weatherapi.com/v1/current.json?key=9cf100fbbedf4ce4a93161534241610&q={city}"

r = requests.get(url)
# print(r.text)

wdics = json.loads(r.text)
print(wdics["current"] ["temp_c"])