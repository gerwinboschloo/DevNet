import requests
import base64

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload = None
authentication = "devnetuser:Cisco123!"
# Standard Base64 Encoding
encodedBytes = base64.b64encode(authentication.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + encodedStr,
    "Accept": "application/json"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))
