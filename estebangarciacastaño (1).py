# Datos del empleado
Nombre = str (input ("ingrese el nombre del empleado: "))
Numero_de_hijos = int (input ("ingrese el numero de hijos: "))
Valor_hora_regular = 10000
Horas_trabajadas = float (input("ingrese numero de horas trabajadas por semana: "))
Horas_regulares = min(Horas_trabajadas,47)
Hora_extras = max(Horas_trabajadas - 47, 0)
Valor_extra = (Valor_hora_regular * 0.35) + Valor_hora_regular


# Horas de bonificacion
if Numero_de_hijos < 3:
    Horas_bonificacion = Numero_de_hijos * 5
else:
    Horas_bonificacion = Numero_de_hijos * 10

# Calcular bonificacion
bonificacion = Horas_bonificacion * Valor_hora_regular

# Calcular salario regular
salario_regular = Horas_trabajadas * Valor_hora_regular

# Calcular horas extras y recargo
recargo_horas_extra = Hora_extras * Valor_extra

# Calcular salario total
salario_total = salario_regular + bonificacion + recargo_horas_extra


# Mostrar datos del empleado
print(f"Nombre: {Nombre}")
print(f"Número de Hijos: {Numero_de_hijos}")
print(f"Horas de Bonificación: {Horas_bonificacion} horas")
print(f"Tarifa por Hora: ${Valor_hora_regular}")
print(f"Horas Regulares Trabajadas: {Horas_regulares} horas")
print(f"Horas Regulares: {Horas_regulares} horas")
print(f"Horas Extras: {Hora_extras} horas")
print(f"Salario Regular: ${salario_regular}")
print(f"Bonificación: ${bonificacion}")
print(f"Recargo por Horas Extras: ${recargo_horas_extra}")
print(f"Salario Total: ${salario_total}")
