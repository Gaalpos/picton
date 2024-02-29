# Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a
# utilizar dos enteros: numerador y denominador.
# Vamos a crear las siguientes funciones para trabajar con funciones:
# Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador.
# Cuando leas una fracción debes simplificarla.
# Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra
# sólo el numerador.
# Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
# Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y
# dominador por el MCD del numerador y denominador.
# Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos
# fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y
# denominador=d1*d2. Se debe simplificar la fracción resultado.
# Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y
# denominador=d1*d2. Se debe simplificar la fracción resultado.
# Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello
# numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello
# numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
# Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
# 1. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
# 2. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
# 3. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
# 4. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
# 5. Salir

def leer_fraccion():
    """Lee por teclado una fracción y la devuelve como una tupla (numerador, denominador)."""
    while True:
        try:
            numerador = int(input("Ingrese el numerador: "))
            denominador = int(input("Ingrese el denominador: "))
            if denominador == 0:
                print("Error: El denominador no puede ser cero.")
                continue
            else:
                return simplificar_fraccion(numerador, denominador)
        except ValueError:
            print("Error: Ingrese valores numéricos para el numerador y el denominador.")

def escribir_fraccion(numerador, denominador):
    """Escribe en pantalla la fracción simplificada."""
    if denominador == 1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")

def calcular_mcd(a, b):
    """Calcula el máximo común divisor (MCD) de dos números."""
    while b != 0:
        a, b = b, a % b
    return a

def simplificar_fraccion(numerador, denominador):
    """Simplifica la fracción dividiendo el numerador y el denominador por su máximo común divisor (MCD)."""
    mcd = calcular_mcd(numerador, denominador)
    return numerador // mcd, denominador // mcd

def sumar_fracciones(n1, d1, n2, d2):
    """Suma dos fracciones y devuelve el resultado simplificado."""
    numerador = n1 * d2 + d1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def restar_fracciones(n1, d1, n2, d2):
    """Resta dos fracciones y devuelve el resultado simplificado."""
    numerador = n1 * d2 - d1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def multiplicar_fracciones(n1, d1, n2, d2):
    """Multiplica dos fracciones y devuelve el resultado simplificado."""
    numerador = n1 * n2
    denominador = d1 * d2
    return simplificar_fraccion(numerador, denominador)

def dividir_fracciones(n1, d1, n2, d2):
    """Divide dos fracciones y devuelve el resultado simplificado."""
    numerador = n1 * d2
    denominador = d1 * n2
    return simplificar_fraccion(numerador, denominador)

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nMenú:")
    print("1. Sumar dos fracciones")
    print("2. Restar dos fracciones")
    print("3. Multiplicar dos fracciones")
    print("4. Dividir dos fracciones")
    print("5. Salir")

def main():
    """Programa principal."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            print("\nSumar dos fracciones:")
            n1, d1 = leer_fraccion()
            n2, d2 = leer_fraccion()
            resultado = sumar_fracciones(n1, d1, n2, d2)
            print("El resultado de la suma es:")
            escribir_fraccion(*resultado)
        elif opcion == "2":
            print("\nRestar dos fracciones:")
            n1, d1 = leer_fraccion()
            n2, d2 = leer_fraccion()
            resultado = restar_fracciones(n1, d1, n2, d2)
            print("El resultado de la resta es:")
            escribir_fraccion(*resultado)
        elif opcion == "3":
            print("\nMultiplicar dos fracciones:")
            n1, d1 = leer_fraccion()
            n2, d2 = leer_fraccion()
            resultado = multiplicar_fracciones(n1, d1, n2, d2)
            print("El resultado de la multiplicación es:")
            escribir_fraccion(*resultado)
        elif opcion == "4":
            print("\nDividir dos fracciones:")
            n1, d1 = leer_fraccion()
            n2, d2 = leer_fraccion()
            if n2 == 0:
                print("Error: No se puede dividir por cero.")
                continue
            resultado = dividir_fracciones(n1, d1, n2, d2)
            print("El resultado de la división es:")
            escribir_fraccion(*resultado)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-5).")

if __name__ == "__main__":
    main()
