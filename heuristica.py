# heuristica.py

def heuristica(nodo_actual, nodo_objetivo):
    h1 = len(set(nodo_objetivo.campeones) - set(nodo_actual.campeones))
    h2 = len(set(nodo_objetivo.sinergias) - set(nodo_actual.sinergias))
    h3 = len(set(nodo_objetivo.objetos) - set(nodo_actual.objetos))

    return h1 + h2 + h3
