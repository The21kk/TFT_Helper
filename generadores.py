# generadores.py

from nodos import Nodo, Arista
from grafo import Grafo

# Campeones y costos
composicion_meta_campeones = ['Ahri', 'Rumble', 'Bard', 'Hecarim', 'Shen', 'Tahm Kench', 'Varus', 'Xerath']
composicion_meta_objetos = ['Blue Buff', "Rabadon's Deathcap", 'Ionic Spark']
costo_campeones = {'Ahri': 3, 'Rumble': 3, 'Bard': 5, 'Hecarim': 4, 'Shen': 2, 'Tahm Kench': 2, 'Varus': 3, 'Xerath': 4}

def generar_transiciones_compra(grafo, nodo_actual):
    for campeon in composicion_meta_campeones:
        if campeon not in nodo_actual.campeones:
            nuevo_oro = nodo_actual.oro - costo_campeones[campeon]
            if nuevo_oro >= 0:
                nuevo_nodo = Nodo(
                    campeones=nodo_actual.campeones + [campeon],
                    sinergias=nodo_actual.sinergias,
                    objetos=nodo_actual.objetos,
                    oro=nuevo_oro,
                    salud=nodo_actual.salud,
                    posicion=nodo_actual.posicion + [len(nodo_actual.campeones)]
                )
                arista = Arista(
                    costo=costo_campeones[campeon],
                    accion=f"comprar_{campeon}",
                    nodo_destino=nuevo_nodo
                )
                grafo.agregar_arista(nodo_actual, arista)
                grafo.agregar_nodo(nuevo_nodo)

def generar_transiciones_objetos(grafo, nodo_actual):
    for objeto in composicion_meta_objetos:
        if objeto not in nodo_actual.objetos:
            nuevo_nodo = Nodo(
                campeones=nodo_actual.campeones,
                sinergias=nodo_actual.sinergias,
                objetos=nodo_actual.objetos + [objeto],
                oro=nodo_actual.oro,
                salud=nodo_actual.salud,
                posicion=nodo_actual.posicion
            )
            arista = Arista(
                costo=0,
                accion=f"asignar_{objeto}",
                nodo_destino=nuevo_nodo
            )
            grafo.agregar_arista(nodo_actual, arista)
            grafo.agregar_nodo(nuevo_nodo)
