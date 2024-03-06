salario_basico = float(input("Ingrese el salario del empleado: "))

if salario_basico > 1000000:
    suma_concepto = salario_basico * 0.3
else:
    suma_concepto = salario_basico * 0.2

print("el subsidio de vivienda del empleado es:", suma_concepto)