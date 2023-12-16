import requests
headers = {
    'Authorization': 'Bearer 3019|jfwx2CAuSGI3twjSYyvxFATfXuBl4ZUT2z2Vos8c'
}

payload = {
    'keyword': 'chair',
    'countryCode': 'US',
    'languageCode': 'en'
    }
url = f"https://zylalabs.com/api/2226/ikea+api/2075/search+by+keyword?keyword={payload['keyword']}&countryCode=US&languageCode=en"
    
print(response = requests.request("GET", url, headers=headers, data=payload))
