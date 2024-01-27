import requests
import json

API_KEY = '2f44ab8d94825710392977b37c24d3ac'

def weather_request(city_name, api_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric')
    
    return json.loads(response.text)

def weather_output():
    city_name = 'Saint Petersburg'
    weather_data = weather_request(city_name, API_KEY)

    print(f'City: {city_name}')
    print(f'Temp: {weather_data["main"]["temp"]}°C')
    print(f'Humidity: {weather_data["main"]["humidity"]}%')
    print(f'Pressure: {weather_data["main"]["pressure"]} Pa')

def covid_request():
    response = requests.get('https://api.covidtracking.com/v1/us/current.json')
    return json.loads(response.text)

def covid_output():
    covid_data = covid_request()

    print('US total covid data:')
    print(f'Positive tests: {covid_data[0]["positive"]}')
    print(f'Negative tests: {covid_data[0]["negative"]}')
    print(f'Pending tests: {covid_data[0]["pending"]}')
    print(f'Hospitalized currently: {covid_data[0]["hospitalizedCurrently"]}')

if __name__ == '__main__':
    weather_output()
    print('\n')
    covid_output()
