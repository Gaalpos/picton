# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del
# segundo.

def EsMultiplo(numero1, numero2):
    if numero2 == 0:
        return False
    return numero1 % numero2 == 0

def main():
    numero1 = int(input("Ingrese el primer número entero: "))
    numero2 = int(input("Ingrese el segundo número entero: "))

    if EsMultiplo(numero1, numero2):
        print(f"{numero1} es múltiplo de {numero2}.")
    elif EsMultiplo(numero2, numero1):
        print(f"{numero2} es múltiplo de {numero1}.")
    else:
        print("Ninguno de los números es múltiplo del otro.")

if __name__ == "__main__":
    main()
