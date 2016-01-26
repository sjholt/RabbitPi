from pprint import pprint
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Farnborough,uk&appid=d72e04a6c85cc1b7864d3c0f10bb63b0')
pprint(r.json())
{u'base': u'cmc stations',
 u'clouds': {u'all': 68},
 u'cod': 200,
 u'coord': {u'lat': 51.50853, u'lon': -0.12574},
 u'dt': 1383907026,
 u'id': 2643743,
 u'main': {u'grnd_level': 1007.77,
           u'humidity': 97,
           u'pressure': 1007.77,
           u'sea_level': 1017.97,
           u'temp': 282.241,
           u'temp_max': 282.241,
           u'temp_min': 282.241},
 u'name': u'London',
 u'sys': {u'country': u'GB', u'sunrise': 1383894458, u'sunset': 1383927657},
 u'weather': [{u'description': u'broken clouds',
               u'icon': u'04d',
               u'id': 803,
               u'main': u'Clouds'}],
 u'wind': {u'deg': 158.5, u'speed': 2.36}}
