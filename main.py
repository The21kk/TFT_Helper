# main.py

from nodos import Nodo
from grafo import Grafo
from busqueda import busqueda_a_estrella
from generadores import generar_transiciones_compra, generar_transiciones_objetos

# Nodo objetivo
nodo_objetivo = Nodo(
    campeones=['Ahri', 'Rumble', 'Bard', 'Hecarim', 'Shen', 'Tahm Kench', 'Varus', 'Xerath'],
    sinergias=['Arcanist', 'Bard', 'Guardian', 'Swiftshot', 'Shapeshifter', 'Scalescorn'],
    objetos=["Blue Buff", "Rabadon's Deathcap", 'Ionic Spark'],
    oro=0,
    salud=100,
    posicion=[0, 1, 2, 3, 4, 5, 6, 7]
)

# Nodo inicial
nodo_inicial = Nodo(
    campeones=[],
    sinergias=[],
    objetos=[],
    oro=50,
    salud=100,
    posicion=[]
)

# Crear grafo y agregar el nodo inicial
grafo = Grafo()
grafo.agregar_nodo(nodo_inicial)

# Expansión del grafo
frontera = [nodo_inicial]
while frontera:
    nodo_actual = frontera.pop(0)
    
    generar_transiciones_compra(grafo, nodo_actual)
    generar_transiciones_objetos(grafo, nodo_actual)

    for arista in grafo.obtener_vecinos(nodo_actual):
        if arista.nodo_destino not in frontera:
            frontera.append(arista.nodo_destino)

# Ejecutar búsqueda A*
camino_optimo = busqueda_a_estrella(grafo, nodo_inicial, nodo_objetivo)

# Mostrar resultados
if camino_optimo:
    print("Camino encontrado:")
    for paso in camino_optimo:
        print(f"Campeones: {paso.campeones}, Sinergias: {paso.sinergias}, Objetos: {paso.objetos}, Oro: {paso.oro}")
else:
    print("No se encontró un camino hacia la composición meta.")
