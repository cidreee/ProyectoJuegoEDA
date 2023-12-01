"""
@author: Christopher Oswaldo Márquez Reyes
@author: Valeria Marian Andrade Monreal
"""

import sys
import time


# ---------------------------- Clases del código --------------------------------------------------------

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

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    
    def get_weapons(self):
        if len(self.weapons) == 1:
            print(f'\n        Tomar tu {self.weapons[0]}.\n')
        else:
            print(f'\n        Tomar tu {self.weapons[0]}.\n'
                  f'          Tomar tu {self.weapons[1]}.\n')
            
                
    # Imprimimos la lista de items
    def get_items(self):
        return self.items

    # Agregamos un item al inventario
    def add_item(self, item):
        self.items.append(item)

    # Agregamos dinero al inventario
    def add_money(self, money):
        self.money += money

myPlayer = Player()


# Verificamos con qué compañero vamos a trabajar, ya que este nos ayudará en la historia más adelante
class Partner:
    def __init__(self, jose = False, marcus = False):
        self.jose = jose
        self.marcus = marcus

    def partner_name(self):
        if self.jose is True:
            return 'José'

        if self.marcus is True:
            return 'Marcus'


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
                Tipo de sangre: O+                                      ...-@@@@@@@@@@@@-...
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
                ...-@@@@@@@@@@@@-...        Tipo de sangre: AB-
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
            hacia ti.\n

            Tus decisiones han dejado cicatrices en mi vida que van más allá de lo que puedes 
            entender. No sé si alguna vez te detuviste a pensar en las consecuencias de tus 
            acciones, o si simplemente no te importó. Pero necesito *( sepas que lo que 
            hiciste es algo que no puedo olvidar ni perdonar.\n

            Esta carta es ;:<>?/ acto de liberación personal. La verdad, solo te odio por lo que me 
            has hecho pasar.\n

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

def cabin_map():
    print("""\n

                    ,----------------------------------------------------.-----.    
                    |                                    |                     |    
                    |    			         |                     |    
                    |                                    |                     |    
                    |             Sala                   |       Cocina        |    
                    |                                    |                     |    
                    |                                    |                     |    
                    |                                    |                     |    
                    |         ,----------"         ------:-----                |    
                    |         |                                                |    
                    |---------:    		                               |    
                    |    |                                  ,------------------:              
                    |    |.    ----------------.                               |    
                    |    |                     |                               |    
                    :----'                     |            |                  |  	
                    |                          |            ---:    Baño       |    
                    |         Cuarto         `-|               |               |    
                    |                          .---            |               |    
                    |                              |           |               |    
                    |                              |           |               |    
                    `------------------------------¨           `---------------'
         \n """)

def cabin_bath():
    print("""  
                                                 _______________________________________________________________________________ 
                                                |                                                                               | 
            |   |   |   |   |                   |                                                                               | 
            |   |___|   |   |                   |           _____________________________                                       | 
            |___|   |___|   |                   |          |  _________________________  |                                      |
            |   |   |   |   |                   |          |O|                         |O|                                      |
     /| |___|___|___|___|___| _________         |   /_\    | | //                      | |                   /_\                | 
       .| |/|   |   |   |   |   |               |%  =|=  % |O|                         |O|                   =|=                | 
      / | / |___|___|___|___|                   |          | |    //                   | |                                      |  
    .'| |/|/|   |   |   |   |       |           |          | |    //                   | |                                      | 
   /| |,| / |___|___|___|___|   |               |          |O|                         |O|                                      | 
  / | / |/|.' __________________ `.             |==========| |                         | |======================================| 
 /| |'| / |'.'_.-------------._`.`.             |          |O|                         |O|                                      | 
| |/| |'|.'/.'  .           .  `.\`.            |          | | //                      | |              ________________        | 
| / |/| / //                     \\\_\_          |          |O|_________________________|O|             |________________|       | 
|/| / |/ //                       |   \         |          |_____________________________|               |            |         | 
| |/| / //                        \  __\        |           ______________/;____________                 |~           |  =====  | 
| / |/ //                          \|\ \        |         /`        .--T--|--T--.       `\               |            |         | 
|/| / /_                              \ \       |        /_________'------'------'________\              |__%______%__|         | 
| |/ _(')=                            /  \      |         |  _____   ____   ____   _____ |                .`        `.          | 
| / (___)._________________________.-'    \     |         | |__~__| |    | |    | |__~__||                :          :          | 
|/_________________________________________\    |         |         |    | |    |        |                 '.      .'           | 
|                                           |   lc________|         |   {| |}   |        |___________________\`'-'`/____________| 
|                                           |             |         |    | |    |        |                    |   | 
|                                           |             |_________|____|_|____|________|                    |___|
|                                           |   
|                                           |                                                                            . .           
|                                           |             ⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠜                        ⢀⠀⢿⠆⠀⠀⠸⡟⢹⠁⠀⠀⠀⠈⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
hjm_________________________________________|               ⠸⢷⣄⠠⠀⠀⠀⢠⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠀                                ⠃⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠙⢆⠀⠈⣄⢸⡄⢀⣤⢁⠄⠀⠀⠀⠀⠔⠊⠁⠀⠀⠀⠀                              ⠘⠛⠀⠀        
                                                             ⠀⠀⠀⠀⠀⠳⣤⣸⣿⣷⣿⣿⣿⠀⣀⠴⠂⠀⠀⠀⠀⠀⠀⠀⠀
                                                             ⠀⠀⠠⢤⣀⣴⣿⣿⣿⣿⣿⣿⣿⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                            ⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀
                                                            ⠀⠀⠀⣤⡶⠻⢿⣿⣿⣿⣿⣿⣿⣿⡿⠦⢤⣀⣀⡀⠀⠀⠀⠀⠀
                                                             ⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠛⠙⠻⣏⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀
                                                             ⢀⠀⢿⠆⠀⠀⠸⡟⢹⠁⠀⠀⠀⠈⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                             ⠀⠀⠀⠀⠀⠀⠀⠃⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                             ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀
            

          """)

def cabin_living():
    print("""
                        ____________________________________________________________________________________________________
                        |                     ||_|_|_|_|_|_|_|_|_|_|_|                                                      |
                        |                     |_|_|_|_|_|_|_|_|_|_|_||                                                      |
                        |                     ||_|_|_|_|_|_|_|_|_|_|_|                                                      |
                        |                     |_|_|_|_|_|_|_|_|_|_|_||                                                      |
                        |                     ||_|_|_|_|_|_|_|_|_|_|_|                                                      |
                        |  _                  |_|_|_|_|_|_|_|_|_|_|_||                                                      |
                        | /_\                 ||_|_|_|_|_____|_|_|_|_|                                                      |
                        | =|=                 |_|_|_|_|_|_|_|_|_|_|_||                                                      |
                        |=================,;,/________________________\,;,=================================================     
                        |                                                               O                                   |
                        |                 =;============================;=             /~\                                  |    
                        |                  [_|_|_]================[_|_|_]              |~|               .-=""'""'"'=-.     | 
                        |                  [__|__]                [__|__]    __________|_|____          | . . . . . . . |   |
                        |                  [_|_|_] o            o [_|_|_]    |       |       |          | .'.'.'.'.'.'. |   |
                        |                  [__|__] |            | [__|__]    |       |       |         ()_______________()  |
                        |                  [_|_|_] |---@@@@@@---| [_|_|_]    |      ~|~      |         ||_______________||  |
                        |                  [__|__]/!\ @@@@@@@@ /!\[__|__]    |       |       |        |                   | |                
                        lc_______________ /______________________________\___|_______|_______|________|                   | |
                                         |________________________________|  ||"           "||        |___________________|                
                                                    
                                ~=======,,,,,=====================================~     _
                                ~========\%%%%\===================================~   (_)
                                ~==========\%%%%\=========================?=======~   
                                ~============\%%%%\===============================~ 
                                ~============`````======.=====.===================~
                                ~====================='.'...'.'===================~

                               
          """)

def cabin_kitchen():
    print("""

                    
                    |'.                    (|)                     .'|
                    |  '.                                        .'  |
                    |    '.                                    .'    |
                    |      '. ______________________________ .'      |
                    |        :                              :     .. |
                    |        :     mmmmmmm                  :   .'|| |
                    |        :     |  |  |                  :  |  || |
                    |        :     |--|--|                  :  I  || |
                    |        :     |__|__|                  :  |  || |
                    |        :                              :  |  || |
                    |        :;;       .'````````````````:  :  |  || |
                    |        :||___   :================:'|  :  | 0+| |
                    |        :||===)  | |              | |  :  |  || |
                    |        ://``\\\__|_|______________|_|__:  I  || |
                    |      .'/'    \\' | '              | '   '.|  || |
                    |    .'           |                |       '. || |
                    |  .'                                        '|| |
                    |.'                                            '.|
                    
          """)

def cabin_room():
    print("""

                   o(=(=(=(=)=)=)=)o
                    !!!!!!}!{!!!!!!                                                ___ 
                    !!!!!} | {!!!!!                                               /   \\
                    !!!!}  |  {!!!!             ()              ()               | //  |
                    !!!'   |   '!!!             ||______________||               |     |
                    ~@~----+----~@~             |                |                \___/
                    !!!    |    !!!             |                |              _________
                    !!!    |    !!!             |_______  _______|             |____-____|
                    !!!____|____!!!  _________  {__~@~__}{__~@~__}             |____-____|
                    !!!=========!!!   |__-__|   %%%%%%%%%%%%%%%%%%             |____-____|
                   _!!!_________!!!___|_____|_ %%%%%%%%%%%%%%%%%%%% ___________|____-____|_
                                      |     | %%%%%%%%%%%%%%%%%%%%%%           |/       \|
                              .              %%%%%%%%%%%%%%%%%%%%%%%%
                           ..   .           %%%%%%%%%%%%%%%%%%%%%%%%%%
                    ⢀⠀⢿⠆⠀⠀⠸⡟⢹⠁⠀⠀⠀   ⠀⠀     %%%%%%%%%%%%%%%%%%%%%%%%%%%%
                         ⢸ ⣷⠀⠀⠀⠀⠀⠀⠀   ⠀   /!!!!!!!!!!!!!!!!!!!!!!!!!!!!\\
                              ⠘⠛⠀         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                          !!!!!!!!!!!!!!!!!!!!!!!!!!lc!!
                                          `======~@~==========~@~======`
                                         `==============================`
                                        `====~@~==================~@~====`
                                        `==================================`
                                      `==~@~==========================~@~==`
                                            
                                         


          """)

def inv_bathroom():
    message = ()
    for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.040)


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


