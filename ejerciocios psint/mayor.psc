Proceso mayor
	Escribir "ingresa el numero 1:"
	Leer numero1
	Escribir "ingresa el numero 2:"
	Leer numero2
	Escribir "ingresa el numero 3:"
	Leer numero3
	si numero1>numero2 Y numero1>numero3 Entonces
		Imprimir  "el numero mas grande es:" numero1
	SiNo
		si numero2>numero3 Y numero2>numero1 Entonces
			Imprimir "el numero mas grande es:" numero2
		SiNo
			Imprimir "el numero mas grande es:" numero3
		FinSi
	FinSi
FinProceso
