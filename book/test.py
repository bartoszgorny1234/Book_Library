import requests
import json

parameters = {
    "q": 'Hobbit'
}
# https://www.googleapis.com/books/v1/volumes?q=Hobbit
response = requests.get("https://www.googleapis.com/books/v1/volumes", params=parameters).json()['items']
print(response)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# print(json.dumps(response, sort_keys=True, indent=4))
for element in response:
    element1 = element['volumeInfo']
    jprint(element1['title'])
    jprint(element1['authors'])