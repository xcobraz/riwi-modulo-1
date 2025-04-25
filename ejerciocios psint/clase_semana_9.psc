Proceso clase_semana_9
	
	Dimension mueble[5];
	definir palabraPrueba como caracter
	i=0;
	
	Mientras i<5 Hacer
		Escribir "digite el producto que desea guardar en la pocision " ,i;
		Leer palabraPrueba;
		inicial=SubCadena(palabraPrueba,0,0)
		si inicial=="T" o inicial=="t" Entonces
			mueble[i]=palabraPrueba
			i=i+1
		SiNo
			Escribir "No es posible guardar tu producto"
			
		FinSi
		leer mueble[i]
		
	FinMientras
	j=0
	
	Mientras j<5 Hacer
		escribir "tienes en la pocision " , j , " : " ,mueble[j];	
		j=j+1
	Fin Mientras
FinProceso
