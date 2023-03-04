import json
import os
from datetime import date, datetime




#Somecoment


# ****** Inicio Clase Cliente ******
class Cliente:
    def __init__(self, id: int, nombre: str, apellido: str, correo: str, fecha_registro: date, saldo: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo #Elemento privado

        

    def get_saldo(self):
        #return self.__saldo #elemento publico con el que puede usuario interactuar con saldo
        with open('clientes.json') as f:
            clientes = json.load(f)
        
        if not clientes:
            print('No hay clientes registrados.')
        else:
            for cliente in clientes:
                 print(f"{cliente['id']} {cliente['nombre']} {cliente['apellido']} {cliente['saldo']}")
                

    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo #elemento publico con el que puede usuario interactuar con saldo


    #Funcion crear cliente
    @staticmethod
    def crear_cliente(id, nombre, apellido, correo, fecha_registro, saldo):
        # Validar si el archivo existe y no está vacío

            # Verificar si el archivo de clientes existe, y crearlo si no
            if not os.path.isfile("clientes.json"):
                with open("clientes.json", "w") as archivo:
                    json.dump([], archivo)

            nombre = input('Ingrese el nombre del cliente: ')
            apellido = input('Ingrese el apellido del cliente: ')
            correo = input('Ingrese el correo del cliente: ')
            fecha_registro = datetime.now().date()
            saldo = int(input('Ingrese el saldo del cliente: '))

            # Crear un diccionario con los datos del usuario
            nuevo_cliente = {
            "id": len(archivo) + 1,
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "fecha_registro": fecha_registro,
            "saldo": saldo,
            }
        
            # Agregar el cliente al diccionario
            archivo.append(nuevo_cliente)

            # Guardar los clientes en el archivo externo
            with open("clientes.json", "w") as archivo:
                json.dump(clientes, archivo)

            # Mostrar un mensaje de confirmación
            print("Cliente creado con éxito")
        
        
        

    # Funcion Mostrar Clientes
    @staticmethod
    def mostrar_clientes():
        with open('clientes.json') as f:
            clientes = json.load(f)
        
        if not clientes:
            print('No hay clientes registrados.')
        else:
            for cliente in clientes:
                print('ID:', cliente['id'])
                print('Nombre completo:', cliente['nombre'], cliente['apellido'])
                print('Correo electrónico:', cliente['correo'])
                print('Fecha de registro:', cliente['fecha_registro'])
                print('Saldo:', cliente['saldo'])
                print('---')


# ****** Fin Clase Cliente ******



# ****** Inicio Clase Producto ******
class Producto:
    def __init__(self, sku: int, nombre: str, categoria: str, proveedor: str, stock: int, valor_neto: int, impuesto: float = 1.19):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto

    def get_precio_neto(self):
        return self.valor_neto
    
    def get_precio_bruto(self):
        return self.valor_neto * self.__impuesto

    def set_impuesto(self, nuevo_impuesto: float):
        self.__impuesto = nuevo_impuesto

# ****** Fin Clase Producto ******

# ****** Inicio Clase Vendedor ******
class Vendedor:
    def __init__ (self, run: str, nombre: str, apellido: str, seccion: str, comision: int = 0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision 

    def get_comision(self):
        return self.__comision
    
    def set_comision(self, nueva_comision: int):
        self.__comision = nueva_comision


# ****** Fin Clase Vendedor ******

# ***** Menú ******
while True:
    print('--- Menú ---')
    print('1. Crear cliente')
    print('2. Mostrar clientes')
    print('3. Agregar saldo')
    print('4. Mostrar saldo')
    print('0. Salir')

    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        
        Cliente.crear_cliente()

    elif opcion == '2':
        Cliente.mostrar_clientes()

    elif opcion == '3':
        id = int(input('Ingrese el ID del cliente: '))
        nuevo_saldo = int(input('Ingrese el nuevo saldo del cliente: '))

        with open('clientes.json') as f:
            clientes = json.load(f)

        for cliente in clientes:
            if cliente['id'] == id:
                cliente['saldo'] = nuevo_saldo

        with open('clientes.json', 'w') as archivo:
            json.dump(clientes, archivo)

        print('Saldo actualizado correctamente.')

    elif opcion == '4':
        Cliente.get_saldo()

    elif opcion == '0':
        break

    else:
        print('Opción inválida. Por favor, intente nuevamente.')


