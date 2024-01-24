#Solicitar datos del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
valor_matricula = float(input("Ingrese el valor de la matrícula: "))
estrato = int(input("Ingrese el estrato del estudiante (1-6): "))

descuento = 0
recargo = 0

if estrato == 1:    descuento = 0.4
elif estrato == 2:  descuento = 0.3
elif estrato == 3:  descuento = 0.1

if estrato == 6:  recargo = 0.4
elif estrato == 5:  recargo = 0.3
elif estrato == 4:  recargo = 0.1

valor_final = valor_matricula - (valor_matricula * descuento) + (valor_matricula * recargo)

print("\nResumen de matrícula para", nombre_estudiante)
print("Valor de la matrícula: $", valor_matricula)
print("Descuento aplicado: {}%".format(descuento * 100) if descuento > 0 else "No hay descuento")
print("Recargo aplicado: {}%".format(recargo * 100) if recargo > 0 else "No hay recargo")
print("Valor final de la matrícula: $", valor_final)