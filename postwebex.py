import requests

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'OGEzOTliYTEtOTUyMi00Y2IxLTliZTAtZjI2ZjU4YjRiOWM4NDg3YWM5MWMtNWU1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 'toPersonEmail': 'njansens@cisco.com', 'text': 'Dag Niels' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )
