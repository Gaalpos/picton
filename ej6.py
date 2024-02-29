# Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un
# programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

import math

def calcular_area_perimetro_circunferencia(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def programa_principal():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    area, perimetro = calcular_area_perimetro_circunferencia(radio)
    print(f"El área de la circunferencia es: {area:.2f}")
    print(f"El perímetro de la circunferencia es: {perimetro:.2f}")

if __name__ == "__main__":
    programa_principal()
