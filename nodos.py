# nodos.py

class Nodo:
    def __init__(self, campeones, sinergias, objetos, oro, salud, posicion):
        self.campeones = campeones
        self.sinergias = sinergias
        self.objetos = objetos
        self.oro = oro
        self.salud = salud
        self.posicion = posicion

    def __hash__(self):
        return hash((tuple(self.campeones), tuple(self.sinergias), tuple(self.objetos), self.oro, self.salud, tuple(self.posicion)))

    def __eq__(self, other):
        return (self.campeones, self.sinergias, self.objetos, self.oro, self.salud, self.posicion) == \
               (other.campeones, other.sinergias, other.objetos, other.oro, other.salud, other.posicion)

    def __lt__(self, other):
        # Ordenar primero por el número de campeones y luego por el oro (esto es una sugerencia y se puede ajustar)
        return (len(self.campeones), self.oro) < (len(other.campeones), other.oro)

class Arista:
    def __init__(self, costo, accion, nodo_destino):
        self.costo = costo
        self.accion = accion
        self.nodo_destino = nodo_destino
