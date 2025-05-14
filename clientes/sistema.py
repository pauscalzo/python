usuarios = {
    "admin": "123",
    "paula": "1234",
    "rodrigo": "12345"
}

def introducir_credenciales():
    username = input("Usuario: ")
    password = input("Contraseña: ")
    return username, password

def registrar_usuario():
    print("\n--- Registro de nuevo usuario ---")
    username, password = introducir_credenciales()
    if username in usuarios:
        print("Ese nombre de usuario ya existe.")
    else:
        usuarios[username] = password
        print("Usuario registrado con éxito.")

def login():
    print("\n--- Iniciar sesión ---")
    username, password = introducir_credenciales()
    if usuarios.get(username) == password:
        print("¡Bienvenido/a,", username + "!")
        return True
    else:
        print("Acceso denegado.")
        return False

def mostrar_usuarios():
    print("\n--- Usuarios registrados ---")
    for usuario in usuarios:
        print("-", usuario)
