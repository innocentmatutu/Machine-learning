import requests

city = "Nairobi"
country_code = 'Kenya'
API = '99fced1417e6ce31e3322b04f40e5492'

geo_url = f'https://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={API}'
geo_response = requests.get(geo_url)
geo_data = geo_response.json()


lat = geo_data[0]['lat']
lon = geo_data[0]['lon']

weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric'
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

current_temp = weather_data['main']['temp']
calculated_temp =round(current_temp * 9/5 + 32,1)
print(f'Temprature in {city} is: {calculated_temp} degrees')