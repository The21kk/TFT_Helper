# busqueda.py

import heapq
from heuristica import heuristica
from generadores import expandir_nodo

def busqueda_a_estrella(grafo, nodo_inicial, nodo_objetivo, debug=False):
    open_set = []
    heapq.heappush(open_set, (0, nodo_inicial))
    
    costo_acumulado = {nodo_inicial: 0}
    padres = {nodo_inicial: None}

    if debug:
        print("\nIniciando búsqueda A* desde el nodo inicial:")
        print(f"Nodo inicial: Campeones={nodo_inicial.campeones}, Objetos={nodo_inicial.objetos}, Oro={nodo_inicial.oro}")

    while open_set:
        _, nodo_actual = heapq.heappop(open_set)

        if debug:
            print(f"\nExplorando nodo: Campeones={nodo_actual.campeones}, Objetos={nodo_actual.objetos}, Oro={nodo_actual.oro}")

        # Nueva condición de finalización: solo se requiere que los campeones coincidan
        if set(nodo_actual.campeones) == set(nodo_objetivo.campeones):
            if debug:
                print("\n¡Objetivo alcanzado solo con campeones! Reconstruyendo el camino.")
            return reconstruir_camino(padres, nodo_actual)

        # Expande el nodo actual
        expandir_nodo(grafo, nodo_actual, debug)

        # Expande cada nodo vecino
        for arista in grafo.obtener_vecinos(nodo_actual):
            nodo_vecino = arista.nodo_destino
            nuevo_costo = costo_acumulado[nodo_actual] + arista.costo

            if nodo_vecino not in costo_acumulado or nuevo_costo < costo_acumulado[nodo_vecino]:
                costo_acumulado[nodo_vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(nodo_vecino, nodo_objetivo)
                heapq.heappush(open_set, (prioridad, nodo_vecino))
                padres[nodo_vecino] = nodo_actual
                if debug:
                    print(f"  -> Añadido a la cola de prioridad: Campeones={nodo_vecino.campeones}, Objetos={nodo_vecino.objetos}, Prioridad={prioridad}")

    if debug:
        print("No se encontró un camino hacia la composición meta de campeones.")
    return None

def reconstruir_camino(padres, nodo_final):
    camino = []
    nodo = nodo_final
    while nodo:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()
    return camino
