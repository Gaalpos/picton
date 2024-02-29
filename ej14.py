# Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos
# permite guardar un conjunto de variables. La característica fundamental es que el último elemento que
# se añade al conjunto es el primero que se puede sacar.
# Para representar una pila vamos a utilizar una lista de cadenas de caracteres.
# Vamos a crear varias funciones para trabajar con la pila:
# LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
# EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene
# elementos.
# EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
# AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no
# está llena. si esta llena muestra un mensaje de error.

# 4/4
# SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la
# pila. Si la pila está vacía muestra un mensaje de error.
# EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
# Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú,
# con las siguientes opciones:
# 1. Añadir elemento a la pila
# 2. Sacar elemento de la pila
# 3. Longitud de la pila
# 4. Mostrar pila
# 5. Salir

def longitud_pila(pila):
    """Devuelve el número de elementos en la pila."""
    return len(pila)

def esta_vacia_pila(pila):
    """Devuelve True si la pila está vacía, False en caso contrario."""
    return len(pila) == 0

def esta_llena_pila(pila, capacidad):
    """Devuelve True si la pila está llena (alcanzó su capacidad máxima), False en caso contrario."""
    return len(pila) == capacidad

def add_pila(elemento, pila, capacidad):
    """Añade un elemento a la pila si no está llena."""
    if not esta_llena_pila(pila, capacidad):
        pila.append(elemento)
    else:
        print("Error: La pila está llena.")

def sacar_de_la_pila(pila):
    """Devuelve y elimina el último elemento añadido a la pila."""
    if not esta_vacia_pila(pila):
        return pila.pop()
    else:
        print("Error: La pila está vacía.")

def escribir_pila(pila):
    """Muestra en pantalla los elementos de la pila."""
    print("Elementos en la pila:")
    if not esta_vacia_pila(pila):
        for elemento in reversed(pila):
            print(elemento)
    else:
        print("La pila está vacía.")

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nMenú:")
    print("1. Añadir elemento a la pila")
    print("2. Sacar elemento de la pila")
    print("3. Longitud de la pila")
    print("4. Mostrar pila")
    print("5. Salir")

def main():
    """Programa principal."""
    pila = []
    capacidad_maxima = 5  # Capacidad máxima de la pila

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            elemento = input("Ingrese el elemento a añadir a la pila: ")
            add_pila(elemento, pila, capacidad_maxima)
        elif opcion == "2":
            elemento = sacar_de_la_pila(pila)
            if elemento:
                print(f"Se ha sacado de la pila el elemento: {elemento}")
        elif opcion == "3":
            print(f"Longitud de la pila: {longitud_pila(pila)}")
        elif opcion == "4":
            escribir_pila(pila)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-5).")

if __name__ == "__main__":
    main()
