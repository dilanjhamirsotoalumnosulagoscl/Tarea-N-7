
numeros = []

for i in range(10):
    num = int(input(f"Ingrese número {i+1}: "))
    numeros.append(num)

print("Los números en orden inverso son:")
for num in reversed(numeros):
    print(num)