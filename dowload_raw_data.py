import requests

params = {
    'from_date' : '2021-04-13',
    'to_date' : '2021-04-13'
}

api_secret = "You can find secret in project settings"

url = 'https://data.mixpanel.com/api/2.0/export'
r = requests.get(url, auth = (f'{api_secret}:', ''), params=params)
with open('output.txt', 'w') as f:
    f.write(r.text)