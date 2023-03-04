import json
import os
from datetime import date, datetime

# Inicio Clase Cliente
class Cliente:
    def __init__(self, id: int, nombre: str, apellido: str, correo: str, fecha_registro: date, saldo: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo #Elemento privado

    # Metodo para Crear nuevo Cliente
    @staticmethod
    def crear_cliente():
        try:
            # Verificar si el archivo de clientes existe, y crearlo si no
            if not os.path.isfile("clientes.json"):
                with open("clientes.json", "w") as archivo:
                    json.dump([], archivo)

            # Leer los clientes del archivo
            with open("clientes.json", "r") as archivo:
                clientes = json.load(archivo)

            nombre = input('Ingrese el nombre del cliente: ')
            apellido = input('Ingrese el apellido del cliente: ')
            correo = input('Ingrese el correo del cliente: ')
            fecha_registro = datetime.now().date()
            saldo = int(input('Ingrese el saldo del cliente: '))

            # Crear un diccionario con los datos del usuario
            nuevo_cliente = {
                "id": len(clientes) + 1,
                "nombre": nombre,
                "apellido": apellido,
                "correo": correo,
                "fecha_registro": fecha_registro.strftime('%Y-%m-%d'),
                "saldo": saldo,
            }

            # Agregar el cliente al diccionario
            clientes.append(nuevo_cliente)

            # Guardar los clientes en el archivo externo
            with open("clientes.json", "w") as archivo:
                json.dump(clientes, archivo)

            # Mostrar un mensaje de confirmación
            print("Cliente creado con éxito")

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

    # Funcion Mostrar Clientes
    @staticmethod
    def mostrar_clientes():
        with open('clientes.json') as f:
            clientes = json.load(f)
        
        if not clientes:
            print('No hay clientes registrados.')
        else:
            for cliente in clientes:
                print(cliente)
                """print('ID:', cliente['id'])
                print('Nombre completo:', cliente['nombre'], cliente['apellido'])
                print('Correo electrónico:', cliente['correo'])
                print('Fecha de registro:', cliente['fecha_registro'])
                print('Saldo:', cliente['saldo'])
                print('---')"""

  # Metodo para agregar saldo a un cliente
    def agregar_saldo():
        try:
            
            with open('clientes.json') as f:
                clientes = json.load(f)
            
            id_cliente = input('Ingrese el ID del cliente al que desea agregar saldo: ')
            cantidad = int(input('Ingrese la cantidad de saldo que desea agregar: '))

            cliente_encontrado = False
            for cliente in clientes:
                if cliente['id'] == int(id_cliente):
                    cliente['saldo'] += cantidad
                    cliente_encontrado = True
                    print(f'Se han agregado {cantidad} unidades de saldo. Saldo actual del cliente: {cliente["saldo"]}')

            if not cliente_encontrado:
                print(f"No se encontró el cliente con ID {id_cliente}")

            with open('clientes.json', 'w') as f:
                json.dump(clientes, f)

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

    # Metodo para mostrar el saldo de un cliente
    def mostrar_saldo():
        with open('clientes.json') as f:
            clientes = json.load(f)
        
        if not clientes:
            print('No hay clientes registrados.')

        else:
            for cliente in clientes:
                print('ID:', cliente['id'], 'Nombre:', cliente['nombre'], cliente['apellido'],'Saldo:', cliente['saldo'])
                

        

# Fin Clase Cliente

while True:
    print('--- Menú ---')
    print('1. Crear cliente')
    print('2. Mostrar clientes')
    print('3. Agregar saldo a un cliente')
    print('4. Mostrar saldo de un cliente')
    print('0. Salir')
    
    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        Cliente.crear_cliente()
    
    elif opcion == '2':
        Cliente.mostrar_clientes()
    
    elif opcion == '3':
        Cliente.mostrar_saldo()
        Cliente.agregar_saldo()
    
    elif opcion == '4':
        Cliente.mostrar_saldo()
        

    elif opcion == '0':
        break

    else:
        print('Opción inválida. Por favor, intente nuevamente.')