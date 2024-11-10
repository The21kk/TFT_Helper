# busqueda.py

import heapq
from heuristica import heuristica
from nodos import Nodo
from grafo import Grafo

def busqueda_a_estrella(grafo, nodo_inicial, nodo_objetivo):
    open_set = []
    heapq.heappush(open_set, (0, nodo_inicial))
    
    costo_acumulado = {nodo_inicial: 0}
    padres = {nodo_inicial: None}

    while open_set:
        _, nodo_actual = heapq.heappop(open_set)

        if nodo_actual == nodo_objetivo:
            return reconstruir_camino(padres, nodo_actual)

        for arista in grafo.obtener_vecinos(nodo_actual):
            nodo_vecino = arista.nodo_destino
            nuevo_costo = costo_acumulado[nodo_actual] + arista.costo

            if nodo_vecino not in costo_acumulado or nuevo_costo < costo_acumulado[nodo_vecino]:
                costo_acumulado[nodo_vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(nodo_vecino, nodo_objetivo)
                heapq.heappush(open_set, (prioridad, nodo_vecino))
                padres[nodo_vecino] = nodo_actual

    return None

def reconstruir_camino(padres, nodo_final):
    camino = []
    nodo = nodo_final
    while nodo:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()
    return camino
