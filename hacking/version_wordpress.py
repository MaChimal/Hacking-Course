#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

url = "https://curso--python-0-pruebas1.000webhostapp.com/"
cabecera = {'User-Agent':'Firefox'}
peticion = requests.get(url=url, headers=cabecera)
soup = BeautifulSoup(peticion.text, 'html5lib')
for v in soup.find_all('meta'):
    if v.get('name') == 'generator':
        version = v.get('content')
print(version)