palabras = []

while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if palabra == "":
        break
    palabras.append(palabra)

for palabra in palabras:
    c = 0
    for char in palabra:
        if char == "A" or char == "a":
            c += 1
    print("La palabra '" + palabra + "' tiene " + str(c) + " caracteres 'A' o 'a'")