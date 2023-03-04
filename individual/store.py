import os
import json
import time
from helpers import clear, update, open_file

# Cargar los productos desde el archivo externo
products = open_file('products.json')

def stock_view():
    for product in products: 
        print('*********************************************')
        print(f'ID: {product["id"]} / Producto: {product["name"]} / Stock: {product["stock"]}')
        print('*********************************************')
        time.sleep(1)

def action_add():
    clear()
    stock_view()
    option_product = int(input('Seleccion ID de producto: '))
    
    # Solicitamos Cantidad Stock y Validamos
    while True:
        cant_product = input('Ingrese Stock a sumar:  ')
        if cant_product.isdigit() and int(cant_product):
            break
        print("Debe ingresar una valor válido en números enteros.")
    # Recorremos la lista de diccionarios
    for product_search in products:
    # Comprobamos si el ID coincide con el que buscamos
        if product_search['id'] == option_product:
            # Modificamos los valores del diccionario
            product_search['stock'] = product_search['stock'] + int(cant_product)
            update(products, 'products.json')
            break
    clear()
    stock_view()

def action_subtract():
    clear()
    stock_view()
    option_product = int(input('Seleccion ID de producto: '))
    cant_product = input('Ingrese Stock a restar: ')
    # Recorremos la lista de diccionarios
    for product_search in products:
    # Comprobamos si el ID coincide con el que buscamos
        if product_search['id'] == option_product:
            # Modificamos los valores del diccionario
            product_search['stock'] = product_search['stock'] - int(cant_product)
            update(products, 'products.json')
            break
    clear()
    stock_view()

def action_add_product():
    clear()
    name = input('Ingrese el nombre del nuevo producto: ')
    while True:
        stock = input('Ingrese Stock de Producto:  ')
        if stock.isdigit() and int(stock):
            break
        print("Debe ingresar una valor válido en números enteros.")

    new_product = {'id':len(products)+1, 'name': name, 'stock': stock}
    
    # Agregar el nuevo producto a la lista de productos
    products.append(new_product)
    update(products, 'products.json')
    clear()
    stock_view()

def action_remove_product():
    clear()
    stock_view()
    option_product = int(input('Seleccion ID de producto: '))
    # Recorremos la lista de diccionarios
    for product_search in products:
        # Comprobamos si el ID coincide con el que buscamos
        if product_search['id'] == option_product:
            # Eliminamos el producto de la lista
            products.remove(product_search)
            update(products, 'products.json')
            break
    clear()
    stock_view()



 