##operaciones de raices, ecuaciones de segundo grado de coeficientes reales
print("bienvenido al programa")
import math
import cmath
print("el valor de a tiene que ser diferente de 0")
a= float(input("ingrese un valor para a: "))
b= float(input("ingrese un valor para b: "))
c= float(input("ingrese un valor para c: "))
if a == 0:
    print("a no puede ser igual a 0 por lo tanto hay un eror")
else:
    D = b ** 2 - 4*a*c
    if D > 0:
        raiz_1= (-b + math.sqrt(D) / (2 * a))
        raiz_2= (-b- math.sqrt(D) / (2 * a))
        print(f"las raices son reales y distintas: x1 = {raiz_1:.4f}. x2 = {raiz_2: .4f}")
    elif D == 0:
        raiz= -b / (2 * a)
        print(f"la ecuacion tiene una unica raiz real doble : x ={raiz:.4f}")
    else:
        raiz_1=(-b -cmath.sqrt(D)) / (2 * a)
        raiz_2=(-b -cmath.sqrt(D)) / (2* a)
        print(f"las raices son complejas y conjugadas  x1 = ({raiz_1}, x2 = {raiz_2})")