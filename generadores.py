# generadores.py

from nodos import Nodo, Arista
from grafo import Grafo

# Definimos los campeones de la composición meta y sus costos
composicion_meta_campeones = ['Ahri', 'Rumble', 'Bard', 'Hecarim', 'Shen', 'Tahm Kench', 'Varus', 'Xerath']
costo_campeones = {
    'Ahri': 3, 'Rumble': 3, 'Bard': 5, 'Hecarim': 4, 'Shen': 2, 
    'Tahm Kench': 2, 'Varus': 3, 'Xerath': 4
}
# Definimos los objetos de la composición meta
objetos_disponibles = ["Blue Buff", "Rabadon's Deathcap", "Ionic Spark"]

def generar_transiciones_compra(grafo, nodo_actual, debug=False):
    if debug:
        print(f"\nGenerando transiciones de compra para el nodo actual: Campeones={nodo_actual.campeones}, Oro={nodo_actual.oro}")
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
                if debug:
                    print(f" -> Generado nodo acumulativo de compra: Campeones={nuevo_nodo.campeones}, Oro restante={nuevo_nodo.oro}")

def generar_transiciones_objetos(grafo, nodo_actual, debug=False):
    if debug:
        print(f"\nGenerando transiciones de asignación de objetos para el nodo actual: Objetos={nodo_actual.objetos}")
    for objeto in objetos_disponibles:
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
                costo=0,  # Asignar objetos no tiene costo
                accion=f"asignar_{objeto}",
                nodo_destino=nuevo_nodo
            )
            grafo.agregar_arista(nodo_actual, arista)
            grafo.agregar_nodo(nuevo_nodo)
            if debug:
                print(f" -> Generado nodo acumulativo de asignación de objeto: Objetos={nuevo_nodo.objetos}")

def expandir_nodo(grafo, nodo_actual, debug=False):
    """
    Expande el nodo actual generando todas las transiciones de compra y asignación de objetos.
    """
    generar_transiciones_compra(grafo, nodo_actual, debug)
    generar_transiciones_objetos(grafo, nodo_actual, debug)
