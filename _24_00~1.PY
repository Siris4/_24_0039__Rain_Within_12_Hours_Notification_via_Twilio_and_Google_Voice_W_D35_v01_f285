import requests
import os
from twilio.rest import Client
# import smtplib  # uncomment if you are using the email functionality:

# environment variables setup:
API_KEY = os.environ.get('API_KEY', 'API key not found')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', 'Twilio Account SID not found')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', 'Twilio Auth Token not found')

# print environment variables to verify:
print(f"The API_KEY is: {API_KEY}")
print(f"The TWILIO_ACCOUNT_SID is: {TWILIO_ACCOUNT_SID}")
print(f"The TWILIO_AUTH_TOKEN is: {TWILIO_AUTH_TOKEN}")

# twilio client setup:
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

lat = 25.672939
lon = -100.309731
API_Weather_URL_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"  # or your desired endpoint:

# weather api parameters:
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=API_Weather_URL_Endpoint, params=weather_params)
response.raise_for_status()  # raise an exception for http errors:
data = response.json()
print(f"The JSON data is: {data}")

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
    message = client.messages.create(
        body="Greetings! This is a 12-Hour heads up, that it will rain in Monterrey, Mexico!☂️ Wear a poncho!!",
        from_="+18888462616",  # replace with your twilio number:
        to='+17654189611',     # replace with your personal number:
    )
    print(f"Message Status: {message.status}")


    #IF SMS WORKING, DISABLE BELOW HERE:


    #
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email1, password=my_email_app_password)
    #     connection.sendmail(
    #         from_addr=my_email1,
    #         to_addrs=email_being_sent_to2,
    #         msg=f"{subject}{body}"
    #     )

'''
None
{'coord': {'lon': -100.3097, 'lat': 25.6729}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 294.52, 'feels_like': 294.12, 'temp_min': 294.19, 'temp_max': 299.78, 'pressure': 1010, 'humidity': 54, 'sea_level': 1010, 'grnd_level': 950}, 'visibility': 10000, 'wind': {'speed': 2.27, 'deg': 113, 'gust': 3.78}, 'clouds': {'all': 100}, 'dt': 1706052079, 'sys': {'type': 1, 'id': 7108, 'country': 'MX', 'sunrise': 1706016484, 'sunset': 1706055453}, 'timezone': -21600, 'id': 3995465, 'name': 'Monterrey', 'cod': 200}
The status code is: 200
The response is: None
{'Clouds'}
{'overcast clouds'}
'''

#200 code! PERFECT!!!

# JSON data for Luftin, Texas:
'''
The JSON data is: {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1706140800, 'main': {'temp': 289.19, 'feels_like': 289.41, 'temp_min': 287.87, 'temp_max': 289.19, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1006, 'humidity': 98, 'temp_kf': 1.32}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.74, 'deg': 99, 'gust': 5.24}, 'visibility': 10000, 'pop': 1, 'rain': {'3h': 5.7}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-25 00:00:00'}, {'dt': 1706151600, 'main': {'temp': 288.81, 'feels_like': 289.02, 'temp_min': 288.06, 'temp_max': 288.81, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1006, 'humidity': 99, 'temp_kf': 0.75}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.82, 'deg': 115, 'gust': 8.43}, 'visibility': 10000, 'pop': 1, 'rain': {'3h': 3.36}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-25 03:00:00'}, {'dt': 1706162400, 'main': {'temp': 288.4, 'feels_like': 288.57, 'temp_min': 288, 'temp_max': 288.4, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1006, 'humidity': 99, 'temp_kf': 0.4}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.36, 'deg': 313, 'gust': 2.98}, 'visibility': 1158, 'pop': 1, 'rain': {'3h': 2.17}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-25 06:00:00'}, {'dt': 1706173200, 'main': {'temp': 287.61, 'feels_like': 287.7, 'temp_min': 287.61, 'temp_max': 287.61, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1005, 'humidity': 99, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.65, 'deg': 334, 'gust': 5.75}, 'visibility': 437, 'pop': 0.83, 'rain': {'3h': 2.58}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-25 09:00:00'}], 'city': {'id': 4708308, 'name': 'Lufkin', 'coord': {'lat': 31.3329, 'lon': -94.7279}, 'country': 'US', 'population': 35067, 'timezone': -21600, 'sunrise': 1706102143, 'sunset': 1706139947}}
The status code (response code - for calling this API) is: 200
The response is: None
The weather condition0: 501
The weather condition1: 501
The weather condition2: 500
The weather condition3: 500

Bring an umbrella!

Process finished with exit code 0


-------------------------------------

The weather condition0: 501
The weather condition1: 501
The weather condition2: 803
The weather condition3: 803

Bring an umbrella!
Message Status: queued

Process finished with exit code 0


'''
