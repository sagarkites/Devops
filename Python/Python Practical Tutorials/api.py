import requests
from pprint import pprint

city = input('Enter the City Name --> ')

url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']

Air = data['wind']['speed']

 
print('Temperature : ', temp)

print('Air : {}'.format(Air))
