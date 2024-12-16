import numpy as np
import random 
campeones = [
    { "id": 1, "nombre": "Amumu", "coste": 1, "Origen": ["Automata"], "clase": ["Watcher"] },
  { "id": 2, "nombre": "Darius", "coste": 1, "Origen": ["Conqueror"], "clase": ["Watcher"] },
  { "id": 3, "nombre": "Draven", "coste": 1, "Origen": ["Conqueror"], "clase": ["Pit Fighter"] },
  { "id": 4, "nombre": "Irelia", "coste": 1, "Origen": ["Rebel"], "clase": ["Sentinel"] },
  { "id": 5, "nombre": "Lux", "coste": 1, "Origen": ["Academy"], "clase": ["Sorcerer"] },
  { "id": 6, "nombre": "Maddie", "coste": 1, "Origen": ["Enforcer"], "clase": ["Sniper"] },
  { "id": 7, "nombre": "Morgana", "coste": 1, "Origen": ["Black Rose"], "clase": ["Visionary"] },
  { "id": 8, "nombre": "Powder", "coste": 1, "Origen": ["Family","Scrap"], "clase": ["Ambusher"] },
  { "id": 9, "nombre": "Singed", "coste": 1, "Origen": ["ChemBaron"], "clase": ["Sentinel"] },
  { "id": 10, "nombre": "Steb", "coste": 1, "Origen": ["Enforcer"], "clase": ["Bruiser"] },
  { "id": 11, "nombre": "Trundle", "coste": 1, "Origen": ["Scrap"], "clase": ["Bruiser"] },
  { "id": 12, "nombre": "Vex", "coste": 1, "Origen": ["Rebel"], "clase": ["Visionary"] },
  { "id": 13, "nombre": "Violet", "coste": 1, "Origen": ["Family"], "clase": ["Pit Fighter"] },
  { "id": 14, "nombre": "Zyra", "coste": 1, "Origen": ["Experiment"], "clase": ["Sorcerer"] },
  { "id": 15, "nombre": "Akali", "coste": 2, "Origen": ["Rebel"], "clase": ["Quickstriker"] },
  { "id": 16, "nombre": "Camille", "coste": 2, "Origen": ["Enforcer"], "clase": ["Ambusher"] },
  { "id": 17, "nombre": "Leona", "coste": 2, "Origen": ["Academy"], "clase": ["Sentinel"] },
  { "id": 18, "nombre": "Nocturne", "coste": 2, "Origen": ["Automata"], "clase": ["Quickstriker"] },
  { "id": 19, "nombre": "Rell", "coste": 2, "Origen": ["Conqueror"], "clase": ["Sentinel","Visionary"] },
  { "id": 20, "nombre": "Renata", "coste": 2, "Origen": ["ChemBaron"], "clase": ["Visionary"] },
  { "id": 21, "nombre": "Sett", "coste": 2, "Origen": ["Rebel"], "clase": ["Bruiser"] },
  { "id": 22, "nombre": "Tristana", "coste": 2, "Origen": ["Emissary"], "clase": ["Artillerist"] },
  { "id": 23, "nombre": "Urgot", "coste": 2, "Origen": ["Experiment"], "clase": ["Artillerist","Pit Fighter"] },
  { "id": 24, "nombre": "Vander", "coste": 2, "Origen": ["Family"], "clase": ["Watcher"] },
  { "id": 25, "nombre": "Vladimir", "coste": 2, "Origen": ["Black Rose"], "clase": ["Sorcerer"] },
  { "id": 26, "nombre": "Zeri", "coste": 2, "Origen": ["Firelight"], "clase": ["Sniper"] },
  { "id": 27, "nombre": "Ziggs", "coste": 2, "Origen": ["Scrap"], "clase": ["Dominator"] },
  { "id": 28, "nombre": "Blitzcrank", "coste": 3, "Origen": ["Automata"], "clase": ["Dominator"] },
  { "id": 29, "nombre": "Cassiopeia", "coste": 3, "Origen": ["Black Rose"], "clase": ["Dominator"] },
  { "id": 30, "nombre": "Ezreal", "coste": 3, "Origen": ["Academy"], "clase": ["Artillerist"] },
  { "id": 31, "nombre": "Gangplank", "coste": 3, "Origen": ["Conqueror","Scrap"], "clase": ["Form Swapper"] },
  { "id": 32, "nombre": "Kogmaw", "coste": 3, "Origen": ["Automata"], "clase": ["Sniper"] },
  { "id": 33, "nombre": "Loris", "coste": 3, "Origen": ["Enforcer"], "clase": ["Sentinel"] },
  { "id": 34, "nombre": "Nami", "coste": 3, "Origen": ["Emissary"], "clase": ["Sorcerer"] },
  { "id": 35, "nombre": "Nunu", "coste": 3, "Origen": ["Experiment"], "clase": ["Bruiser"] },
  { "id": 36, "nombre": "Renni", "coste": 3, "Origen": ["ChemBaron"], "clase": ["Bruiser"] },
  { "id": 37, "nombre": "Scar", "coste": 3, "Origen": ["Firelight"], "clase": ["Watcher"] },
  { "id": 38, "nombre": "Smeech", "coste": 3, "Origen": ["ChemBaron"], "clase": ["Ambusher"] },
  { "id": 39, "nombre": "Swain", "coste": 3, "Origen": ["Conqueror"], "clase": ["Form Swapper","Sorcerer"] },
  { "id": 40, "nombre": "Twisted Fate", "coste": 3, "Origen": ["Enforcer"], "clase": ["Quickstriker"] },
  { "id": 41, "nombre": "Ambessa", "coste": 4, "Origen": ["Conqueror","Emissary"], "clase": ["Quickstriker"] },
  { "id": 42, "nombre": "Corki", "coste": 4, "Origen": ["Scrap"], "clase": ["Artillerist"] },
  { "id": 43, "nombre": "Dr Mundo", "coste": 4, "Origen": ["Experiment"], "clase": ["Dominator"] },
  { "id": 44, "nombre": "Ekko", "coste": 4, "Origen": ["Firelight","Scrap"], "clase": ["Ambusher"] },
  { "id": 45, "nombre": "Elise", "coste": 4, "Origen": ["Black Rose"], "clase": ["Bruiser","Form Swapper"] },
  { "id": 46, "nombre": "Garen", "coste": 4, "Origen": ["Emissary"], "clase": ["Watcher"] },
  { "id": 47, "nombre": "Heimerdinger", "coste": 4, "Origen": ["Academy"], "clase": ["Visionary"] },
  { "id": 48, "nombre": "Illaoi", "coste": 4, "Origen": ["Rebel"], "clase": ["Sentinel"] },
  { "id": 49, "nombre": "Silco", "coste": 4, "Origen": ["ChemBaron"], "clase": ["Dominator"] },
  { "id": 50, "nombre": "Twitch", "coste": 4, "Origen": ["Experiment"], "clase": ["Sniper"] },
  { "id": 51, "nombre": "Vi", "coste": 4, "Origen": ["Enforcer"], "clase": ["Pit Fighter"] },
  { "id": 52, "nombre": "Zoe", "coste": 4, "Origen": ["Rebel"], "clase": ["Sorcerer"] },
  { "id": 53, "nombre": "Caitlyn", "coste": 5, "Origen": ["Enforcer"], "clase": ["Sniper"] },
  { "id": 54, "nombre": "Jayce", "coste": 5, "Origen": ["Academy"], "clase": ["Form Swapper"] },
  { "id": 55, "nombre": "Jinx", "coste": 5, "Origen": ["Rebel"], "clase": ["Ambusher"] },
  { "id": 56, "nombre": "Leblanc", "coste": 5, "Origen": ["Black Rose"], "clase": ["Sorcerer"] },
  { "id": 57, "nombre": "Malzahar", "coste": 5, "Origen": ["Automata"], "clase": ["Visionary"] },
  { "id": 58, "nombre": "Mordekaiser", "coste": 5, "Origen": ["Conqueror"], "clase": ["Dominator"] },
  { "id": 59, "nombre": "Rumble", "coste": 5, "Origen": ["Junker King","Scrap"], "clase": ["Sentinel"] },
  { "id": 60, "nombre": "Sevika", "coste": 5, "Origen": ["ChemBaron","High Roller"], "clase": ["Pit Fighter"] } ]

