Proceso ejercicio_semana9
	Dimension productos[5];
	i=0
	mientras i<5 Hacer
		escribir "digite el nombre del producto "
		Leer producto
		inicialProducto=SubCadena(producto,0,0);
		si inicialProducto=="M" o inicialProducto=="m" Entonces
			productos[i]=producto
			i=i+1
		SiNo
			Escribir "no es valido la inicial no es M"
		FinSi
	FinMientras
	
	j=0
	Mientras j<5 Hacer
		Imprimir  "tienes en la pocision " , j , " : " ,productos[j];	
		j=j+1
	Fin Mientras
	
FinProceso
