numeros = []

i = 0
while i < 10:
    num = int(input("Ingrese un número: "))
    numeros = numeros + [num]
    i += 1

print("Los números en orden inverso son:")
i = len(numeros) - 1
while i >= 0:
    print(numeros[i])
    i -= 1
