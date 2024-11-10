# grafo.py

from nodos import Nodo, Arista

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = []

    def agregar_arista(self, nodo_origen, arista):
        if nodo_origen in self.nodos:
            self.nodos[nodo_origen].append(arista)

    def obtener_vecinos(self, nodo):
        return self.nodos.get(nodo, [])
