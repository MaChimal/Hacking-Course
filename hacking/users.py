import json
import urllib
import urllib.request

url = urllib.request.urlopen("https://curso--python-0-pruebas1.000webhostapp.com/")
for u in json.loads(url.read()):
    user = u['slug']
print(user)
