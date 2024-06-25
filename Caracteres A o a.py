palabras = []
palabra = input("Ingrese una palabra (o Enter para finalizar): ")

while palabra:
    contador_a = 0
    for char in palabra:
        if char == 'a' or char == 'A':
            contador_a += 1
    palabras += [(palabra, contador_a)]
    palabra = input("Ingrese una palabra (o Enter para finalizar): ")

for palabra, contador_a in palabras:
    print("La palabra '" + palabra + "' tiene " + str(contador_a) + " letras 'A' o 'a'.")
