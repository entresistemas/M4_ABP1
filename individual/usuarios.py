import json
import os
from clases1 import Usuario

# Verificar si el archivo de usuarios existe, y crearlo si no
if not os.path.isfile("usuarios.json"):
    with open("usuarios.json", "w") as archivo:
        json.dump([], archivo)

# Menú principal
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("1. Crear nuevo usuario")
    print("2. Modificar usuario")
    print("3. Eliminar usuario")
    print("4. Mostrar Usuarios")
    print("0. Salir")
    opcion = input("Selecciona una opción: ")
    

    if opcion == "1":
        Usuario.crear_usuario()
    elif opcion == "2":
        Usuario.modificar_usuario()
    elif opcion == "3":
        Usuario.eliminar_usuario()
    elif opcion == "4":
        Usuario.muestra_usuarios_registrados()
    elif opcion == "0":
        break
    else:
        print("Opción inválida")