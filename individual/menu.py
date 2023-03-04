import os
import json
from clases1 import Usuario
import clients, store

with open("usuarios.json", "r") as archivo:
    usuarios = json.load(archivo)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print('*******Ingresa Tus Credenciales de Usuario*******')
    nombre = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")
    perfil = Usuario.login(nombre, clave)

    if perfil == "administrador":
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
            Usuario.mostrar_usuarios()
            input("Presione Enter para continuar ...")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

    elif perfil == "vendedor":
        print("1. Ver clientes")
        print("2. Agregar cliente")
        print("3. Eliminar cliente")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            clients.client_view()
            input("Presione Enter para continuar ...")
        elif opcion == "2":
            clients.add_client()
        elif opcion == "3":
            clients.eliminar_cliente()
            input("Presione Enter para continuar ...")
                 
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

    elif perfil == "bodeguero":
        print("1. Ver inventario")
        print("2. Agregar stock al inventario")
        print("3. Eliminar stock del inventario")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            store.stock_view()
        elif opcion == "2":
            store.action_add()
        elif opcion == "3":
            store.action_subtract()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

    else:
        print("Credenciales incorrectas")
        break