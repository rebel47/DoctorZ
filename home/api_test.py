import json
import requests
from requests import sessions

resp =  requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=110025&date=08-06-2021')
data = resp.json()
print(data.values('center_id'))


# for i in data:
#     x = data[i]['center_id']
#     print(x)
