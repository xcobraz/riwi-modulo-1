puertoOriginal=int(3080)
nombreBD="prueba1"
nombreUsuario="pepito"
contraseña="ingreso20*"
servidor="www.riwi.com/BD:"

puerto1=int(input("ingrese el numero del puerto: "))
baseDatos1=input("ingrese el nombre de la base de datos: ")
usuario1=input("ingrese el nombre de usuario: ")
contraseña=input("ingrese la contraseña: ")

servidorVerificado=f"{servidor}{puertoOriginal}/{nombreBD}/{nombreUsuario}/{contraseña}"
servidorIngresado=f"{servidor}{puerto1}/{baseDatos1}/{usuario1}/{contraseña}"
#print(servidorVerificado)
if servidorVerificado==servidorIngresado:
    print("acceso permitido")
else:
    print("acceso denegado")