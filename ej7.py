# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve
# Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número
# de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

def login(nombre_usuario, contrasena, intentos):
    # Verifica si el nombre de usuario y la contraseña son correctos
    if nombre_usuario == "usuario1" and contrasena == "asdasd":
        return True, intentos  # Retorna Verdadero y el número de intentos
    else:
        intentos += 1  # Incrementa el número de intentos
        return False, intentos  # Retorna Falso y el número de intentos incrementado


def main():
    intentos = 0  # Inicializa el contador de intentos
    while intentos < 3:
        # Solicita al usuario el nombre de usuario y la contraseña
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # Intenta hacer login
        resultado, intentos = login(nombre_usuario, contrasena, intentos)

        # Si el login es exitoso, imprime un mensaje y sale del bucle
        if resultado:
            print("¡Inicio de sesión exitoso!")
            break
        else:
            print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
    
    # Si se alcanza el límite de intentos sin éxito, imprime un mensaje
    if intentos == 3:
        print("Se ha excedido el número de intentos permitidos. Cierre el programa.")

if __name__ == "__main__":
    main()
