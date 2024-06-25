supermercado = {}

while True:
    producto = input("Ingrese un producto (o presione Enter para finalizar): ")
    if producto == "":
        break
    cantidad = int(input("Ingrese la cantidad del producto: "))
    supermercado[producto] = cantidad

x = int(input("Ingrese un valor numérico X: "))

print("Productos con cantidades multiplicadas por", x, ":")
for producto in supermercado:
    print(producto, ":", supermercado[producto] * x)