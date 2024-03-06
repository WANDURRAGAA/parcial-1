num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))
num3 = float(input("Ingrese un número: "))
num4 = float(input("Ingrese un número: "))
mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

if num4 > mayor:
    mayor = num4

print("El número mayor es:", mayor)