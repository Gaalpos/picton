# Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura
# de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el
# primer elemento que se añade al conjunto es el primero que se puede sacar.
# En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es
# la que tienes que modificar.

def longitud_cola(cola):
    """Devuelve el número de elementos en la cola."""
    return len(cola)

def esta_vacia_cola(cola):
    """Devuelve True si la cola está vacía, False en caso contrario."""
    return len(cola) == 0

def esta_llena_cola(cola, capacidad):
    """Devuelve True si la cola está llena (alcanzó su capacidad máxima), False en caso contrario."""
    return len(cola) == capacidad

def add_cola(elemento, cola, capacidad):
    """Añade un elemento a la cola si no está llena."""
    if not esta_llena_cola(cola, capacidad):
        cola.append(elemento)
    else:
        print("Error: La cola está llena.")

def sacar_de_la_cola(cola):
    """Devuelve y elimina el primer elemento añadido a la cola."""
    if not esta_vacia_cola(cola):
        return cola.pop(0)
    else:
        print("Error: La cola está vacía.")

def escribir_cola(cola):
    """Muestra en pantalla los elementos de la cola."""
    print("Elementos en la cola:")
    if not esta_vacia_cola(cola):
        for elemento in cola:
            print(elemento)
    else:
        print("La cola está vacía.")

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nMenú:")
    print("1. Añadir elemento a la cola")
    print("2. Sacar elemento de la cola")
    print("3. Longitud de la cola")
    print("4. Mostrar cola")
    print("5. Salir")

def main():
    """Programa principal."""
    cola = []
    capacidad_maxima = 5  # Capacidad máxima de la cola

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            elemento = input("Ingrese el elemento a añadir a la cola: ")
            add_cola(elemento, cola, capacidad_maxima)
        elif opcion == "2":
            elemento = sacar_de_la_cola(cola)
            if elemento:
                print(f"Se ha sacado de la cola el elemento: {elemento}")
        elif opcion == "3":
            print(f"Longitud de la cola: {longitud_cola(cola)}")
        elif opcion == "4":
            escribir_cola(cola)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-5).")

if __name__ == "__main__":
    main()
