import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1cc737a116cec0beaef58e35e9e4286a'
    
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cites = City.objects.all()
    city_weather = []

    for city in cites :
        r = requests.get(url.format(city)).json()
        print(r)
        weather = {
            'city': city,
            'description': r['weather'][0]['description'],
            'temperature': r['main']['temp'],
            'icon': r['weather'][0]['icon'],
        }
        city_weather.append(weather)
        
    context = {
        'city_weather': city_weather,
        'form': form,
    }
    return render(request, "MainApp/index.html", context)
