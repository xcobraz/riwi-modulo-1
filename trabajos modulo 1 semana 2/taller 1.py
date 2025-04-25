#determinar el estado de aprobacion

notaAprobacion=int(input("ingrese la nota con la que van a aprobar los estudiantes entre 0 y 100: "))

#la enntrada mmultiple que va a estar separda por notas

notasx=input("ingrese las notas separadas por una coma ',' ")

#sumatoria empieza por 0 para asi pueda coger cualquier valor en el ciclo

sumatoriaNotas=0
j=0
numeroDeNotasArribaDelPromedio=0

#con esto va a meter el sting que recibimos en una lista seoarando valores por la coma

listaNotas=notasx.split(",")
#print(listaNotas)

#en este ciclo va recorrer la lista y hacer la sumatoria total de las notas

for i in range(1,len(listaNotas)+1):
    sumatoriaNotas+=i
  #  print("loop de notas: " ,sumatoriaNotas)

elemento=0

listaNotas_enteras=list(map(int, listaNotas))
#print("lista enteros ",listaNotas_enteras)

numeroDeNotasArribaDelPromedio=0
numeroBusqueda=float(input("ingrese la nota que quiere ver si saco igual o superior: "))
while j < len(listaNotas_enteras):
    notas=listaNotas_enteras[j]
    j+=1

    #print("estas son las notas ",notas)
    
    if notas >= numeroBusqueda:
        numeroDeNotasArribaDelPromedio+=1
        
    else:
        continue
   # print("notas de aprobacion son: ",numeroDeNotasArribaDelPromedio)

print("el numero de notas que gano: ",numeroDeNotasArribaDelPromedio)

#ahora hace el promedio con la sumatoria de las notas y se divide por la cantidad de datos ingresados (len)

promedio=sumatoriaNotas/len(listaNotas)
print("el promedio de notas es: ",promedio)



#este condicional se basa en el promedio para definir si el estudiante aprobo o no
#en base al dato de nota de aprobacion

if notaAprobacion < 0 or notaAprobacion> 100:
    print("la nota de aprobacion no esta entre 0 y 100")
elif promedio>=notaAprobacion:
    print("el estudiante aprobo")
else:
    print("el estudiante reprobo")


#verificacion y conteo 

valorVerificacion=int(input("ingrese el valor de la nota que quiere verificar: "))

numeroNotas=0
l=0
for l in listaNotas_enteras:
    l+=1
    notaV=listaNotas_enteras[l]
    if notaV==valorVerificacion:
        numeroNotas+=1
    else:
        continue
print(f"el estudiante saco {numeroNotas} veces la nota {valorVerificacion} ")