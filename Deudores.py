deudores = {}

for i in range(5):
    rut = input("Ingrese el RUT de la persona ")
    deuda = int(input("Ingrese la deuda de la persona "))
    deudores[rut] = deuda

while True:
    rut = input("Ingrese el RUT de la persona a abonar (o presione Enter para finalizar) ")
    if rut == "":
        break
    if rut not in deudores:
        print("No existe un deudor con ese RUT")
    else:
        abono = int(input("Ingrese el monto del abono "))
        deudores[rut] = deudores[rut] - abono
        if deudores[rut] <= 0:
            del deudores[rut]

print("Personas que quedaron deudoras y sus respectivos saldos de deuda:")
for rut in deudores:
    print("RUT: " + rut + ", Deuda: " + str(deudores[rut]))
