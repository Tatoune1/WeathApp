import requests


def get_openweather_data(data_type, city):
    """take as a parameter the wanted data and the targeted city as strings. 
    7 options of data : -current_temperature
                           -current_humidity
                           -current_weather_description
                           -current_wind_speed
                           -feels_like
                           -minimal_temperature
                           -maximum_temperature"""
    assert type(data_type) == str, 'the data parameter must be given as a string'
    assert type(city) == str, 'the city parameter must be given as a string'


    API_KEY = "API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr" #make the API request

    try:
        response = requests.get(url)
        response.raise_for_status()

        weather_data = response.json()  #store the data in a dictionary from a Json file send by the website

    except :
        assert False, "There is a problem with the API"
        return False

    if weather_data["cod"] != "404":                                        #stores all retrieived data in a dictionary, before returning the wanted data
        current_temperature = weather_data["main"]["temp"]
        current_humidity = weather_data["main"]["humidity"]
        weather_description =  weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        feels_like = weather_data["main"]["feels_like"]
        temperature_minimal = weather_data["main"]["temp_min"]
        temperature_maximum = weather_data["main"]["temp_max"]
        sunset_time = weather_data["sys"]["sunset"]
        sunrise_time = weather_data["sys"]["sunrise"]

        data = {"current_temperature" : current_temperature,
             "current_humidity" : current_humidity,
             "current_weather_description" : weather_description,
             "current_wind_speed" : wind_speed,
             "feels_like": feels_like,
             "minimal_temperature": temperature_minimal,
             "maximum_temperature": temperature_maximum,
             "sunset_time": sunset_time,
             "sunrise_time": sunrise_time}
        return data[data_type]

print(get_openweather_data("current_temperature", "Eaubonne"))


