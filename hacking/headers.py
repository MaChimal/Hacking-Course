import requests
import argparse



parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument('-t', '--target', help="Objetivo")
parser = parser.parse_args()






# parser.target tiene el objetivo
#headers contiene la respuesta del objetivo


if parser.target:
    try:
        url = requests.get(url=parser.target)
        cabeceras = dict(url.headers)
        for x in cabeceras:
            print(x + " : " + cabeceras[x])
    except:
        print("Error al conectar")
#    print(parser.target)
else:
    print("No hay objetivo")