Proceso menu_opciones
	Escribir "eligue una opcion"
	Escribir "1--sumar"
	Escribir "2--restar"
	Escribir "3--multiplicar"
	Escribir "4--dividir"
	leer opcion1
	
	Escribir "escribe el primer numero"
	leer numero1
	Escribir "ingresa el segundo numero"
	Leer numero2
	
	segun opcion1 Hacer
		caso 1:
			resultado=numero1+numero2
			escribir "el resultado de la suma es:" resultado
		caso 1:
			resultado=numero1+numero2
			escribir "el resultado de la suma es:" resultado
		caso 2:
			resultado=numero1-numero2
			escribir "el resultado de la resta es:" resultado
		caso 3:
			resultado=numero1*numero2
			escribir "el resultado de la multiplicacion es:" resultado
		caso 4:
			resultado=numero1/numero2
			escribir "el resultado de la division es:" resultado
			
		De Otro Modo:
			escribir "opcion invalida"
	FinSegun
	
	
	
	
	
FinProceso
