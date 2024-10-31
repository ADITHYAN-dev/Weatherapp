from django.shortcuts import render
import requests

# Your OpenWeatherMap API key
API_KEY = '7221a575edb1e8ce08d26d15622c77b7'

def index(request):
    # Default city or city provided by user
    city = request.GET.get('city', 'New York')

    # OpenWeatherMap API endpoint with the API_KEY variable
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    # Make the request to OpenWeatherMap API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        weather_data = {'error': 'City not found'}

    return render(request, 'weather/index.html', {'weather_data': weather_data})
