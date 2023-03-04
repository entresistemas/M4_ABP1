import json
import time
from helpers import clear, update, open_file

# Cargar los datos de clientes desde el archivo
clients = open_file('clients.json')

def client_view():
    for client in clients: 
        print('*********************************************')
        print(f'ID: {client["id"]} / Nombre: {client["name"]} / Apellido: {client["last_name"]} / Edad: {client["age"]} / Contraseña: {client["password"]}')
        print('*********************************************')
        time.sleep(1)

def add_client():
    while True:
        name = input('Ingrese Nombre: ')
        if name.isalpha():
            break
        print("Debe ingresar un nombre válido con solo letras.")

    while True:
        last_name = input('Ingrese Apellido: ')
        if last_name.isalpha():
            break
        print("Debe ingresar un apellido válido con solo letras.")
    
    while True:
        age = input('Ingrese Edad: ')
        if age.isdigit() and int(age):
            break
        print("Debe ingresar una edad válida en números enteros.")
    password = input('Ingrese Contraseña: ')
    new_client = {'id':len(clients)+1, 'name': name, 'last_name': last_name,
                  'age': age, 'password': password}
    clients.append(new_client)

    update(clients, 'clients.json')
    clear()
    client_view()

# Función para eliminar un cliente según su ID
def eliminar_cliente():
    client_view()
    id = input('Ingrese ID a eliminar: ')
    for i, cliente in enumerate(clients):
        if cliente["id"] == int(id):
            
            del clients[i]
            update(clients, 'clients.json')
            break
    clear()
    client_view()
