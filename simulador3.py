import random

# Definición de campeones y otros elementos (como en el código anterior)
campeones_coste_1 = [
    {"id": 1, "nombre": "Ashe"}, {"id": 2, "nombre": "Blitzcrank"}, {"id": 3, "nombre": "Elise"},
    {"id": 4, "nombre": "Jax"}, {"id": 5, "nombre": "Jayce"}, {"id": 6, "nombre": "Lillia"},
    {"id": 7, "nombre": "Nomsy"}, {"id": 8, "nombre": "Poppy"}, {"id": 9, "nombre": "Seraphine"},
    {"id": 10, "nombre": "Soraka"}, {"id": 11, "nombre": "Twitch"}, {"id": 12, "nombre": "Warwick"},
    {"id": 13, "nombre": "Ziggs"}, {"id": 14, "nombre": "Zoe"}
]
campeones_coste_2 = [
    {"id": 15, "nombre": "Ahri"}, {"id": 16, "nombre": "Akali"}, {"id": 17, "nombre": "Cassiopeia"},
    {"id": 18, "nombre": "Galio"}, {"id": 19, "nombre": "Kassadin"}, {"id": 20, "nombre": "KogMaw"},
    {"id": 21, "nombre": "Nilah"}, {"id": 22, "nombre": "Nunu"}, {"id": 23, "nombre": "Rumble"},
    {"id": 24, "nombre": "Shyvana"}, {"id": 25, "nombre": "Syndra"}, {"id": 26, "nombre": "Tristana"}
]
campeones_coste_3 = [
    {"id": 27, "nombre": "Bard"}, {"id": 28, "nombre": "Ezreal"}, {"id": 29, "nombre": "Hecarim"},
    {"id": 30, "nombre": "Hwei"}, {"id": 31, "nombre": "Jinx"}, {"id": 32, "nombre": "Katarina"},
    {"id": 33, "nombre": "Mordekaiser"}, {"id": 34, "nombre": "Neeko"}, {"id": 35, "nombre": "Shen"},
    {"id": 36, "nombre": "Swain"}, {"id": 37, "nombre": "Veigar"}, {"id": 38, "nombre": "Vex"},
    {"id": 39, "nombre": "Wukong"}
]
campeones_coste_4 = [
    {"id": 40, "nombre": "Fiora"}, {"id": 41, "nombre": "Gwen"}, {"id": 42, "nombre": "Kalista"},
    {"id": 43, "nombre": "Karma"}, {"id": 44, "nombre": "Nami"}, {"id": 45, "nombre": "Nasus"},
    {"id": 46, "nombre": "Olaf"}, {"id": 47, "nombre": "Rakan"}, {"id": 48, "nombre": "Ryze"},
    {"id": 49, "nombre": "Tahm Kench"}, {"id": 50, "nombre": "Taric"}, {"id": 51, "nombre": "Varus"}
]
campeones_coste_5 = [
    {"id": 52, "nombre": "Briar"}, {"id": 53, "nombre": "Camille"}, {"id": 54, "nombre": "Diana"},
    {"id": 55, "nombre": "Milio"}, {"id": 56, "nombre": "Morgana"}, {"id": 57, "nombre": "Norra & Yuumi"},
    {"id": 58, "nombre": "Smolder"}, {"id": 59, "nombre": "Xerath"}
]

# Lista completa de campeones
todos_los_campeones = campeones_coste_1 + campeones_coste_2 + campeones_coste_3 + campeones_coste_4 + campeones_coste_5

# Probabilidades para las tiendas dependiendo del nivel
probabilidades_tienda = {
    1: [100, 0, 0, 0, 0],
    2: [75, 25, 0, 0, 0],
    3: [55, 30, 15, 0, 0],
    4: [45, 33, 20, 2, 0],
    5: [30, 40, 25, 5, 0],
    6: [19, 30, 40, 10, 1],
    7: [18, 25, 32, 22, 3],
    8: [15, 20, 25, 30, 10],
    9: [5, 10, 20, 40, 25],
    10: [1, 2, 12, 50, 35]
}
clases = [
    {
        "id": 1,
        "nombre": "Ascendant",
        "campeones": [59]
    },
    {
        "id": 2,
        "nombre": "Bastion",
        "campeones": [54, 29, 6, 22, 8, 35, 50]
    },
    {
        "id": 3,
        "nombre": "Bat Queen",
        "campeones": [56]
    },
    {
        "id": 4,
        "nombre": "Blaster",
        "campeones": [28, 30, 23, 58, 26, 51]
    },
    {
        "id": 5,
        "nombre": "Explorer",
        "campeones": [57]
    },
    {
        "id": 6,
        "nombre": "Hunter",
        "campeones": [31, 20, 7, 46, 11]
    },
    {
        "id": 7,
        "nombre": "Incantor",
        "campeones": [17, 43, 25, 13]
    },
    {
        "id": 8,
        "nombre": "Mage",
        "campeones": [18, 44, 57, 9, 10, 37, 38]
    },
    {
        "id": 9,
        "nombre": "Multistriker",
        "campeones": [16, 42, 4, 29, 53, 19]
    },
    {
        "id": 10,
        "nombre": "Preserver",
        "campeones": [27, 56, 47, 55]
    },
    {
        "id": 11,
        "nombre": "Scholar",
        "campeones": [15, 27, 55, 48, 14]
    },
    {
        "id": 12,
        "nombre": "Shapeshifter",
        "campeones": [52, 3, 5, 45, 34, 24, 36]
    },
    {
        "id": 13,
        "nombre": "Vanguard",
        "campeones": [2, 18, 33, 23, 49, 12]
    },
    {
        "id": 14,
        "nombre": "Warrior",
        "campeones": [16, 40, 41, 32, 21]
    }
]


