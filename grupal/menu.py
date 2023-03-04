import os
import json
from datetime import datetime, date
from clases1 import Cliente
import re


def mostrar_menu():
    print('--- Menú ---')
    print('1. Crear cliente')
    print('2. Mostrar Clientes')
    print('3. Agregar Saldo')
    print('4. Mostrar Saldo')
    print('0. Salir')


def ejecutar_opcion(opcion, clase_cliente):
    if opcion == '1':
        # Solicitar los datos para crear un nuevo cliente
        nombre = input('Ingrese el nombre del cliente: ')
        apellido = input('Ingrese el apellido del cliente: ')
        correo = input('Ingrese el correo electrónico del cliente: ')
        while True:
            fecha_registro = input("Fecha de registro del cliente (formato dd/mm/aaaa): ")
            if re.match(r'^\d{2}/\d{2}/\d{4}$', fecha_registro):
                fecha_registro = datetime.strptime(fecha_registro, '%d/%m/%Y')
                break
            else:
                print("Formato de fecha no válido. Intente de nuevo.")
        saldo = int(input('Ingrese el saldo del cliente: '))

        # Llamar al método crear_cliente con los datos ingresados
        clase_cliente.crear_cliente(id, nombre, apellido, correo, fecha_registro, saldo)
    elif opcion == "2":
        # Mostrar los clientes
        Cliente.mostrar_clientes()

    elif opcion == "3":
        # Mostrar los clientes
        Cliente.mostrar_clientes()
        # Agregar saldo
       

    elif opcion == "4":
            # Mostrar saldo
        cliente = Cliente()
        cliente.get_saldo()
        clientes = Cliente.get_saldo()
        if clientes:
            print(f"{'ID':<4} {'Nombre':<10} {'Apellido':<10} {'Saldo':<10}")
        for cliente in clientes:
            print(f"{cliente['id']:<4} {cliente['nombre']:<10} {cliente['apellido']:<10} {cliente['saldo']:<10}")
        else:
            print('No hay clientes registrados.')
        

    elif opcion == "0":
        print("Gracias por utilizar nuestro sistema. ¡Hasta luego!")
        return
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")


while True:
    mostrar_menu()
    opcion = input('Seleccione una opción: ')
    ejecutar_opcion(opcion, Cliente)