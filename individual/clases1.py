from __future__ import annotations
import json


class Usuario:
    nombre: str
    clave: str
    perfil: str
    id: int

    def __init__(self, id, nombre, clave, perfil):
        self.id = id
        self.nombre = nombre
        self.clave = clave
        self.perfil = perfil
    
    class Interfaces():
        def formulario_datos() -> Usuario:
            usuario: Usuario = Usuario(0, "", "", "")# crear objeto usuario con valores por defecto
            print("Crear nuevo usuario:")
            usuario.nombre = input("Nombre de usuario: ")
            usuario.clave = input("Contraseña: ")
            usuario.perfil = input("Perfil (administrador/vendedor/bodeguero): ")
            return usuario
    
    @classmethod
    def mostrar_usuarios(cls):
        # Abrir el archivo de usuarios
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)

        # Mostrar el listado de usuarios
        print("Listado de usuarios:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Perfil: {usuario['perfil']}")
            
    
    @classmethod
    def seleccionar_usuario(cls):
        id_usuario = input("Ingrese el ID del usuario que desea seleccionar: ")
        return int(id_usuario)

    @classmethod
    def crear_usuario(cls):
        # Abrir el archivo de usuarios
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)

        # Preguntar por los datos del nuevo usuario
        nuevo_usuario = cls.Interfaces.formulario_datos()

        # Obtener el id del nuevo usuario
        id_usuario = usuarios[-1]['id'] + 1 if usuarios else 1

        # Crear un nuevo usuario con los datos ingresados
        nuevo_usuario = cls(id_usuario, nuevo_usuario.nombre, nuevo_usuario.clave, nuevo_usuario.perfil)

        # Agregar el nuevo usuario a la lista de usuarios
        usuarios.append({
            "id": nuevo_usuario.id,
            "nombre": nuevo_usuario.nombre,
            "clave": nuevo_usuario.clave,
            "perfil": nuevo_usuario.perfil
        })

        # Guardar la lista de usuarios en el archivo
        with open("usuarios.json", "w") as archivo:
            json.dump(usuarios, archivo)

    @classmethod
    def eliminar_usuario(cls):
        # Mostrar el listado de usuarios
        cls.mostrar_usuarios()

        # Seleccionar el usuario a eliminar
        id_usuario = cls.seleccionar_usuario()
        
        # Abrir el archivo de usuarios
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)

        # Buscar el usuario a eliminar
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario["id"] == id_usuario:
                usuarios.remove(usuario)  # Eliminar el usuario de la lista de usuarios
                usuario_encontrado = True
                break

        # Si se encontró el usuario, guardar la lista de usuarios actualizada en el archivo
        if usuario_encontrado:
            with open("usuarios.json", "w") as archivo:
                json.dump(usuarios, archivo)
            print(f"Usuario con id {id_usuario} eliminado correctamente.")
        else:
            print(f"No se encontró ningún usuario con id {id_usuario}.")

    @classmethod
    def modificar_usuario(cls):
        # Mostrar el listado de usuarios
        cls.mostrar_usuarios()

        # Seleccionar el usuario a modificar
        id_usuario = cls.seleccionar_usuario()

        # Abrir el archivo de usuarios
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)

        # Buscar el usuario a modificar
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario["id"] == id_usuario:
                usuario_encontrado = True
                break

        # Si se encontró el usuario, solicitar nuevos datos y modificarlos
        if usuario_encontrado:
            print(f"Modificar usuario con id {id_usuario}:")
            nuevo_nombre = input("Nuevo nombre de usuario: ")
            nueva_clave = input("Nueva contraseña: ")
            nuevo_perfil = input("Nuevo perfil (administrador/vendedor/bodeguero): ")

            usuario["nombre"] = nuevo_nombre
            usuario["clave"] = nueva_clave
            usuario["perfil"] = nuevo_perfil

        # Guardar la lista de usuarios actualizada en el archivo
            with open("usuarios.json", "w") as archivo:
                json.dump(usuarios, archivo)
        else:
            print(f"No se encontró ningún usuario con id {id_usuario}.")

    @classmethod
    def muestra_usuarios_registrados(cls):
        # Mostrar el listado de usuarios
        cls.mostrar_usuarios()

        # para pausar muestra
        input("Presione Enter para continuar")


    @classmethod
    def login(cls, nombre, clave):
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
        for usuario in usuarios:
            if usuario["nombre"] == nombre and usuario["clave"] == clave:
                return usuario["perfil"]
        return None