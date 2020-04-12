import requests 
import argparse
from os import path


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="Archivo a subir")
parser = parser.parse_args()


if parser.file:
    if path.exists(parser.file):
        archivo = open(parser.file, 'rb')
        headers = {'User-Agent':'Firefox'}
        peticion = requests.post(url = "https://curso--python-0-prueba-pentest.000webhostapp.com/", files={'uploaded_file':archivo}, headers=headers)
        if parser.file in peticion.text:
            print(peticion.text)
            print("Archivo subido con éxito")
        else:
            print("Falló la subida")
    else:
        print(":(")
else:
    print("Necesito un archivo")

