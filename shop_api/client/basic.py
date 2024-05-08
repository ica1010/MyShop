import requests
endpoint = 'http://httpbin.org/anything'


response = requests.get(endpoint)

print(response.json())
print(response.text)
# HTTP REQUEST --> HTML
# REST API HTTP ---> JSON (JAVASCRIPT OBJECT NOTATION)