origenes = [
    {
        "id": 1,
        "nombre": "Arcana",
        "campeones": [15, 29, 49, 59]
    },
    {
        "id": 2,
        "nombre": "Chrono",
        "campeones": [4, 16, 34, 25, 18]
    },
    {
        "id": 3,
        "nombre": "Dragon",
        "campeones": [7, 24, 58]
    },
    {
        "id": 4,
        "nombre": "Druid",
        "campeones": [39]
    },
    {
        "id": 5,
        "nombre": "Eldritch",
        "campeones": [1, 6, 17, 33, 44, 11, 14]
    },
    {
        "id": 6,
        "nombre": "Faerie",
        "campeones": [27, 32, 6, 53, 47, 25, 26]
    },
    {
        "id": 7,
        "nombre": "Frost",
        "campeones": [30, 54, 46, 36, 11, 12, 18]
    },
    {
        "id": 8,
        "nombre": "Honeymancy",
        "campeones": [2, 20, 22, 23, 13]
    },
    {
        "id": 9,
        "nombre": "Portal",
        "campeones": [28, 18, 19, 20, 33, 50, 48, 14]
    },
    {
        "id": 10,
        "nombre": "Pyro",
        "campeones": [16, 45, 36, 51]
    },
    {
        "id": 11,
        "nombre": "Ravenous",
        "campeones": [52]
    },
    {
        "id": 12,
        "nombre": "Sugarcraft",
        "campeones": [27, 41, 31, 23, 10]
    },
    {
        "id": 13,
        "nombre": "Witchcraft",
        "campeones": [17, 40, 56, 34, 47, 48]
    }
]
valor_compo = [1] * 60  # Asumiendo que tenemos un total de 60 campeones (ids 1-59)

# Asignamos valores de base según el coste de los campeones
for campeon in campeones_coste_1:
    valor_compo[campeon["id"] - 1] = 1  # Costo 1
for campeon in campeones_coste_2:
    valor_compo[campeon["id"] - 1] = 2  # Costo 2
for campeon in campeones_coste_3:
    valor_compo[campeon["id"] - 1] = 3  # Costo 3
for campeon in campeones_coste_4:
    valor_compo[campeon["id"] - 1] = 4  # Costo 4
for campeon in campeones_coste_5:
    valor_compo[campeon["id"] - 1] = 5  # Costo 5

# Aumentamos el valor para los campeones de la clase Bastion
bastion_ids = clases[1]["campeones"]  # IDs de los campeones de la clase Bastion
for bastion_id in bastion_ids:
    valor_compo[bastion_id - 1] += 7  # Aumentamos 7 puntos

# Buscamos otras clases y orígenes que contengan los campeones de Bastion y les agregamos 3 puntos
for clase in clases:
    for campeon_id in clase["campeones"]:
        if campeon_id in bastion_ids:
            continue  # Evitamos duplicar el aumento de +3 si ya se le sumaron +7
        valor_compo[campeon_id - 1] += 3  # Aumentamos 3 puntos a campeones con esos IDs

# Ahora tenemos el arreglo valor_compo actualizado con los valores de cada campeón
print(valor_compo)
# Función para obtener los campeones disponibles en la tienda (ahora con 5 campeones)
import random

# Campeones y tienda definidos como antes
# (Definición de campeones y probabilidades_tienda aquí)

# Función para obtener campeones disponibles en la tienda
def tienda_para_jugador(nivel):
    probabilidades = probabilidades_tienda[nivel]
    opciones = []
    campeones_disponibles = []
    
    for coste, probabilidad in enumerate(probabilidades):
        campeones_de_coste = []
        if coste == 0:
            campeones_de_coste = campeones_coste_1
        elif coste == 1:
            campeones_de_coste = campeones_coste_2
        elif coste == 2:
            campeones_de_coste = campeones_coste_3
        elif coste == 3:
            campeones_de_coste = campeones_coste_4
        elif coste == 4:
            campeones_de_coste = campeones_coste_5
        
        for _ in range(probabilidad):
            campeon = random.choice(campeones_de_coste)
            campeones_disponibles.append(campeon)
    
    while len(opciones) < 5:
        campeon = random.choice(campeones_disponibles)
        if campeon not in opciones:
            opciones.append(campeon)
    
    return opciones