pool = []
for campeon in campeones:
    if campeon["coste"] == 1:
        pool.append(22)
    elif campeon["coste"] == 2:
        pool.append(20)
    elif campeon["coste"] == 3:
        pool.append(17)
    elif campeon["coste"] == 4:
        pool.append(10)
    elif campeon["coste"] == 5:
        pool.append(9)

print(pool)
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

pooljugador1=[]
pooljugador2=[]
pooljugador3=[]
pooljugador4=[]
pooljugador5=[]
pooljugador6=[]
pooljugador7=[]
pooljugador8=[]

exp_jugadores = np.array([0,0,0,0,0,0,0,0])  # Experiencia actual de cada jugador
niveles_jugadores = np.array([1, 1, 1, 1, 1, 1, 1, 1])  # Nivel actual de cada jugador
oro_jugadores = np.array([0,0,0,0,0,0,0,0])
aumentooro=2
ronda=1
fase=["1-1","1-2","1-3","1-4","2-1","2-2","2-3","2-4","2-5","2-6","2-7","3-1","3-2","3-3","3-4","3-5","3-6","3-7","4-1","4-2","4-3","4-4","4-5","4-6","4-7"
      ,"5-1","5-2","5-3","5-4","5-5","5-6","5-7","6-1","6-2","6-3","6-4","6-5","6-6","6-7"]

exp=[2,4,6,10,20,40,76,124,196,280]





###################### GENERA 5 CAMPEONES EN LA TIENDA################################

