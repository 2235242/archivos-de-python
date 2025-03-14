##programa para mostrar datos de empleados con condicional if para determinar si gana el salario minimo o no
##pido datos
print("bievenido al programa ")
nombre=input("digite su nombre:")
apellido=input("digite su apellido: ")
documento=input("digite su numero de documento de identidad: ")
sueldo=float(input("digite su sueldo: "))
salario_minimo= 1.623000
if sueldo >= salario_minimo:
    print("este empleado tiene un sueldo mayor al salario mininmo")
else:
    print("este empleado tiene un salario menor al del salario minimo")
print("informacion del empleado")
print("nombre: ", nombre)
print("apellido: ", apellido)
print("documento de identidad: ", documento)