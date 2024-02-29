# El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido
# desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha
# nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
# LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
# DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
# EsBisiesto: Recibe un año y nos dice si es bisiesto.
# Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

def leer_fecha():
    """Lee por teclado una fecha (día, mes y año) y la devuelve como una tupla."""
    try:
        dia = int(input("Ingrese el día (1-31): "))
        mes = int(input("Ingrese el mes (1-12): "))
        anio = int(input("Ingrese el año: "))
        return dia, mes, anio
    except ValueError:
        print("Error: Ingrese valores numéricos para el día, mes y año.")

def dias_del_mes(mes, anio):
    """Recibe un mes y un año y devuelve los días de ese mes en ese año."""
    meses_31 = {1, 3, 5, 7, 8, 10, 12}
    meses_30 = {4, 6, 9, 11}

    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    elif mes in meses_31:
        return 31
    elif mes in meses_30:
        return 30
    else:
        return None

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

    if dias_del_mes(mes, anio) is None:
        print("Error: El mes ingresado no es válido.")
    else:
        dia_juliano = calcular_dia_juliano(dia, mes, anio)
        print(f"El día juliano correspondiente a la fecha ingresada es: {dia_juliano}")

if __name__ == "__main__":
    main()