class Fase:
    def __init__(self):
        self.numero_fase = 1
        self.etapa = 1
    
    def avanzar(self):
        if self.numero_fase == 7 and self.etapa == 1:
            print("Has alcanzado la fase final 7-1.")
            return False  # Indica que el juego debería detenerse
        elif self.etapa < 7:
            self.etapa += 1
        else:
            self.numero_fase += 1
            self.etapa = 1
        return True  # Indica que el juego continúa

    def obtener_fase_actual(self):
        return f"{self.numero_fase}-{self.etapa}"

# Clase Jugador actualizada para ganar oro basado en la fase
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.oro = 10
        self.nivel = 1
        self.experiencia = 0
        self.campeones = []

    def ganar_oro(self, etapa):
        oro_ganado = etapa + 2
        if self.oro >= 10:
            oro_extra = (self.oro - 10) // 10
            oro_ganado += oro_extra
        self.oro += oro_ganado

    def ganar_experiencia(self, puntos=4):
        self.experiencia += puntos
        if self.experiencia >= 10:
            self.subir_nivel()

    def subir_nivel(self):
        niveles = [0, 2, 8, 18, 38, 74, 122, 194, 278]
        for nivel, experiencia_requerida in enumerate(niveles):
            if self.experiencia >= experiencia_requerida:
                self.nivel = nivel + 1

    def comprar_campeon(self, campeon):
        coste = 1 if campeon in campeones_coste_1 else (2 if campeon in campeones_coste_2 else (3 if campeon in campeones_coste_3 else (4 if campeon in campeones_coste_4 else 5)))
        if self.oro >= coste:
            self.campeones.append(campeon)
            self.oro -= coste
            return True
        return False

    def comprar_experiencia(self):
        if self.oro >= 4:
            self.oro -= 4
            self.ganar_experiencia()
            return True
        return False

    def actualizar_tienda(self):
        if self.oro >= 2:
            self.oro -= 2
            return True
        return False

# Función del turno de juego con avance de fase hasta 7-1
def interfaz_turno(jugador):
    fase = Fase()
    
    while True:
        print(f"\n--- Turno para {jugador.nombre} ---")
        print(f"Fase: {fase.obtener_fase_actual()} | Nivel: {jugador.nivel} | Oro: {jugador.oro} | Experiencia: {jugador.experiencia}")
        print("Tus campeones:", [campeon['nombre'] for campeon in jugador.campeones])

        # Generar y mostrar la tienda
        tienda = tienda_para_jugador(jugador.nivel)
        print("\nTienda actual:")
        for i, campeon in enumerate(tienda, 1):
            print(f"{i}. {campeon['nombre']} (Costo: {1 if campeon in campeones_coste_1 else (2 if campeon in campeones_coste_2 else (3 if campeon in campeones_coste_3 else (4 if campeon in campeones_coste_4 else 5)))} oro) Valor de Composicion { valor_compo[campeon["id"]-1]}")

        # Opciones de juego
        print("\nOpciones:")
        print("1. Comprar un campeón (escribe el número del campeón)")
        print("2. Comprar 4 de experiencia por 4 de oro")
        print("3. Actualizar la tienda por 2 de oro")
        print("4. Ver Tablero de otros jugadores")
        print("5. Terminar turno")

        opcion = input("\nElige una opción: ")
        if opcion == "1":
            try:
                idx = int(input("Escribe el número del campeón para comprar: ")) - 1
                campeon_seleccionado = tienda[idx]
                if jugador.comprar_campeon(campeon_seleccionado):
                    print(f"Has comprado a {campeon_seleccionado['nombre']}")
                else:
                    print("No tienes suficiente oro.")
            except (IndexError, ValueError):
                print("Opción inválida.")
        elif opcion == "2":
            if jugador.comprar_experiencia():
                print("Has comprado 4 de experiencia.")
            else:
                print("No tienes suficiente oro para comprar experiencia.")
        elif opcion == "3":
            if jugador.actualizar_tienda():
                print("La tienda ha sido actualizada.")
            else:
                print("No tienes suficiente oro para actualizar la tienda.")
        elif opcion == "4":
            print("Turno terminado.")
            jugador.ganar_oro(fase.etapa)
            jugador.ganar_experiencia(2)
            if not fase.avanzar():
                print("¡El juego ha terminado en la fase 7-1!")
                break
        elif opcion == "5":
            print("Turno terminado.")
            jugador.ganar_oro(fase.etapa)
            jugador.ganar_experiencia(2)
            if not fase.avanzar():
                print("¡El juego ha terminado en la fase 7-1!")
                break
        else:
            print("Opción inválida.")

# Crear un jugador de ejemplo y ejecutar la interfaz de turno
jugador1 = Jugador("Jugador 1")
interfaz_turno(jugador1)