import requests
import os
from pprint import pprint
from twilio.rest import Client, TwilioHttpClient  # didnt create a usr in this page

key = "80e877059407012cbef59f8ac82bcf1c"
city_name = 'Helsinki'
apilist = '?'

url = apilist

# from twilio page dashboard:
account_sid = "your auth key from twilio page"
auth_token = 'dgasjhdgbasbgdyndsagdasd'
client = Client(account_sid, auth_token)

vallila_position = 60.1944, 24.9570

endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'

endpoint_coor = 'api.openweathermap.org/data/2.5/weather?'
weather_params = {
    'lat': vallila_position[0],
    'long': vallila_position[1],
    'appid': key
    # 'exclude': "current, minutely, daily"
}

response = requests.get(url=endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'http': os.environ['http_proxy']}

msg = client.messages \
    .create(
    body_="join earth migtiest heroes. like kevin bacon",
    from_="+15017122661",
    to='+1555867310'
    )
print(msg.status)