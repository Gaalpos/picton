# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en
# pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes
# del texto). Además subraya el mensaje utilizando el carácter =.

def EscribirCentrado(texto):
    anchura_pantalla = 80
    longitud_texto = len(texto)
    espacios_antes = (anchura_pantalla - longitud_texto) // 2
    print("=" * anchura_pantalla)
    print(" " * espacios_antes + texto)
    print("=" * anchura_pantalla)

# Ejemplo de uso:
texto_ejemplo = "Hola, mundo!"
EscribirCentrado(texto_ejemplo)
