from django.shortcuts import render,render
import requests
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=314b03e761de15a2e6fc1e7822396b7e'#api link with api key
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()#taking the information from api inform of json
    

    city_weather = {

        'city' : city,
        'temperature' : r['main']['temp'],
        'descripiton' : r['weather'][0]['description'],
        'icon' :  r['weather'][0]['icon']

    }
    context = {'city_weather' : city_weather}

    return render(request,'weather.html',context)
