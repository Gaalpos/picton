# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor
# máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo,
# utilizando la función anterior.

def calcularMaxMin(lista_numeros):
    if not lista_numeros:
        return None, None  # Si la lista está vacía, devuelve None para máximo y mínimo

    maximo = minimo = lista_numeros[0]  # Inicializa máximo y mínimo con el primer elemento de la lista
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    return maximo, minimo

def programa_principal():
    lista_numeros = []
    continuar = True
    
    while continuar:
        try:
            numero = float(input("Ingrese un número (o cualquier letra para terminar): "))
            lista_numeros.append(numero)
        except ValueError:
            continuar = False

    maximo, minimo = calcularMaxMin(lista_numeros)
    if maximo is not None and minimo is not None:
        print(f"El máximo de la lista es: {maximo}")
        print(f"El mínimo de la lista es: {minimo}")
    else:
        print("La lista está vacía.")

if __name__ == "__main__":
    programa_principal()