def generar_tienda(campeones, nivel_jugador, probabilidades_tienda):
    """
    Genera una tienda de 5 campeones según el nivel del jugador y las probabilidades asociadas.

    :param campeones: Lista de campeones disponibles.
    :param nivel_jugador: Nivel del jugador (1-10).
    :param probabilidades_tienda: Diccionario de probabilidades según el nivel.
    :return: Lista con 5 campeones seleccionados.
    """
    # Obtener las probabilidades según el nivel del jugador
    probabilidades = probabilidades_tienda.get(nivel_jugador, [100, 0, 0, 0, 0])

    # Crear una lista donde cada coste aparece según su probabilidad
    costes = []
    for coste, probabilidad in enumerate(probabilidades, start=1):
        costes.extend([coste] * probabilidad)

    # Generar la tienda seleccionando campeones basados en los costes
    tienda = []
    for _ in range(5):
        coste_seleccionado = random.choice(costes)  # Seleccionar un coste basado en las probabilidades
        candidatos = [c for c in campeones if c["coste"] == coste_seleccionado]
        if candidatos:
            tienda.append(random.choice(candidatos))

    return tienda






############################ REVISA Y ACTUALIZA LOS NIVELES CADA RONDA##########################################


def actualizar_niveles(exp_jugadores, niveles_jugadores, exp_requerida):
  # print(len(exp_jugadores))
  for i in range(len(exp_jugadores)):
      # print("iteracion",i)
      # print("experiencia jugador",exp_jugadores[i])
      # print("exp requerida",exp_requerida[niveles_jugadores[i]-1])
      if exp_jugadores[i] >= exp_requerida[niveles_jugadores[i]]:
          # print("ESTOY AQUI PARA EL JUGADOR", i)
          niveles_jugadores[i] += 1
  return niveles_jugadores








while True:  # Ciclo infinito
    if ronda==5:
      aumentooro+=1
    if ronda==12:
      aumentooro+=1
    if ronda==19:
      aumentooro+=1
    if ronda==26:
      aumentooro+=1
    if ronda==33:
      aumentooro+=1
    if ronda==40:
      aumentooro+=1

      
#### FALTA HACER QUE JUGADORES COMPREN CAMPEONES (MENU PARA EL JUGADOR, RANDOM PARA LOS OTROS Y VER SI EL COSTE ES SUFICIENTE)
#### FALTA VER VALORACION DE CAMPEONES, INTENTAR HACER ALGUNA LOGICA DE COMPRA DE OTROS JUGADORES
#### FALTA HACER TABLERO



    print("\n=== TIENDA ===")
    print("Acción personalizada: Puedes agregar lógica aquí.\n")
    oro_jugadores=oro_jugadores+aumentooro
    exp_jugadores=exp_jugadores+2
    print("exp actual jugadores:", exp_jugadores)

    # Sección 1: Acciones personalizables
    # Aquí puedes escribir acciones específicas que ocurran en cada fase.
    # Por ejemplo, aumentar el inventario automáticamente, descuentos, etc.
    # --- Personaliza esta sección ---
    actualizar_niveles(exp_jugadores,niveles_jugadores,exp)
    tienda = generar_tienda(campeones, niveles_jugadores[0], probabilidades_tienda=probabilidades_tienda)
    for campeon in tienda:
        print(campeon)

    opcion = input("Selecciona una opción: ")
    # # Sección 2: Datos desplegados
    # print("Nivel actual jugador:", niveles_jugadores[0])
    # print("Campeones obtenidos:")
    # # for producto, cantidad in inventario.items():
    # #     print(f"- {producto.capitalize()}: {cantidad} unidades (Precio: ${precios[producto]})")
    # # print()
    # # Sección 3: Menú de opciones
    # print("MENÚ:")
    # print("(1, 2, 3, 4 o 5). Comprar campeon seleccionado")
    # print("6. Para vender campeones")
    # print("7. Comprar experiencia")

    # opcion = input("Selecciona una opción: ")

    # if opcion == "1":
    #     # Comprar producto
    #     producto = input("¿Qué producto deseas comprar? ").lower()
    #     if producto in precios:
    #         cantidad = int(input(f"¿Cuántas unidades de {producto} deseas comprar? "))
    #         costo = cantidad * precios[producto]
    #         if saldo >= costo:
    #             saldo -= costo
    #             inventario[producto] += cantidad
    #             print(f"Has comprado {cantidad} unidades de {producto}.")
    #         else:
    #             print("No tienes suficiente saldo.")
    #     else:
    #         print("Producto no disponible.")

    # elif opcion == "2":
    #     # Vender producto
    #     producto = input("¿Qué producto deseas vender? ").lower()
    #     if producto in inventario:
    #         cantidad = int(input(f"¿Cuántas unidades de {producto} deseas vender? "))
    #         if inventario[producto] >= cantidad:
    #             ganancia = cantidad * precios[producto]
    #             saldo += ganancia
    #             inventario[producto] -= cantidad
    #             print(f"Has vendido {cantidad} unidades de {producto}.")
    #         else:
    #             print("No tienes suficientes unidades para vender.")
    #     else:
    #         print("Producto no disponible.")

    # elif opcion == "3":
    #     # Salir del ciclo infinito
    #     print("Gracias por visitar la tienda. ¡Hasta luego!")
    #     break

    # else:
    #     print("Opción no válida. Intenta nuevamente.")






