import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Imperial&appid=1cc737a116cec0beaef58e35e9e4286a'
    city = 'Lagos '
    city2 = 'London'
    city3 = 'Texas '

    if request.method == "POST":
        new_city = CityForm(request.POST)
        rn = requests.get(url.format(new_city)).json()

        city_weather_new = {
            'city': new_city,
            'temperature': rn['main']['temp'],
            'description': rn['weather'][0]['description'],
            'icon': rn['weather'][0]['icon'],
        }
        return city_weather_new
    
    r = requests.get(url.format(city)).json()
    r2 = requests.get(url.format(city2)).json()
    r3 = requests.get(url.format(city2)).json()
    
    print(r)

    city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

    city_weather2 = {
            'city': city2,
            'temperature': r2['main']['temp'],
            'description': r2['weather'][0]['description'],
            'icon': r2['weather'][0]['icon'],
        }
    
    city_weather3 = {
            'city': city3,
            'temperature': r3['main']['temp'],
            'description': r3['weather'][0]['description'],
            'icon': r3['weather'][0]['icon'],
        }

    

    context = {
        'city_weather': city_weather,
        'city_weather2': city_weather2,
        'city_weather3': city_weather3,
        
    }
    return render(request, "MainApp/index.html", context)


"""

cities = City.objects.all()
    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
    
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

    '''print(city_weather)'''

"""
