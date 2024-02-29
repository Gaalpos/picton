# Escribir dos funciones que permitan calcular:
# La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos,
# convertir a horas,minutos y segundos o salir del programa.

def tiempo_a_segundos(horas, minutos, segundos):
    """Convierte un tiempo dado en horas, minutos y segundos a la cantidad total de segundos."""
    return horas * 3600 + minutos * 60 + segundos

def segundos_a_tiempo(segundos):
    """Convierte una cantidad dada de segundos a horas, minutos y segundos."""
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

def main():
    """Programa principal."""
    while True:
        print("\nMenú:")
        print("1. Convertir a segundos")
        print("2. Convertir a horas, minutos y segundos")
        print("3. Salir")

        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == "1":
            horas = int(input("Ingrese horas: "))
            minutos = int(input("Ingrese minutos: "))
            segundos = int(input("Ingrese segundos: "))
            total_segundos = tiempo_a_segundos(horas, minutos, segundos)
            print(f"El tiempo ingresado equivale a {total_segundos} segundos.")
        elif opcion == "2":
            segundos = int(input("Ingrese la cantidad de segundos: "))
            horas, minutos, segundos_restantes = segundos_a_tiempo(segundos)
            print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
