import requests
import base64

#Get a token from DNA Center
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
payload = None
authentication = "devnetuser:Cisco123!"
encodedBytes = base64.b64encode(authentication.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + encodedStr,
    "Accept": "application/json"
}
response = requests.request('POST', url, headers=headers, data = payload)

#Get Site info from DNA Center

url = "https:///sandboxdnac.cisco.com/intent/api/v1/network-device"
payload = None
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": + response.text.encode('utf8'),
    "Accept": "application/json"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))


