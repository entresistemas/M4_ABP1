import os
import json

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def update(data, file):
    with open(file, 'w') as archivo_json:
        # Usamos json.dump() para escribir la lista de diccionarios en el archivo
        json.dump(data, archivo_json)

    # Cerramos el archivo
    archivo_json.close()

def open_file(file):
    with open(file, "r") as archivo:
        return json.load(archivo)