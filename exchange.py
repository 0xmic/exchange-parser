import json
import requests

def getJson (url):
    try:
        response = requests.get(url)
        file_data = json.loads(response.text)
    except e:
        return ''
    return (file_data)