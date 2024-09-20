from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request

def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        api_key = 'c4bd8136942f0a24e947752f9e5c7cbf'  # Your API key
        # Make a request to the OpenWeatherMap API
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read() 
        list_of_data = json.loads(source) 
        # Convert temperature from Kelvin to Celsius
        temperature_celsius = round(float(list_of_data['main']['temp']) - 273.15, 2)

        # Prepare data to be sent to the template
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']), 
            "temp": str(temperature_celsius) + '°C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
                } 
    else: 
        data = {} 
    return render(request, "index.html", data)
