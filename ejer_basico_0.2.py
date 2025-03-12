##operaciones matematicas
print("para el ingreso de los datos que se desean operarar ingresa uno da inter e ingresa el otro dato")
print("bienvenido ingresa dos valores numericos enteros que quiera sumar")
num_1= 0
num_2= 0
suma= 0
num_1 = int(input())
num_2 = int(input())
suma= num_1 + num_2
print("el resultado de la suma es:", suma)
print("ingrese dos valores numericos enteros que quiera restar")
num_1= 0
num_2= 0
resta= 0
num_1 = int(input())
num_2 = int(input())
resta= num_1 - num_2
print("el resultado de la resta es:", resta)
print("ingrese dos valores numericos enteros que quiera multiplicar")
num_1= 0
num_2= 0
multiplicacion= 0
num_1 = int(input())
num_2 = int(input())
multiplicacion= num_1 * num_2
print("el resultado de la multiplicacion es:", multiplicacion)
print("ingrese dos valores numericos enteros que quiera dividir")
num_1= 0
num_2= 0
division= 0
num_1 = int(input())
num_2 = int(input())
division= num_1 / num_2
print("el resultado de la multiplicacion es:", division)
print("ingrese el numero de la raiz que quiera calcular")
numero=int(input())
print("ingrese el valor que del indice de la raiz")
indice= input()
resultado= pow(float(numero), int(indice))
print("el resultado de la raiz es:", resultado)
print("ingrese el numero y luego el exponente al que este elevado para hallar su potencia ")
num_1= 0
num_2= 0
potencia= 0
num_1 = int(input())
num_2 = int(input())
potencia= num_1 ** num_2
print("el resultado de la potencia es:", potencia)
print("por favor ingrese el porcentaje que desea calcular")
porcentaje= float(input())
print("ingrese el numero base")
numero= float(input())
resultado = porcentaje * numero / 100
print("el", porcentaje, "porciento de", numero , "es", resultado )