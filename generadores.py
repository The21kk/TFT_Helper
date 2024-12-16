# generadores.py

from nodos import Nodo, Arista
from grafo import Grafo

# Definimos los objetos de la composición meta
objetos_disponibles = ["Blue Buff", "Rabadon's Deathcap", "Ionic Spark"]

def generar_transiciones_compra(grafo, nodo_actual, tienda_actual, debug=False):
    """
    Genera nodos y transiciones basados en la compra de campeones disponibles en la tienda actual.

    """
    if debug:
        print(f"\nGenerando transiciones de compra para el nodo actual: Campeones={nodo_actual.campeones}, Oro={nodo_actual.oro}")
        print(f"Tienda actual: {[campeon['nombre'] for campeon in tienda_actual]}")

    for campeon in tienda_actual:
        nombre_campeon = campeon["nombre"]
        coste_campeon = campeon["coste"]
        
        # Verificar si el campeón ya está en el equipo o si no hay suficiente oro
        if nombre_campeon not in nodo_actual.campeones and nodo_actual.oro >= coste_campeon:
            nuevo_oro = nodo_actual.oro - coste_campeon
            nuevo_nodo = Nodo(
                campeones=nodo_actual.campeones + [nombre_campeon],
                sinergias=nodo_actual.sinergias,  # Las sinergias se pueden calcular más adelante si es necesario
                objetos=nodo_actual.objetos,
                oro=nuevo_oro,
                salud=nodo_actual.salud,
                posicion=nodo_actual.posicion + [len(nodo_actual.campeones)]
            )
            arista = Arista(
                costo=coste_campeon,
                accion=f"comprar_{nombre_campeon}",
                nodo_destino=nuevo_nodo
            )
            grafo.agregar_arista(nodo_actual, arista)
            grafo.agregar_nodo(nuevo_nodo)
            if debug:
                print(f" -> Generado nodo acumulativo de compra: Campeones={nuevo_nodo.campeones}, Oro restante={nuevo_nodo.oro}")

def generar_transiciones_objetos(grafo, nodo_actual, debug=False):
    """
    Genera nodos y transiciones basados en la asignación de objetos.

    """
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

def expandir_nodo(grafo, nodo_actual, tienda_actual, debug=False):
    """
    Expande el nodo actual generando todas las transiciones de compra y asignación de objetos.
    
    """
    generar_transiciones_compra(grafo, nodo_actual, tienda_actual, debug)
    generar_transiciones_objetos(grafo, nodo_actual, debug)
