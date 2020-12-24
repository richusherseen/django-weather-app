from django.shortcuts import render,render
import requests
from weather.models import City
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=314b03e761de15a2e6fc1e7822396b7e'#api link with api key
    city = 'Las Vegas'
    
    cities = City.objects.all()
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()#taking the information from api inform of json
        
        
        city_weather = {

            'city' : city.name,
            'temperature' : r['main']['temp'],
            'descripiton' : r['weather'][0]['description'],
            'icon' :  r['weather'][0]['icon']

        }
        weather_data.append(city_weather)
       
    context = {'weather_data' : weather_data}

    return render(request,'weather.html',context)
