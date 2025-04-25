Proceso clasificacion_edad
	Escribir "ingrese su edad:"
	leer edad1
	//Si tiene menos de 12 años, muestra "Eres un niño".
	
	//Si tiene entre 13 y 17 años, muestra "Eres un adolescente".
		
		//Si tiene 18 años o más, muestra "Eres un adulto".
	
	si edad1 > 12 Y edad1< 17 Entonces
		Imprimir "eres un adolecente"
	SiNo
		si edad1 <= 12 Entonces
			Imprimir "eres un niño"
		SiNo
			Imprimir "eres un adulto"
		FinSi
		
		
	FinSi
	
FinProceso
