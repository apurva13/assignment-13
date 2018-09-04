#Q.1-Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.

import requests
response=requests.get("https://api.forismatic.com/api/1.0/")
print(response.status_code)
print(response.content)
import json
data=response.json()
print(type(data))
print(data)
