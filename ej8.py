# Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal
# donde se lea un entero y se muestre el resultado del factorial.

def factorial(n):
    """Función recursiva para calcular el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Programa principal."""
    try:
        # Solicita al usuario un número entero
        numero = int(input("Ingrese un número entero para calcular su factorial: "))

        # Verifica si el número es negativo
        if numero < 0:
            print("El factorial no está definido para números negativos.")
        else:
            # Calcula y muestra el factorial del número
            resultado = factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
