Proceso clasificacion_edad
	Escribir "ingrese su edad:"
	leer edad1
	//Si tiene menos de 12 a�os, muestra "Eres un ni�o".
	
	//Si tiene entre 13 y 17 a�os, muestra "Eres un adolescente".
		
		//Si tiene 18 a�os o m�s, muestra "Eres un adulto".
	
	si edad1 > 12 Y edad1< 17 Entonces
		Imprimir "eres un adolecente"
	SiNo
		si edad1 <= 12 Entonces
			Imprimir "eres un ni�o"
		SiNo
			Imprimir "eres un adulto"
		FinSi
		
		
	FinSi
	
FinProceso
