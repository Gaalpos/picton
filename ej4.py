# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con
# un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa
# principal donde se use dicha función.

def ConvertirEspaciado(texto):
    nuevo_texto = ""
    for letra in texto:
        if letra != " ":
            nuevo_texto += letra + " "
        else:
            nuevo_texto += " "
    return nuevo_texto

def programa_principal():
    texto_original = input("Ingrese un texto: ")
    texto_convertido = ConvertirEspaciado(texto_original)
    print("Texto convertido:", texto_convertido)

if __name__ == "__main__":
    programa_principal()
