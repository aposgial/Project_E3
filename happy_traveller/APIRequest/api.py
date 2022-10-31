import requests
import json

url = "https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=0c42b0411f9852d52d31cd1445ad3b09&tags=Paris+city&has_geo=&format=json"
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)

else:
    print(f"Error: {response.status_code}")
