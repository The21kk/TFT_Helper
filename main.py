# main.py

from nodos import Nodo
from grafo import Grafo
from busqueda import busqueda_a_estrella

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

# Ejecutar búsqueda A* con opción de depuración activada o desactivada
debug_mode = True  # Cambia a True para activar la depuración
camino_optimo = busqueda_a_estrella(grafo, nodo_inicial, nodo_objetivo, debug=debug_mode)

# Mostrar resultados
if camino_optimo:
    print("Camino encontrado hacia la composición meta.")
else:
    print("No se encontró un camino hacia la composición meta.")
