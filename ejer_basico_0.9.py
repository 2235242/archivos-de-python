##programa para poder hallar el perimetro ya area de un triangulo rectangulo
print("por favor digite el valor del lado 1 del triangulo rectangulo")
lado_1=float(input())
print("por favor digite el valor del lado 2 del triangulo rectangulo")
lado_2=float(input())
print("por favor digite el valor del lado 3 del triangulo rectangulo, que va a ser tomado como la hipotenusa ")
lado_3=float(input())
perimetro=(lado_1 + lado_2 + lado_3)
print("el valor del perimetro del triangulo rectangulo es:", perimetro)
area= (lado_1 * lado_2 / 2)