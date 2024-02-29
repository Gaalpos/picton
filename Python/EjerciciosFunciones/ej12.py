# Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer
# una fecha se asegura que es válida.

def leer_fecha():
    """Lee por teclado una fecha (día, mes y año) y la devuelve como una tupla."""
    while True:
        try:
            dia = int(input("Ingrese el día (1-31): "))
            mes = int(input("Ingrese el mes (1-12): "))
            anio = int(input("Ingrese el año: "))
            if validar_fecha(dia, mes, anio):
                return dia, mes, anio
            else:
                print("Error: La fecha ingresada no es válida.")
        except ValueError:
            print("Error: Ingrese valores numéricos para el día, mes y año.")

def validar_fecha(dia, mes, anio):
    """Valida si una fecha es válida."""
    if mes < 1 or mes > 12:
        return False
    
    dias_del_mes = [31, 28 if not es_bisiesto(anio) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia < 1 or dia > dias_del_mes[mes - 1]:
        return False
    
    return True

def dias_del_mes(mes, anio):
    """Recibe un mes y un año y devuelve los días de ese mes en ese año."""
    if mes == 2:
        return 28 if not es_bisiesto(anio) else 29
    elif mes in {4, 6, 9, 11}:
        return 30
    else:
        return 31

def es_bisiesto(anio):
    """Recibe un año y devuelve True si es bisiesto, False en caso contrario."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def calcular_dia_juliano(dia, mes, anio):
    """Recibe una fecha y devuelve el día juliano correspondiente."""
    dias_totales = dia
    for m in range(1, mes):
        dias_totales += dias_del_mes(m, anio)
    return dias_totales

def main():
    """Programa principal."""
    dia, mes, anio = leer_fecha()
    dia_juliano = calcular_dia_juliano(dia, mes, anio)
    print(f"El día juliano correspondiente a la fecha ingresada es: {dia_juliano}")

if __name__ == "__main__":
    main()