# ----------------- Inicio del juego ------------------------------------------------------
def start_game():
    global myPlayer  # Indica que quieres utilizar la variable global

    print('\nCargando el juego, esto puede tomar algunos segundos...')
    time.sleep(2)
    print('\n+----------------------------------------------------------------------------------------------------+')
    print('\nHola, ¿cuál es tu nombre? ')
    player_name = input('\n> ')
    myPlayer = Player(name=player_name)
    while not player_name:
        time.sleep(1)
        print('Por favor dime tu nombre: ')
        player_name = input('\n> ')
    time.sleep(1)
    if player_name.lower() in ['samir']:
        print(f'\n¡Así que eres {myPlayer.name}!\n\n'
              f'¡No vas a poder jugar!\n')  # Easter Egg
        sys.exit()
    else:
        print(f'\nEse es un grandioso nombre. ¡Bienvenido {myPlayer.name}!')
    time.sleep(1)
    while True:
        print('\n¿Estás listo para comenzar (si/no)? ')
        option = input('\n> ')
        time.sleep(1)
        if any(keyword in option.lower() for keyword in ['si', 'no']):
            if option.lower() == 'si':
                print('\n¡Esa es la actitud! Empecemos...\n')
            elif option.lower() == 'no':
                print('\n¡No me importa! Empecemos...\n')
            break
        else:
            print('\nNo te escuche bien...')
            time.sleep(1)

    print('+----------------------------------------------------------------------------------------------------+\n')

    prologo()


