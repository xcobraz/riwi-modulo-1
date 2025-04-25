num1=int(input("ingrese el numero 1: "))
num2=int(input("ingrese el numero 2: "))

if num1>10 and num2>10:
    print("los numeros son mayores que 10")
elif num1>10 or num2>10:
    print("al menos uno es mayor que 10")
elif num1>10 and num2<10:
    print("el numero 1 es mayor que 10")
elif num1<10 and num2>10:
    print("el numero 2 es mayor que 10")
else:
    print("los numeros son menores")