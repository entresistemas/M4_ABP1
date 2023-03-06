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
    # --------------------
   
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

     # *** Crear Producto ***   
    def crear_producto():
        try:
            # Verificar si el archivo de clientes existe, y crearlo si no
            if not os.path.isfile("productos.json"):
                with open("productos.json", "w") as archivo:
                    json.dump([], archivo)

            # Leer los clientes del archivo
            with open("productos.json", "r") as archivo:
                productos = json.load(archivo)

            sku = input('Ingrese el SKU del Producto: ')
            nombre = input('Ingrese el nombre del Producto: ')
            categoria = input('Ingrese la Categoría del Producto: ')
            proveedor = input('Ingrese Proveedor del Producto: ')
            stock = int(input('Ingrese el Stock del Producto: '))
            valor_neto = int(input("Ingrese el valor neto del producto: "))
            

            # Crear un diccionario con los datos del usuario
            impuesto = 1.19
            nuevo_producto = {
                "sku": sku,
                "nombre": nombre,
                "categoria": categoria,
                "proveedor": proveedor,
                "stock": stock,
                "valor_neto": valor_neto,
                "impuesto": impuesto,
                "valor_bruto": valor_neto*impuesto,
                
            }

            # Agregar el cliente al diccionario
            
            productos.append(nuevo_producto)  # agregar el producto a la lista de productos
            

            # Guardar los clientes en el archivo externo
            with open("productos.json", "w") as archivo:
                json.dump(productos, archivo)

            # Mostrar un mensaje de confirmación
            print("Producto creado con éxito")

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

# Metodo para mostrar Productos
    def mostrar_productos():
        with open('productos.json') as archivo:
            productos = json.load(archivo)
        
        if not productos:
            print('No hay Productos registrados.')

        else:
            for producto in productos:
                
                print('SKU:', producto['sku'], 'Nombre:', producto['nombre'], 'Producto', producto['categoria'],'Proveedor:', producto['proveedor'], 'Stock:', producto['stock'], 'Neto:', producto['valor_neto'], 'IVA:', producto['impuesto'], 'Total:', producto['valor_bruto'])

# Mostrar Impuesto
    def mostrar_impuesto():
        with open('productos.json') as f:
                productos = json.load(f)
                
                if not productos:
                    print('No hay Productos registrados.')

                else:
                    for producto in productos:
                        print('Nombre:', producto['nombre'], 'IVA:', producto['impuesto'])
# ****** Fin Clase Producto ******

