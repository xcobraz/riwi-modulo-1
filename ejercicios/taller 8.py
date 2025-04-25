num1=int(input("ingrese el numero 1: "))
num2=int(input("ingrese el numero 2: "))

if  num2==0:
    print("no se puede dividir por 0")
else:
    resultado=num1//num2
    print("la divison entera es: ",resultado)
if  num2==0:
    print("no se puede hacer modulo de 0")
else:
    resultadomodular=num1%num2
    print("el resultado del modulo es ",resultadomodular)