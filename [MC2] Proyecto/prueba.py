
def recorridoancho(vertices,aristas):
	grafo = {}
	recorridos = []
	vertices.sort()
	for vertice in vertices:
		ady = []
		for arista in aristas:
			aux = arista.split('--')
			if vertice == aux[0]:
				ady.append(aux[1])
			elif vertice == aux[1]:
				ady.append(aux[0])
		ady.sort()
		grafo[vertice] = ady

	origen = min(grafo.items())[0]


	visitados = []
	cola = []
	colapadre = []
	#Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA COLA
	padre = origen
	cola.append(origen)
	colapadre.append(padre)
	#Paso 2: MIENTRAS LA COLA NO ESTE VACÍA
	while cola:
		#paso 3: DESENCOLAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
		actual = cola.pop(0)
		padre = colapadre.pop(0)

		#paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
		if actual not in visitados:
			#paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
			if actual != padre:
				recorridos.append(f'{padre}--{actual}')
			#paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
			visitados.append(actual)
		#paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
		#        Y QUE NO HA SIDO VISITADO:
		#        ENCOLAR EL VERTICE
		for key in grafo[actual]:
			if key not in visitados:
				cola.append(key)
				colapadre.append(actual)

	return recorridos