# ****** Inicio Clase Vendedor ******
class Vendedor:
    def __init__ (self, run: str, nombre: str, apellido: str, seccion: str, comision: float = 0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision 

    def get_comision(self):
        return self.__comision
    
    def set_comision(self, nueva_comision: int):
        self.__comision = nueva_comision

    def crear_vendedor():
        try:
            # Verificar si el archivo de clientes existe, y crearlo si no
            if not os.path.isfile("vendedores.json"):
                with open("vendedores.json", "w") as archivo:
                    json.dump([], archivo)

            # Leer los clientes del archivo
            with open("vendedores.json", "r") as archivo:
                vendedores = json.load(archivo)

            run = input('Ingrese el RUN de Vendedor: ')
            nombre = input('Ingrese el Nombre de Vendedor: ')
            apellido = input('Ingrese Apellido de Vendedor: ')
            seccion = input('Ingrese Sección de Vendedor: ')
            comision = float(input('Ingrese Comisión de Vendedor: '))
            
            

            # Crear un diccionario con los datos del usuario
            
            nuevo_vendedor = {
                "run": run,
                "nombre": nombre,
                "apellido": apellido,
                "seccion": seccion,
                "comision": comision,
                                
            }

            # Agregar el cliente al diccionario
            
            vendedores.append(nuevo_vendedor)  # agregar el producto a la lista de productos
            

            # Guardar los clientes en el archivo externo
            with open("vendedores.json", "w") as archivo:
                json.dump(vendedores, archivo)

            # Mostrar un mensaje de confirmación
            print("Vendedor creado con éxito")

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

# Metodo para mostrar Vendedores
    def mostrar_vendedores():
        with open('vendedores.json') as archivo:
            vendedores = json.load(archivo)
        
        if not vendedores:
            print('No hay Vendedores registrados.')

        else:
            for vendedor in vendedores:
                
                print('RUN:', vendedor ['run'], '   Nombre : ', vendedor ['nombre'], vendedor ['apellido'], '   Sección : ', vendedor ['seccion'])

# Mostrar Comision
    def mostrar_comision():
        with open('vendedores.json') as f:
                vendedores = json.load(f)
                
                if not vendedores:
                    print('No hay Vendedores registrados.')

                else:
                    for vendedor in vendedores:
                        print('Nombre : ', vendedor ['nombre'], vendedor ['apellido'], 'Comision : ', vendedor ['comision'])


# ****** Fin Clase Vendedor ******

# ****** Inicio Clase Proveedor ******
class Proveedor:
    def __init__ (self, rut: str, nombre_legal: str, razon_social: str, pais: str, tipo: str):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo = tipo 

    

    def crear_proveedor():
        try:
            # Verificar si el archivo de clientes existe, y crearlo si no
            if not os.path.isfile("proveedores.json"):
                with open("proveedores.json", "w") as archivo:
                    json.dump([], archivo)

            # Leer los clientes del archivo
            with open("proveedores.json", "r") as archivo:
                proveedores = json.load(archivo)

            rut = input('Ingrese el RUT de Proveedor: ')
            nombre_legal = input('Ingrese el Nombre Legal: ')
            razon_social = input('Ingrese Razón Social : ')
            pais = input('Ingrese Pais: ')
            tipo = input('Ingrese Tipo de Sociedad (Persona Natural / Persona Jurídica ): ')
            
            

            # Crear un diccionario con los datos del usuario
            
            nuevo_proveedor = {
                "rut": rut,
                "nombre legal": nombre_legal,
                "razon social": razon_social,
                "pais": pais,
                "tipo": tipo,
                                
            }

            # Agregar el proveedor al diccionario
            
            proveedores.append(nuevo_proveedor)  # agregar proveedor a lista de proveedores
            

            # Guardar los proveedores en el archivo externo
            with open("proveedores.json", "w") as archivo:
                json.dump(proveedores, archivo)

            # Mostrar un mensaje de confirmación
            print("Proveedor creado con éxito")

        except Exception as e:
            print(f"Ocurrió un error: {str(e)}")

# Metodo para mostrar Vendedores
    def mostrar_proveedores():
        with open('proveedores.json') as archivo:
            proveedores = json.load(archivo)
        
        if not proveedores:
            print('No hay Vendedores registrados.')

        else:
            for proveedor in proveedores:
                
                print('RUT:', proveedor ['rut'], '   Nombre Legal : ', proveedor ['nombre legal'], 'Razon Social', proveedor ['razon social'], '   Pais : ', proveedor ['pais'], '   Tipo Sociedad : ', proveedor ['tipo'])

# Mostrar Comision
    def mostrar_tipo():
        with open('proveedores.json') as f:
                proveedores = json.load(f)
                
                if not proveedores:
                    print('No hay Proveedores registrados.')

                else:
                    for proveedor in proveedores:
                        print('RUT : ', proveedor ['rut'], proveedor ['razon social'], 'Tipo Sociedad : ', proveedor ['tipo'])


# ****** Fin Clase Proveedor ******



# *****  Menú Cliente *****

def menu_clientes():
    os.system("cls" if os.name == "nt" else "clear") # Limpia pantalla
    while True:
        print('--- Menú ---')
        print('1. Crear cliente')
        print('2. Mostrar clientes')
        print('3. Agregar saldo a un cliente')
        print('4. Mostrar saldo de un cliente')
        print('0. Volver')
        
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

# *****  Fin Menú Cliente *****

# *****  Menú Producto *****
def menu_productos():
    os.system("cls" if os.name == "nt" else "clear") # Limpia pantalla
    while True:
        print('--- Menú ---')
        print('1. Crear Producto')
        print('2. Mostrar Productos')
        print('3. Mostrar Impuesto')
        print('0. Volver')
        
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            
            Producto.crear_producto()  # llamar al método en la instancia creada
                    
        elif opcion == '2':
            Producto.mostrar_productos()
        
        elif opcion == '3':
            Producto.mostrar_impuesto()
        
        elif opcion == '4':
            pass

        elif opcion == '0':
            break

        else:
            print('Opción inválida. Por favor, intente nuevamente.')

# *****  Fin Menú Producto *****

# *****  Menú Vendedor *****
def menu_vendedor():
    os.system("cls" if os.name == "nt" else "clear") # Limpia pantalla
    while True:
        print('--- Menú ---')
        print('1. Crear Vendedor')
        print('2. Mostrar Vendedores')
        print('3. Mostrar Comision')
        print('0. Volver')
        
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            
            Vendedor.crear_vendedor()  # llamar al método en la instancia creada
                    
        elif opcion == '2':
            Vendedor.mostrar_vendedores()
        
        elif opcion == '3':
            Vendedor.mostrar_comision()
        
        elif opcion == '4':
            pass

        elif opcion == '0':
            break

        else:
            print('Opción inválida. Por favor, intente nuevamente.')

# *****  Fin Menú Producto *****

# *****  Menú Proveedor *****
def menu_proveedor():
    os.system("cls" if os.name == "nt" else "clear") # Limpia pantalla
    while True:
        print('--- Menú ---')
        print('1. Crear Proveedor')
        print('2. Mostrar Proveedores')
        print('3. Mostrar Tipo Sociedad')
        print('0. Volver')
        
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            
            Proveedor.crear_proveedor()  # llamar al método en la instancia creada
                    
        elif opcion == '2':
            Proveedor.mostrar_proveedores()
        
        elif opcion == '3':
            Proveedor.mostrar_tipo()
        
        elif opcion == '4':
            pass

        elif opcion == '0':
            break

        else:
            print('Opción inválida. Por favor, intente nuevamente.')

# *****  Fin Menú Proveedor *****


# *********** Menú Pricipal ************
while True:
        os.system("cls" if os.name == "nt" else "clear") # Limpia Pantalla
        print('--- Menú ---')
        print('1. Clientes')
        print('2. Productos')
        print('3. Vendedor')
        print('4. Proveedor')
        print('0. Salir')
        
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            menu_clientes()
        
        elif opcion == '2':
            menu_productos()
        
        elif opcion == '3':
            menu_vendedor()
        
        elif opcion == '4':
            menu_proveedor()

        elif opcion == '0':
            break

        else:
            print('Opción inválida. Por favor, intente nuevamente.')