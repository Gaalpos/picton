# Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides
# es el siguiente:
# Se divide el número mayor entre el menor.
# Si la división es exacta, el divisor es el MCD.
# Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma
# hasta obtener una división exacta, siendo el último divisor el MCD.
# Crea un programa principal que lea dos números enteros y muestre el MCD.

def mcd_euclides(a, b):
    """Calcula el MCD de dos números utilizando el método de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

def main():
    """Programa principal."""
    try:
        # Solicita al usuario dos números enteros
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))

        # Calcula el MCD de los dos números y muestra el resultado
        mcd = mcd_euclides(num1, num2)
        print(f"El MCD de {num1} y {num2} es: {mcd}")

    except ValueError:
        print("Error: Por favor, ingrese dos números enteros válidos.")

if __name__ == "__main__":
    main()