# Introducción del juego donde conocerás el comienzo de la historia
def prologo():
    time.sleep(2)
    print('\nCargando...\n')
    time.sleep(2)
    print('\n+----------------------------------------------------------------------------------------------------+')
    print('''                                         ╔═╗╦═╗╔═╗╦  ╔═╗╔═╗╔═╗
                                         ╠═╝╠╦╝║ ║║  ║ ║║ ╦║ ║
                                         ╩  ╩╚═╚═╝╩═╝╚═╝╚═╝╚═╝''')
    print('+----------------------------------------------------------------------------------------------------+\n')
    print("""  \n
                                     _____________ 
                                    |             |  
                   ,==.-------.     | *RING RING *|  
                  (    ) ====  \    /_____________|    
                  ||  | [][][] |
                ,8||  | [][][] |
                8 ||  | [][][] |
                8 (    ) O O O /
                '88`=='-------'            
            \n

            """ )
    time.sleep(1.5)
    text_to_display = (
        f'\n\nEl teléfono suena con insistencia en la madrugada.\n\n'
    )

    for char in text_to_display:
        print(char, end='', flush=True)
        time.sleep(0.040)
    

    while True:
        text = ('\n¿Quieres contestar (si/no)?\n')
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.040)
        option = input('\n> ')
        if any(keyword in option.lower() for keyword in ['si', 'no']):
            if option.lower() == 'si':
                message = (
                    f'\nUna voz ronca de una mujer suena del otro lado del teléfono en cuanto contestas.\n\n'
                    f'- "¿Hola...? ¿Eres {myPlayer.name}, no?\n'
                    f'   No sabes lo mucho que cuesta conseguir tu número. Bueno, como sea, esto es urgente, Te necesitamos\n'
                    f'   en la oficina ahora."\n\n'
                    f'Finaliza la llamada antes de que pudieras replicar.\n\n'
                    f'...\n\n'
                )
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.025)

                text = ('\n¿Irás a la oficina (si/no)?\n ')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
                option = input('\n> ')
                while not any(keyword in option.lower() for keyword in ['si']):
                    if any(keyword in option.lower() for keyword in ['no']):
                        print('\n¿No? Parecía importante... ')
                        option = input('\n> ')
                    else:
                        print('\nEsa respuesta no es válida.')
                        print('\nTe pregunto de nuevo, ¿irás a la oficina (si/no)? ')
                        option = input('\n> ')
                message = (
                    f'\nExcelente...\n\n'
                    f'Será mejor ir ahora.\n\n'
                )
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.040)

                time.sleep(1)

                print('+----------------------------------------------------------------------------------------------------+\n')

                oficina()
                break

            elif option.lower() == 'no':
                message = (
                    f'\nDejas sonando el teléfono hasta que suena el último pitido.\n\n'
                )
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
                message = (f'... \n\n')
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.060)
                message = (f'Oh, no. Parece que no puedes volver a conciliar el sueño.\n'
                    f'Será mejor ir un rato a la cocina.\n'
                    f'\n')
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
                message = (f'.\n'
                           f'.\n'
                           f'.\n')
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.070)
                
                
                time.sleep(1.9)
                print("""
                        \n
                        0================================================0
                        |'.                    (|)                     .'|
                        |  '.                   |                    .'  |
                        |    '.                |O|                 .'    |
                        |      '. ____________/===\_____________ .'      |
                        |        :            `\"/`  ______     :     .. |
                        |        :     mmmmmmm  V   |--%%--|    :   .'|| |
                        |        :     |  |  |      |-%%%%-|    :  |  || |
                        |        :     |--|--| @@@  |=_||_=|    :  I  || |
                        |        :     |__|__|@@@@@ |_\__/_|    :  |  || |
                        |        :             \|/   ____       :  |  || |
                        |        :;;       .'``(_)```\__/````:  :  |  || |
                        |        :||___   :================:'|  :  | 0+| |
                        |        :||===)  | |              | |  :  |  || |
                        |        ://``\\\__|_|______________|_|__:  I  || |
                        |      .'/'    \\' | '              | '   '.|  || |
                        |    .'           |                |       '. || |
                        |  .'                                        '|| |
                        |.'                                            '.|
                        0================================================0
                        \n
                        """)
                
                time.sleep(1)


                message = (

                    f'\nComo siempre, no hay nada más que una pequeña televisión arrinconada junto a las frutas que están \n'
                    f'en el punto antes de volverse malas.\n\n'
                    f'...\n\n'
                )
                for char in message:
                    print(char, end='', flush=True)
                    time.sleep(0.040)

                frutas = obtener_lista_frutas()

                while True:
                    text = ('\n¿Qué tienes ganas de hacer ahora...? \n')
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(0.040)
                    option = input('\n> ')
                    time.sleep(1)
                    if any(keyword in option.lower() for keyword in ['fruta', 'nada', 'salir', 'encender', 'ver', 'dormir', 'levantarte', 'inspeccionar', 'comer', 'comerme', 'levantarme']):
                        if any(fruta in option.lower() for fruta in frutas) or 'comer' in option.lower() or 'comerme' in option.lower():
                            text = ('\n¡Wuacala, que asco!')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                            time.sleep(0.1)
                            text = (f'Será mejor tirar la fruta antes de cualquier incidente...\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif 'nada' in option.lower():
                            text = (f'\nEntiendo.., entonces no hay razón para estar en la cocina.\n'
                                  f'\nSerá mejor ir a la habitación.\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif 'salir' in option.lower():
                            text = ('\n¿Adónde vas...?\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif 'encender' in option.lower():
                            text = ('\nBien, habrá que buscar el control remoto.\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif 'ver' in option.lower():
                            text = ('\nBien, habrá que buscar el control remoto.\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif 'dormir' in option.lower():
                            text = (f'\nEntendible...\n'
                                  f'Será mejor ir a la habitación.\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif any(keyword in option.lower() for keyword in ['levantarse', 'levantarme']):
                            text = ('\nBien.\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        elif 'inspeccionar' in option.lower():
                            text = ('\nNo encontrarás mucho de todos modos.., pero está bien\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        break
                    elif any(keyword in option.lower() for keyword in ['ayuda']):
                        text = (f'\nLa verdad, no hay mucho que puedas hacer...\n\n'
                                f'Siempre puedes aprovechar para inspeccionar tu alrededor, ver la TV o \n'
                                f'comer una de las tantas frutas en tu cocina :)\n\n' )
                        for char in text:
                            print(char, end='', flush=True)
                            time.sleep(0.040)
                    else:
                        text = ('\n(๏̯͡๏). Será mejor que hagas otra cosa...\n')
                        for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                        time.sleep(1)

                note = (
                    f'...\n\n'
                )
                for char in note:
                    print(char, end='', flush=True)
                    time.sleep(0.075)

                time.sleep(1)
                print("""
                      \n
                      \n
                           \  /
                            \/
                    .====================.
                    | .----------------. |
                    | |                | |
                    | | Encendiendo... | |
                    | |                | |   
                    | '----------------'o|  
                    |====================|  
                    |####################|  
                    '===================='  
                      
                    \n
                    \n  
                      """)
                
                time.sleep(0.75)


                note = (
                    f'\n¡Oh! Parece que se ha encendido la televisión.\n' 
                    f'\nEn cuanto intentaste levantarte has movido la mesa tirando el control.\n\n'
                    f'\nEstán pasando las noticias.\n\n' 
                    f'\nComo no es novedad, un crimen verdaderamente horrible se ha cometido en tu ciudad\n'
                    f'\nEl nombre de la víctima está escrito justo en la parte inferior de la pantalla.\n'
                    f'\n'
                    f'\n'
                    
                )
                for char in note:
                    print(char, end='', flush=True)
                    time.sleep(0.040)

                time.sleep(1.8)
                
                text = ('               Martín Arriaga Pérez\n\n\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.1)
                
                time.sleep(1.5)
                
                text = (f'\n\n'
                        f'Es el nombre de tu mejor amigo.\n\n'
                        f'¿Cómo...?\n\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)

                while True:
                    text = (
                        f'\n¿¿¿Qué harás ahora???\n'
                        f'\nOpciones:'
                        f'\n    - Nada'
                        f'\n    - Correr a buscarlo'
                        f'\n    - Llorar\n'
                    )
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(0.040)

                    option = input('\n> ')
                    time.sleep(1)
                    if any(keyword in option.lower() for keyword in ['nada', 'correr', 'llorar']):
                        if 'nada' in option.lower():
                            text = (
                                f'\nAl poco tiempo caes en depresión y obtienes una dependencia a medicamentos.\n'
                                f'Mueres de una sobredosis.\n\n'
                                f'...\n\n'
                            )
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.075)
                            
                            time.sleep(2)

                            bad_ending()

                        elif 'correr' in option.lower():
                            text = (
                                f'\nAbres la puerta sin preocuparte por cerrarla, está muy cerca de tu casa.\n'
                                f'Sabes que la casa de tu amigo está muy cerca de ti.\n'
                                f'\n'
                                f'... Tiene que estar ahí.\n\n'
                                f'En cuanto pones un pie fuera de la banqueta, una luz te deslumbra por completo para en seguida todo volverse negro.\n\n'
                                f'\nEl 17/11/1986 moriste atropellado por un autobús.'
                                f'...\n\n'
                            )
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.075)
                            
                            time.sleep(2)

                            bad_ending()

                        elif 'llorar' in option.lower():
                            text = (
                                f'\nGran decisión.\n\n'
                                f'...\n'
                            )
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.025)
                            time.sleep(1.8)
                            text = (
                                f'\nYa que ya te desahogaste...\n\n' )
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                            while True:
                                text = ('¿Crees que sea conveniente llamar a la policía?\n ')
                                for char in text:
                                    print(char, end='', flush=True)
                                    time.sleep(0.040)
                                option = input('\n> ')
                                if option.lower() == 'si':
                                    text = (
                                        f'\nDespués de llamar a la policía, prometieron hacer su trabajo. Sin embargo, después\n'
                                        f'de unos meses dejaron de investigar el caso marcándolo como un suicidio.\n'
                                        f'\n'
                                        f'\n'
                                        f'\n'
                                        f'Al final, la depresión se apodera por completo de ti y terminas quitándote la vida el 03 de diciembre de 1987.\n\n'
                                        f'...\n\n'
                                    )
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.075)

                                    bad_ending()

                                elif option.lower() == 'no':
                                    text = (
                                        f'\nAl poco tiempo caes en depresión y obtienes una dependencia a medicamentos.\n'
                                        f'\n'
                                        f'Parece que al pasar los años no lograste sobrellevarlo\n'
                                        f'\n'
                                        f'\n...\n\n'
                                        f'Mueres de una sobredosis el 17 de Julio de 1989.\n\n' 
                                        # Agregar una imagen ascii de drogadictos
                                        f'...\n\n'
                                    )
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.075)
                                    
                                    time.sleep(1.8)

                                    bad_ending()
                                else:
                                    print('\nTienes que tomar una decisión.\n')
                                    time.sleep(1)
                        break
                    else:
                        print('No creo que eso sea conveniente en este momento...\n\n')
                        time.sleep(1)
        else:
            print('\nEl teléfono sigue sonando y es bastante molesto...\n')
            time.sleep(1)


# Continuación del prólogo, donde conoces el expediente del caso y escoges un compañero para la partida
def oficina():
    time.sleep(2)
    print('\nCargando...\n')
    time.sleep(2)
    print('\n+----------------------------------------------------------------------------------------------------+')
    print('''                                          ╔═╗╔═╗╦╔═╗╦╔╗╔╔═╗
                                          ║ ║╠╣ ║║  ║║║║╠═╣
                                          ╚═╝╚  ╩╚═╝╩╝╚╝╩ ╩''')
    print('+----------------------------------------------------------------------------------------------------+\n')
    time.sleep(1)
    text = (
        f'En cuanto llegas tu jefe te intercepta con tanta prisa que atropella a algunas personas \n'
        f'en el breve trayecto que recorre hasta ti.\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    
    time.sleep(2)

    print(""" \n
           __________. 
           |  < (_) >|
           /==== =====
          (.---._ _.-.)
           |/   a` a |
           (      _\ |
            \    __  ;
            |\   .  /
         _.'\ '----;'-.
     _.-'  O ;-.__.'\O `o.
    /o \      \/-.-\/|    \\
   |    ;,     '.|\| /     |
                                                              \n   """)

    time.sleep(2)

    print(f"""
                   |\________________________________________________________             
                   |                                                         |
                   |   Es Martin, {myPlayer.name}, quería que te enteraras   
                   |   antes de que saliera en las noticias.                 |
                   |                                                        /   
                    \______________________________________________________/                    
          
                                                                   """)
    time.sleep(2.5)

    text = ( f'\n ... \n\n'
            f'Martin, ¿tu mejor amigo...?\n'
            f'\nImposible.\n'
            f'\n¿Quién sería capaz...?\n\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.078)
    
    time.sleep(1.8)
    

    print("""
                   |\____________________________________________________________             
                   |                                                             |
                   |   Como se trata de alguien que era cercano a ti, más        |
                   |   te vale encontrar al asesino y no equivocarte de nuevo.   |
                   |                                                            /   
                    \__________________________________________________________/   

          

                                                                   """)
    
    time.sleep(3.5)
    
    print("""

                   |\___________________________________________________________             
                   |                                                            | 
                   |    Aquí tienes el folder con el expediente del caso y los  |
                   |    perfiles de 2 candidatos para que elijas a uno          |
                   |    como compañero.                                        /   
                    \_________________________________________________________/                    
          
          """)

    time.sleep(4)

    text =(
        f' \n\n'
        f'Miras el folder y después unos segundos de duda que parecieron eternos, decides abrirlo.\n\n'
        f'Recuerda leer con atención los archivos dentro de este.\n\n'
    )
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)

    file_read = False
    profile_read = False
    letter_read = False
    first_option = False
    partner_choosen = False
    letter_unlocked = False
    seguir = True

    text = ('¿Qué archivos del folder quieres leer primero?\n')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)

    opcion_e = input('\n> ')
    while seguir:
        if any(keyword in opcion_e.lower() for keyword in ['ayuda', 'help', 'ayudame']):
            text = (f'\nRecuerda lo que tu jefe ha dicho:\n'
                    f'El folder contiene el *expediente* del caso y los *perfiles* de dos compañeros.\n'
                    f'\n¿Qué archivo del folder quieres leer?\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.040)
            opcion_e = input('\n> ')

        if any(keyword in opcion_e.lower() for keyword in ['expediente', 'reporte']):
            first_option = True
            if file_read:
                text = ('\nPor ahora, ya has visto el expediente.\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
            else:
                print('\n\nCargando expediente...')
                time.sleep(2)
                print('\n')
                criminal_file()
                time.sleep(1.8)
                file_read = True
                letter_unlocked = True
                text = ('\n\nEl expediente ha sido guardado en items :)\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
                myPlayer.add_item(criminal_file)

        elif any(keyword in opcion_e.lower() for keyword in ['perfil', 'perfiles', 'compañero', 'compañeros']):
            first_option = True
            if profile_read:
                text = ('\nPor ahora, ya has visto los perfiles.\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
            else:
                print('\n\nCargando perfiles...')
                time.sleep(2)
                print('\n')
                partner()
                time.sleep(1.8)
                profile_read = True
                text = ('\n\nAmbos perfiles han sido guardado en items:)\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
                myPlayer.add_item(partner)

                while not partner_choosen:
                    text = ('\n¿Con cuál de estas dos personas quieres trabajar?\n')
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(0.040)
                    election_partner = input('\n> ')
                    if any(keyword in election_partner.lower() for keyword in ['jose', 'pepe', 'paredes', 'pacheco', '1', 'primera', 'primer']):
                        myPartner.jose = True
                        partner_choosen = True
                        text = (f'\n¡Excelente!\n'
                                f'\nDurante el caso, José será tu compañero. Felicidades.\n' )
                        for char in text:
                            print(char, end='', flush=True)
                            time.sleep(0.040)
                    elif any(keyword in election_partner.lower() for keyword in ['marc', 'markus', 'davidson','2', 'segundo', 'segunda']):
                        myPartner.marcus = True
                        partner_choosen = True
                        text = (f'\n¡Excelente!\n\n'
                                f'\nDurante el caso, Marcus será tu compañero. Felicidades.\n' )
                        for char in text:
                            print(char, end='', flush=True)
                            time.sleep(0.040)
                    else:
                        text=('\nElige una opción válida...\n')
                        for char in text:
                            print(char, end='',flush=True)
                            time.sleep(0.040)

        elif letter_unlocked and any(keyword in opcion_e.lower() for keyword in ['carta', 'papel', 'hoja']):
            first_option = True
            if letter_read:
                text=('\nYa has leído la carta.\n')
                for char in text:
                    print(char, end='',flush=True)
                    time.sleep(0.025)
            else:
                print('\n\nCargando carta...')
                time.sleep(2)
                print('\n')
                letter()
                time.sleep(1.8)
                text = ('\n\nLa carta ha sido guardada en items :)\n')
                letter_read = True
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.025)
                myPlayer.add_item(letter)

        else:
            text=('\nOpción inválida. Elige algo que te hayan entregado...\n')
            for char in text:
                print(char, end='',flush=True)
                time.sleep(0.040)
            opcion_e = input('\n> ')

        if letter_read and profile_read and file_read:
            text = ('\n¡Perfecto! Ya has leído todos los archivos del expediente.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.040)
            break

        while first_option:
            text=('\n\n¿Quieres leer alguna otra cosa en el folder (si/no)?\n')
            for char in text:
                print(char, end='',flush=True)
                time.sleep(0.040)
            opcion_sino = input('\n> ')

            if any(keyword in opcion_sino.lower() for keyword in ['si']):
                text=('\n¿Qué quieres leer?\n')
                for char in text:
                    print(char, end='',flush=True)
                    time.sleep(0.040)
                opcion_e = input('\n> ')
                first_option = False

            elif any(keyword in opcion_sino.lower() for keyword in ['no']):
                if not file_read or not profile_read:
                    text=(f'\nCreo que todavía te falta una cosa por leer...\n'
                          f'\nRecuerda que tu jefe te ha entregado el expediente y los perfiles.\n')
                    for char in text:
                        print(char, end='',flush=True)
                        time.sleep(0.040)
                else:
                    seguir = False
                    first_option = False
                    break

            else:
                text=('\nOpción inválida. Tienes que elegir (si/no).\n')
                for char in text:
                    print(char, end='',flush=True)
                    time.sleep(0.040)
    


    text = (
        f'\n¡Muy bien! Podrás acceder a lo que leíste en el folder más adelante.\n'
    )
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)
    
    time.sleep(1.5)

    text = (
        f'\n\nAhora, quizá te encuentres peligros durante tu investigación, así que necesitarás algo de ayuda.\n'
        f'\nEscoge dos de las cosas que se encuentren en la armería.\n'
    )
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)
    
    print('\n\nCargando armería...')
    time.sleep(2)
    print('\n')

    print("""
           +-----------------------------------------------------------------------------------------------------+
              __,_____
             / __.==--"       ________ ____________       _________________.---.______                 __  __
            /#(-'            |_____ __)._______.-'       (_(______________(_o o_(____()               )  \/  (
            `-'                                                       .___.'. .'.___.                |XXXXXXXX|
           Pistola               Navaja                               \ o    Y    o /                |HHHHHHHH|
                                                                       \ \__   __/ /                 |XXXXXXXX| 
                                                                        '.__'-'__.'                   |||||||| 
                                                                            '''                                  
                                                                      Hacha                       Chaleco Antibalas                                                      
                                                    
            +----------------------------------------------------------------------------------------------------+
          """)

    time.sleep(1.8)

    text = (f'\n¿Qué quieres llevar para el caso?\n')    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    while len(myPlayer.weapons) < 2:
        option = input('\n> ')
    
        if any(keyword in option.lower() for keyword in ['pistola', 'navaja', 'hacha', 'chaleco', 'antibalas']):
            if option.lower() == 'pistola':
                myPlayer.add_weapon('pistola')
                myPlayer.gun = True
            elif option.lower() == 'navaja':
                myPlayer.add_weapon('navaja')
            elif option.lower() == 'hacha':
                myPlayer.add_weapon('hacha')
            elif option.lower() in ['chaleco', 'antibalas']:
                myPlayer.bulletproof = True
    
            if len(myPlayer.weapons) == 2:
                text = ('\nYa has elegido. Esto es lo que llevarás contigo:\n\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
                myPlayer.get_weapons()  # Imprimir las armas elegidas por el jugador
            else:
                text = ('\nExcelente. Aún puedes elegir otra cosa más :)\n')
                for char in text:
                    print(char, end='', flush=True)
                    time.sleep(0.040)
        else:
            text = ('\nPor favor, elige alguna de las opciones en la armería.\n')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.040)

    text = (f'\n\n¡Perfecto! Ahora ya estás listo para comenzar.\n'
            f'\nLo primero será ir a investigar la escena del crimen. La cabaña.\n'
            f'\n{myPartner.partner_name} te verá allá.\n\n'
            f'\nMucha suerte atrapando al culpable.\n')    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)
    
    cabin()
##_---------------------------------------------------------------------------------------------

# Primer capítulo, continuación del prólogo y la oficina
def chapter_1():
    pass


# Segundo capítulo, este solo podrás acceder luego de que investigues cada escenario en el capítulo 1
def chapter_2():
    pass

baño = False
sala = False
cocina = False
cuarto = False

# --------------------- Escenarios del juego -----------------------------------------------------
# Lugares de la historia donde habrá pistas y una descripción breve del lugar
def cabin():
    text = (f'\n.\n'
            f'.\n'
            f'.\n')    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    time.sleep(2.3)
    # Cambiar de musica en la cabaña
    print(f'\n'
        f'\n+----------------------------------------------------------------------------------------------------+\n'
        f'                                                        /\\\n'
        f'                                               __      /%%\\\n'
        f'                                             |_I_|     /%%\\\n'
        f'                   _________________/,\'_____ |I_I|____/%%%%\\/\\\n'
        f'                 /\\\'.___.\'____.\'__./\'/_\\\'.__.\'__.\'__.\'\\%%%%/%%\\\n'
        f'                /%%\\_.\'___.\'___.\'./\\/_ _\\.\'__.\'__.\'__.\'\\%%/%%%%\\\n'
        f'               /%%%%\\.__.\'___.\'._/\\/|_|_|\\.__.\'__.\'__.\'.\\%/%%%%\\   \n'
        f'               /%%%%\\_.\'__.\'__.\'.\\/_|_|_|_\\\'.___.\'__.\'___\\%%%%%%\\                  \n'
        f'              /%%%%%%\\____________________________________\\%%%%%%\\\n'
        f'             /%%%%%%%%\\]== _ _ _ ============______======]%%%%%%%\\\n'
        f'             /%%%%%%%/\]==|_|_|_|============|////|======]%%%%%%%%\\__\n'
        f'          __/%%%%%%%/%%\\==|_|_|_|============|////|======]%%%%%%%%\\\n'
        f'           /%%%%%%%/%%%%\\====================|&///|======]%%%%%%%%%\\\n'
        f'           /%%%%%%%/%%%%\\====================|////|======]^^^^^^^^^^\n'
        f'          /%%%%%%%/%%%%%%\\===================|////|======]  _ - _ -\n'
        f'          /%%%%%%%/%%%%%%%\"""""""""""""""""""\'====\'"""""""""""""""""""\n'
        f'          ^^^^^^^/%%%%%%%%\\   _ -   _ -              _-                   ---   __\n'
        f'                 ^^^^^^^^^^                                           ---    \n'
        f'+----------------------------------------------------------------------------------------------------+  \n\n      '           
        f'        ')


    
    time.sleep(1.5)
    
    text = (f'\nParece que tu compañero {myPartner.partner_name()} aún no ha llegado...\n'
            f'\nLo mejor será comenzar a recolectar pistas por tu cuenta.\n'
            f'\nAquí tienes un pequeño mapa del interior de la cabaña.\n')    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)
    
    time.sleep(1.5)
    print('\n\nCargando mapa...\n')
    time.sleep(1.5)
    print('+----------------------------------------------------------------------------------------------------+  ')
    time.sleep(1)
    cabin_map()
    time.sleep(1)
    print('+----------------------------------------------------------------------------------------------------+  ')
    time.sleep(2.2)

    text = (f'\n¿En qué parte de la cabaña te gustaría comenzar buscando?\n')  
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.040)

    eleccion = input('\n> ')

    def select_cabin():
        global baño, sala, cocina, cuarto
        
        while True:
            if baño and sala and cocina and cuarto:
                pass
            
            else:
                if 'baño' in eleccion.lower():
                    if baño:
                        text = (f'\n!!\n'
                                f'\nParece que ya habías entrado al baño.\n'
                                f'\nNo querrás dañar la escena del crimen volviendo a entrar...\n')  
                        for char in text:
                            print(char, end='', flush=True)
                            time.sleep(0.040)
                    else:   
                        tina = False
                        espejo = False
                        inodoro = False
                        suelo = False
                        lavabo = False
                        baño = True
                        time.sleep(1.5)
                        print('\n\n\n Cargando baño... \n\n\n')
                        time.sleep(2.2)
                        cabin_bath()
                        time.sleep(1.8)
                        text = (f'\n¿Cuál de estos lugares te gustaría analizar más de cerca?\n\n')  
                        for char in text:
                            print(char, end='', flush=True)
                            time.sleep(0.040)
                        time.sleep(1.5)
                        print (f'    La tina.\n'
                                f'    El espejo.\n'
                                f'    El suelo.\n'
                                f'    El lavabo\n'
                                f'    El inodoro\n'
                                f'    Mejor nada...')  
                        analize = input('\n> ')

                        while True:
                            if tina and espejo and inodoro and suelo and lavabo:
                                text = (f'\n¡Increíble!\n\n'
                                        f'Haz anallizado cada rincón del baño\n')  
                                for char in text:
                                    print(char, end='', flush=True)
                                    time.sleep(0.040)
                                break
                            else:
                                if 'tina' in analize.lower():
                                    text = (f'\nAquí fue encontrado el cuerpo de Martin.\n'
                                            f'\n.'
                                            f'\n.'
                                            f'\n.\n'
                                            f'\nParece que lo único que hay es un enorme charco de su sangre...\n')  
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)

                                elif 'espejo' in analize.lower():
                                    print(""" 
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠟⠛⠛⠛⠛⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⣠⡶⠟⠛⠛⠷⣦⣄⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⢀⣾⠃⠰⠟⢠⡶⠶⠶⣦⣄⠉⠳⣤⡈⢻⣦⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⣼⠇⣰⡆⢠⡄⠀⣀⣀⣀⠙⠻⣦⡙⢿⣆⠉⠁⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠰⠿⢠⡿⠀⣿⠀⣾⠋⣉⠙⢷⣄⠈⠻⣦⡙⢳⣄⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⣤⠀⠚⠃⠀⣿⠀⣿⡀⠹⣷⡀⠙⢷⣄⠈⠻⡦⠁⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⣿⠀⣴⠰⣦⠘⣆⠈⢿⣦⡈⠻⢷⣄⠙⠻⠀⣤⠄⣰⡄⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⢿⡆⢻⡆⠹⣧⠙⣦⡀⠉⠻⣦⣄⠙⠳⠆⢠⡿⢀⣿⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⢸⣇⠈⣿⠀⠘⢷⣌⠛⠶⡤⠀⣉⠛⠆⢠⡿⢁⣾⠃⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠟⢀⣠⣴⠦⠀⠙⢃⣀⣀⠈⠙⠛⠀⠛⢁⣾⠃⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠛⠉⣠⣴⠾⠛⢛⣉⣙⣛⡛⠗⠰⣦⠀⠁⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢠⡶⠟⢛⣉⣉⣉⡛⠛⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⢋⣁⣠⣈⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                                """)
                                    text = (f'\n¡Oh! Una huella.\n'
                                            f'\nMe pregunto de quién será...\n')  
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)

                                elif 'inodoro' in analize.lower():
                                    text = (f'\nMmmm...\n'
                                            f'\nNo hay nada relevante.'
                                            )  
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)

                                elif 'suelo' in analize.lower():
                                    text = (f'\nNo parece haber nada más que sangre...\n\n')  
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)
                                    time.sleep(2.4)
                                    text = (f'\n ...\n')
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.080)
                                    time.sleep(1.5)
                                    text = (f'\nSe acaba de escuchar una puerta abriéndose.\n'
                                            f'\nAlguien más acaba de entrar a la cabaña.\n')
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)
                                    time.sleep(2.4)
                                    text = (f'\nTienes que actuar ya.\n'
                                            f'\n¿Qué harás?\n')
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)
                                    myPlayer.get_weapons()
                                    print(f'        Nada')
                                    serious_op = input('\n> ')

                                    if 'tomar' in serious_op.lower():
                                        while True:
                                            if any(palabra in serious_op.lower() for palabra in myPlayer.weapons):
                                                text = (f'\nToma algo que tengas en tu armería...\n')
                                                for char in text:
                                                    print(char, end='', flush=True)
                                                    time.sleep(0.040)
                                                serious_op = ('\n> ')
                                            else:    
                                                if 'pistola' in serious_op.lower():
                                                    text = (f'\nBien.\n'
                                                            f'\nEstás apuntando a la puerta del baño que por ahora estpá cerrada.\n')
                                                    for char in text:
                                                        print(char, end='', flush=True)
                                                        time.sleep(0.040)
                                                    text = (f'\n ...\n')
                                                    for char in text:
                                                        print(char, end='', flush=True)
                                                        time.sleep(0.080)
                                                    print ("""
  ____    _    _   _  ____ _ 
 | __ )  / \  | \ | |/ ___| |
 |  _ \ / _ \ |  \| | |  _| |
 | |_) / ___ \| |\  | |_| |_|
 |____/_/   \_\_| \_|\____(_)
                                 
                                                            """)  
                                                    if myPartner.jose:
                                                        time.sleep(3)
                                                        text = (f'\nDisparaste.\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        time.sleep(1.9)
                                                        text = (f'\nLa puerta sigue cerrada. Lograste disparar antes de que entrara.\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        text = (f'\n...¿Quieres abir la puerta?\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        open = input('\n> ')
                                                        while not any(keyword in open.lower() for keyword in ['si']):
                                                            if any(keyword in open.lower() for keyword in ['no']):
                                                                text = (f'\nCreo que sería mejor si lo haces.'
                                                                        f'\n...¿Quieres abir la puerta?\n')
                                                                for char in text:
                                                                    print(char, end='', flush=True)
                                                                    time.sleep(0.040)
                                                                open = input('\n> ')
                                                            else:
                                                                print('\n??')
                                                                print('\n¿Sí o no...?\n')
                                                                open = input('\n> ')

                                                        # Cuando abre la puerta

                                                        text = (f'\nHay alguien en el suelo. Le has dado. Felicidades.\n'
                                                                f'\nOh.\n'
                                                                f'\nParece que tiene algo en su mano...\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        
                                                        print (""" 
   ,   /\   ,
  / '-'  '-' \\ 
 | DETECTIVE  |
 \    .--.    /
  |  ( 19 )  |
  \   '--'   /
   '--.  .--'
       \/
                                                               

    """)

                                                        text = (f'\n¿Un detective?\n'
                                                                f'\nParece ser que su nombre está en la parte trasera de la placa...\n\n\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        text = (f'\n ...\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.070)
                                                        text = ('               José Paredes Pacheco \n\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.1)
                                                        
                                                        text = (f'\nOh.\n'
                                                                f'\nLe has disparado a tu compañero.\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.075)
                                                        time.sleep(2.8)
                                                        text = (f'\n.\n'
                                                                f'.\n'
                                                                f'.\n')    
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.1)
                                                        time.sleep(3)
                                                        text = (f'\nNo duraste mucho, ¿verdad?\n'
                                                                f'\nDespués de este incidente te removieron en seguida del caso, {myPlayer.name}.\n'
                                                                f'\nNo encontraste al culpable y no pudiste hacer nada por Martin.\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.060)
                                                        time.sleep(2.5)
                                                        bad_ending()

                                                    elif myPartner.marcus:
                                                        time.sleep(3)
                                                        text = (f'\nTe han disparado.\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        time.sleep(1.9)
                                                        text = (f'\n ...\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.070)
                                                        time.sleep(1)
                                                        text = (f'\nNo supiste en qué momento pero ya estás en suelo.\n'
                                                                f'\nDe repente hace mucho frío...\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.080)
                                                        text = (f'\n¿Quién es...?\n'
                                                                f'\nHay alguien parado en frente de ti.\n'
                                                                f'\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        time.sleep(2)
                                                        text = (f'\n!!!?\n'
                                                                f'\nEs Marcus...,¿cómo....?.\n'
                                                                f'\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.040)
                                                        text = (f'\n.\n'
                                                                f'.\n'
                                                                f'.\n')    
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.1)
                                                        text = (f'\nMoriste desangrado el 17 de Noviembre de 1986\n'
                                                                f'\nEs Marcus...,¿cómo....?.\n'
                                                                f'\n')
                                                        for char in text:
                                                            print(char, end='', flush=True)
                                                            time.sleep(0.075)
                                                            bad_ending()                         

                                                elif 'hacha' in serious_op.lower():
                                                    text = (f'\nBien, sostenla fuerte.\n')
                                                    for char in text:
                                                        print(char, end='', flush=True)
                                                        time.sleep(0.040)
                                                    time.sleep(2)
                                                    text = (f'\nLa puerta se ha abierto...\n'
                                                            f'\nOh.\n'
                                                            f'\nEs José.\n')
                                                    for char in text:
                                                        print(char, end='', flush=True)
                                                        time.sleep(0.040)
                                                    print(""" 

                                                          """)


                                                elif 'navaja' in serious_op.lower():
                                                    pass

                                    elif 'nada' in serious_op.lower():
                                        if myPartner.jose:
                                            pass
                                        elif myPartner.marcus:
                                            pass                       

                                elif 'nada' in analize.lower():
                                    text = (f'\nBien, será mejor continuar.\n')  
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)
                                    time.sleep(2.4)
                                    select_cabin()

                                else:
                                    text = ('\nRevisa algo que esté en el baño... \n')
                                    for char in text:
                                        print(char, end='', flush=True)
                                        time.sleep(0.040)

                            
                            text = ('\n¿Qué otra cosa quisieras revisar?\n')
                            for char in text:
                                print(char, end='', flush=True)
                                time.sleep(0.040)
                            analize = input('\n> ')

                    
                    # Colocar lo demás para encontrar las pistas

                elif 'sala' in eleccion.lower():
                    sala = True
                    time.sleep(1.5)
                    print('\n\n\nCargando sala... \n\n\n')
                    time.sleep(2.2)
                    cabin_living()
                    time.sleep(1.8)
                
                elif 'cocina' in eleccion.lower():
                    cocina = True
                    time.sleep(1.5)
                    print('\n\n\nCargando cocina... \n\n\n')
                    time.sleep(2.2)
                    cabin_kitchen()
                    time.sleep(1.8)

                elif 'cuarto' in eleccion.lower():
                    cuarto = True
                    time.sleep(1.5)
                    print('\n\n\nCargando cuarto... \n\n\n')
                    time.sleep(2.2)
                    cabin_room()
                    time.sleep(1.8)
                
                else:
                    text = (f'\nCreo que eso no está en la cabaña... \n')  
                    for char in text:
                        print(char, end='', flush=True)
                        time.sleep(0.040)
    
    select_cabin()

        







def lugar2():
    print('\n¡Bienvenido a Lugar2!')
    # Implementa la lógica para el lugar2


def lugar3():
    print('\n¡Bienvenido a Lugar3!')
    # Implementa la lógica para el lugar3


def lugar4():
    print('\n¡Bienvenido a Lugar4!')
    # Implementa la lógica para el lugar4


def lugar5():
    print('\n¡Bienvenido a Lugar5!')
    # Implementa la lógica para el lugar5



#oficina()
#title_screen()
#cabin()
#cabin_room()
