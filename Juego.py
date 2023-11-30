"""
@author: Christopher Oswaldo Márquez Reyes
@author: Valeria Marian Andrade Monreal
"""

import heapq
import sys
import time


# ---------------------------- Clases del código --------------------------------------------------------
class Mapa:
    def __init__(self, pos_actual):
        self.matriz = [[2, 5, 1, 7],
                       [13, 8, 11, 10],
                       [6, 9, 10, 8],
                       [12, 3, 1, 7]]
        self.pos_actual = pos_actual

    def calcular_min_costo(self, destino):
        m = len(self.matriz)
        n = len(self.matriz[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # derecha, izquierda, abajo, arriba

        dp[self.pos_actual[0]][self.pos_actual[1]] = self.matriz[self.pos_actual[0]][self.pos_actual[1]]
        heap = [(dp[self.pos_actual[0]][self.pos_actual[1]], self.pos_actual)]

        while heap:
            costo_actual, (i, j) = heapq.heappop(heap)

            if costo_actual != dp[i][j]:
                continue

            for dx, dy in movimientos:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    costo_nuevo = costo_actual + self.matriz[x][y]

                    if costo_nuevo < dp[x][y]:
                        dp[x][y] = costo_nuevo
                        heapq.heappush(heap, (costo_nuevo, (x, y)))

        min_costo = dp[destino[0]][destino[1]]
        return min_costo

    # Determinamos las coordenadas de cada lugar en el mapa
    def obtener_posicion_lugar(self, lugar):
        lugares = {
            'Lugar1': (3, 0),
            'Lugar2': (0, 1),
            'Lugar3': (0, 2),
            'Lugar4': (0, 3),
            'Lugar5': (1, 0),
            # Añade más lugares según sea necesario
        }
        return lugares.get(lugar)


# Inicializamos los atributos del personaje principal
class Player:
    def __init__(self, name='', hp=100, location=(0, 0), status_effects=None, items=None, money=0, bulletproof = False, gun = False, weapons = []):
        self.name = name
        self.weapons = weapons if weapons is not None else []
        self.bulletproof = bulletproof
        self.gun = gun
        self.hp = hp
        self.location = location
        self.status_effects = status_effects if status_effects is not None else []
        self.items = items if items is not None else []
        self.money = money
        self.mapa = Mapa(location)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    
    def get_weapons(self):
        for weapon in self.weapons:
            print(f"\n    - {weapon}\n")

    # Imprimimos la lista de items
    def get_items(self):
        return self.items

    # Agregamos un item al inventario
    def add_item(self, item):
        self.items.append(item)

    # Agregamos dinero al inventario
    def add_money(self, money):
        self.money += money

    # Actualizamos la posición del jugador en tiempo real
    def mover(self, nueva_posicion):
        self.location = nueva_posicion
        self.mapa.pos_actual = nueva_posicion


myPlayer = Player()


# Verificamos con qué compañero vamos a trabajar, ya que este nos ayudará en la historia más adelante
class Partner:
    def __init__(self, jose = False, marcus = False):
        self.jose = jose
        self.marcus = jose

    def partner_name(self):
        if self.jose is True:
            return 'Pepe'

        if self.marcus is True:
            return 'Marc'


myPartner = Partner()


# --------------------- Funciones del código -----------------------------------------------------
def check_items():
    print('\nAbriendo el inventario...\n')
    time.sleep(1)

    player_items = myPlayer.get_items()

    if not player_items:
        print('No tienes nada guardado en tu inventario.')
    else:
        print('Tienes los siguientes items:')
        for item in player_items:
            print(f'- {item}')

    time.sleep(1)


# Lista de acciones posibles del jugador para abarcar mayor margen
def actions():
    pass


def obtener_lista_frutas():
    return [
        "Manzana", "Plátano", "Naranja", "Fresa", "Uva", "Pera", "Kiwi", "Piña",
        "Mango", "Melón", "Sandía", "Cereza", "Ciruela", "Coco", "Granada", "Limón",
        "Papaya", "Higo", "Fruta de la Pasión", "Frambuesa", "Pomelo", "Mandarina",
        "Guayaba", "Castaña", "Níspero", "Arándano", "Lichi", "Membrillo", "Nectarina",
        "Tamarindo", "Carambola", "Chirimoya", "Caqui", "Mangostán", "Uchuva",
        "Rambután", "Physalis", "Grosella", "Feijoa", "Aguacate", "Albaricoque",
        "Arándano azul", "Arándano rojo", "Anona roja", "Almendra (fruto del almendro)",
        "Alquejenje", "Avellana (fruto seco del avellano)", "Aceituna", "Anona",
        "Árbol de pan", "Araza", "Acerola", "Badeas", "Breja", "Berenjena",
        "Babiaco", "Banana", "Bergamota", "Bala de cañón", "Caqui", "Castaña",
        "Chirimolla", "Corozo", "Caimito", "Cidra", "Cacao", "Copoazu", "Durazno",
        "Dátil", "Dragonfly", "Durian", "Damasco", "Escaramujo (mosqueta)",
        "Frutipan", "Fruta de la pasión", "Guanábana", "Achotillo", "Aguaje",
        "Arándano blanco", "Borojo", "Canela", "Ciruela verde", "Curuba", "Endrina",
        "Ensete", "Fresón", "Fruta de pan", "Granadilla", "Grosella espinosa",
        "Guama", "Guarana", "Jaca", "Lúcuma", "Mamey", "Nance", "Palo santo",
        "Papaturro", "Pepino dulce", "Pepino melón", "Pepino verde", "Pitanga",
        "Pitomba", "Pomarrosa", "Pouteria", "Salacca", "Sapodilla", "Tuna",
        "Uvilla", "Yaca", "Zapote", "Zarzamora"
    ]


# Lista de compañeros, puede no ser función y solo ser comentados
def partner():
    print("""
                                            PERFIL 1\n
                \n                Nombre: José Paredes Pacheco                            .......#@@@@#:......
                Alias: Pepe                                             .....-@@@@@@@@=.....
                Lugar de Nacimiento: Austin, Texas                      .....+@@@@@@@@+.....
                Edad: 33 años                                           .....:#@@@@@@%:.....
                Estatura: 1.71 cm                                       .......:*@@*:.......
                Peso: 70 kg                                             .....+@@@@@@@@+.....
                Color favorito: Blanco                                  ...-@@@@@@@@@@@@-...
                Perfil Profesional:                                     ..:@@@@@@@@@@@@@@-..
                    Academia de policía estatal de Texas:               ..#@@@@@@@@@@@@@@%..
                    Graduado con el promedio más bajo en su clase       .:@@@@@@@@@@@@@@@@-.
                    en 1985.                                            .=@@@@@@@@@@@@@@@@@=
                    Licenciatura en Justicia Criminal:                  Sin foto
                    Graduado en 1980.\n
                Datos extra:
                Alérgico a los gatos.
                Es bueno con el combate cuerpo a cuerpo.\n
                Casos resueltos:
                1 / 5

            """)

    print("""
                                        PERFIL 2\n
                \n                .......#@@@@#:......        Nombre: Marcus Davidson       
                .....-@@@@@@@@=.....        Alias: Marc
                .....+@@@@@@@@+.....        Lugar de Nacimiento: Arkansas
                .....:#@@@@@@%:.....        Edad: 41 años
                .......:*@@*:.......        Estatura: 1.67 cm
                .....+@@@@@@@@+.....        Peso: 80 kg
                ...-@@@@@@@@@@@@-...        Color favorito: No tiene
                ..:@@@@@@@@@@@@@@-..        Perfil Profesional:
                ..#@@@@@@@@@@@@@@%..            Criminología en Southern Arkansas University:
                .:@@@@@@@@@@@@@@@@-.            Graduado con promedio de 8.8 en 1961.
                .=@@@@@@@@@@@@@@@@=.            Ciencias forenses:
                Sin foto                        Graduado en 1968.\n
                                            Datos extra:
                                            Problemas estomacales.
                                            Pésimo en el trabajo en equipo.\n
                                            Casos resueltos:
                                            4/23
            
          """)


# Carta de la víctima
def letter():
    print("""
            )_-+\n
            He llegado a un punto en #& que no puedo ignorar el resentimiento que siento 
            hacia ti. Cada recuerdo de nuestra relación se ha vuelto tóxico, y quiero 
            expresar la profundidad de mi desprecio.\n

            Tus decisiones han dejado cicatrices en mi vida que van más allá de lo que puedes 
            entender. No sé si alguna vez te detuviste a pensar en las consecuencias de tus 
            acciones, o si simplemente no te importó. Pero necesito *( sepas que lo que 
            hiciste es algo que no puedo olvidar ni perdonar.\n

            Esta carta es ;:<>?/ acto de liberación personal. La verdad es que no hay espacio 
            en mi corazón para el perdón en este momento, solo te odio por lo que me has hecho 
            pasar.\n

            No deseo nada más que alejarme de ti y de todo lo que representas.\n

            Atte:,
            #&$%@!^*(          
          """)


# Expediente del asesinato
def criminal_file():
    print(   '\nN° Expediente:** 93932                                        Fecha: 17/11/1986'
             f'\n                                                              Hora: 06:35 a.m'
             f'\nLugar: Parque Nacional de Yosemite '
             f'\nDescripción del Caso:'
             f'\nMartín Arriaga Pérez, su cuerpo fue encontrado en una cabaña abandonada a 20 km'
             f'\nde la entrada principal del parque por un guardabosques luego de ver rastros de'
             f'\nuna fogata.\n'
             f'\nResultado de la autopsia: *Pendiente*'
             f'\nCausa de muerte: *Pendiente*'
             f'\nPosibles causas:'
             f'\nHipotermia.'
             f'\nSobredosis.'
             f'\nSuicidio.\n'
             f'\nInformación de la víctima:'
             f'\nNombre completo: Martín Arriaga Pérez'
             f'\nEdad: 23'
             f'\nLugar de Nacimiento: Caborca, Sonora'
             f'\nNacionalidad: Mexicana'
             f'\nSexo: Masculino'
             f'\nTipo de Sangre: O+'
             f'\nEstatura: 1.80'
             f'\nPeso: 84 kg'
             f'\nHistorial Médico: '
             f'\nProblemas con el tabaco, la bebida y abuso de sustancias.'
             f'\nProblemas de asma.\n'
             f'\nSospechosos: ??\n'
             f'\nEvidencia:'
             f'\n    1. Huellas: Se desconoce de quién.'
             f'\n    2. No se encontró el arma homicida.'
             f'\n    3. Hoja de papel: Se encontró una carta escrita a mano en el pantalón de la'
             f'\n       víctima. **La carta se encuentra en este mismo folder**'
             f'\n       Se desconoce si la carta la escribió la víctima.'
             f'\n'
             f'\n                               CONFIDENCIAL')


# Pantalla que maneja las opciones de inicio
def title_screen_selections():
    print('Selecciona una opción: ')
    option = input('\n> ')
    if option.lower() == 'jugar':
        time.sleep(1)
        start_game()
    elif option.lower() == 'ayuda':
        time.sleep(1)
        help_menu()
    elif option.lower() == 'salir':
        time.sleep(1)
        sys.exit()

    while option.lower() not in ['jugar', 'ayuda', 'salir']:
        print('\nSelecciona una opción válida: ')
        option = input('\n> ')
        if option.lower() == 'jugar':
            time.sleep(1)
            start_game()
        elif option.lower() == 'ayuda':
            time.sleep(1)
            help_menu()
        elif option.lower() == 'salir':
            time.sleep(1)
            sys.exit()


# Pantalla de inicio del juego
def title_screen():
    time.sleep(1)
    print('\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('''▄                                                                                                    ▄
▄                                                                                                    ▄
▄                          ███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗                          ▄
▄                          ██╔════╝████╗  ██║██║██╔════╝ ████╗ ████║██╔══██╗                         ▄
▄                          █████╗  ██╔██╗ ██║██║██║  ███╗██╔████╔██║███████║                         ▄
▄                          ██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║                         ▄
▄                          ███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║                         ▄
▄                          ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝                         ▄
▄                                                                                                    ▄
▄                                                                                                    ▄
▄                                         ▀▀█ █ █ █▀▀ █▀█ █▀▄                                        ▄
▄                                     ▄▄▄   █ █ █ █ █ █▀█ █▀▄ ▄▄▄                                    ▄
▄                                         ▀▀  ▀▀▀ ▀▀▀ ▀ ▀ ▀ ▀                                        ▄
▄                                                                                                    ▄
▄                                         █▀█ █ █ █ █ █▀▄ █▀█                                        ▄
▄                                     ▄▄▄ █▀█  █  █ █ █ █ █▀█ ▄▄▄                                    ▄
▄                                         ▀ ▀  ▀  ▀▀▀ ▀▀  ▀ ▀                                        ▄
▄                                                                                                    ▄
▄                                         █▀▀ █▀█ █   ▀█▀ █▀▄                                        ▄
▄                                     ▄▄▄ ▀▀█ █▀█ █    █  █▀▄ ▄▄▄                                    ▄
▄                                         ▀▀▀ ▀ ▀ ▀▀▀ ▀▀▀ ▀ ▀                                        ▄
▄                                                                                                    ▄''')
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n')
    title_screen_selections()
    print('\n')


# Menu de ayuda donde podrás entender como jugar
def help_menu():
    time.sleep(1)
    print('\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print(f'* * * * * * * * * * * * MENU DE AYUDA * * * * * * * * * * * * \n'
          f'Quizás tengas dudas acerca del juego asi que\n'
          f'esta es una guía rápida acerca de cómo jugar:\n'
          f'- Usa arriba, abajo, izquierda  y derecha para moverte.\n'
          f'- Usa "mirar" para inspeccionar.\n'
          f'- Hay eventos aleatorios alrededor del mapa, suerte.\n'
          f'- Escribe el comando a realizar.\n'
          f'- Puedes obtener items que te ayudaran en el juego\n'
          f'- Para checar tu inventario escribe "inventario"\n'
          f'- Para checar el mapa escribe "ver mapa"\n'
          f'- Si al jugar tienes dudas, escribe "ayuda"\n'
          f'- ¡Mucha suerte y diviértete!...')
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n')
    time.sleep(5)
    title_screen()

# Pantalla de final malo
def bad_ending():
    print('+----------------------------------------------------------------------------------------------------+')
    print('''                                                                     
                ██████╗  █████╗ ██████╗     ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝ 
                ██████╔╝███████║██║  ██║    █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗
                ██╔══██╗██╔══██║██║  ██║    ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║
                ██████╔╝██║  ██║██████╔╝    ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝
                ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝         \n''')

    print('¿DESEAS COMENZAR DE NUEVO (SI/NO)? ')
    option = input('\n> ')
    print('+----------------------------------------------------------------------------------------------------+\n')
    if option.lower() == 'si':
        time.sleep(1)
        prologo()
    elif option.lower() == 'no':
        time.sleep(1)
        sys.exit()
    while option.lower() not in ['yes', 'no']:
        print('Tienes que tomas una decisión...')
        time.sleep(1)
        print('¿DESEAS COMENZAR DE NUEVO (SI/NO)? ')
        option = input('\n> ')
        print('+----------------------------------------------------------------------------------------------------+\n')
        if option.lower() == 'si':
            time.sleep(1)
            prologo()
        elif option.lower() == 'no':
            time.sleep(1)
            sys.exit()

