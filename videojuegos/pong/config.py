# fichero de configuración

v = 1.7

print(f'{__name__} v{v}')

CARPETA_SONIDO = 'sonidos/'
SONIDO_REBOTE_PARED = 'boing-pared.mp3'
SONIDO_REBOTE_RAQUETA = 'boing-raqueta.mp3'
SONIDO_PUNTO = 'sonido-punto.mp3'
# sonidos menu https://pixabay.com/es/sound-effects/search/block/
SONIDO_MENU_SELECCION = 'place-100513.mp3'
SONIDO_MENU = 'blocking-arm-with-hand-6941.mp3'

# TODO: Musica juego y menu
MUSICA_MENU = ''
MUSICA_JUEGO = ''

CONFIG_MUTE = 'mute'
CONFIG_N_JUGADORES = 'n_jugadores'
CONFIG_LANGUAGE = 'languaje'
CONFIG_LEVEL = 'level'

CARPETA_FUENTES = 'fuentes/'
FUENTE_JUGADOR1 = '8-BIT WONDER.TTF'
FUENTE_JUGADOR2 = 'Nicolast.ttf'
FUENTE_MENU = 'LETRA1.ttf'

ICONOS_SIZE = 96

# iconos https://icons8.com/icon/set/unmute/family-windows
CARPETA_IMAGENES = 'imagenes/'
ICONO_MUTE = 'icons8-mute-96.png'
ICONO_SOUND = 'icons8-sound-96.png'
# Iconos  -  https://boxicons.com/?query=
# https://www.freepik.com/search?format=search&last_filter=query&last_value=ROBOT+vs+robot&query=ROBOT+vs+robot&type=icon
ICONO_0_JUGADORES = 'robots_11808375.png'
# https://www.freepik.com/search?format=search&last_filter=query&last_value=1+player&query=1+player&type=icon
ICONO_1_JUGADOR = 'drone_2181593.png'
# https://www.freepik.com/search?format=search&last_filter=query&last_value=2+player&query=2+player&type=icon
ICONO_2_JUGADORES = 'change_6409303.png'

ICONO_ES = 'es_flag.png'
ICONO_EN = 'en_flag.png'
ICONO_DE = 'de_flag.png'

ICONO_RAQUETA1 = 'barra1.png'
ICONO_RAQUETA2 = 'barra2.png'
# https://www.freepik.com/author/smashicons/icons/basic-miscellany-lineal-color_311?t=f&query=emoji#from_element=families
ICONO_NIVEL_FACIL = 'happy_4951994.png'
ICONO_NIVEL_DIFICIL = 'grimacing_4955392.png'
ICONO_NIVEL_PESADILLA = 'sweating_1094605.png'

ICONOS_PELOTA = 'pelotas.png' # 'balls.png'
ICONO_PELOTA_NUMERO_FRAMES = 8
ICONO_PELOTA_SIZE = 32

FONDO1 = 'fiesta-halloween.jpg' # fondo1.png'

# fuentes de Dafont: https://www.dafont.com/
# paleta en https://htmlcolorcodes.com/es/
BLACK = (0,0,0)
RED = (255,0,0)
PURPLE = (200,50,240)
GREEN = (55,236,0)
WHITE = (255,255,255)
DARK_GRAY = (150,150,150)
BLUE = (51,175,255)

FONT_NAME = 'Arial'
FONT_SIZE = 25

MAX_VELOCIDAD = 25

COLOR_PLAYER1 = GREEN
COLOR_PLAYER2 = RED

COLOR_BALL = PURPLE

COLOR_FONDO_MENU = BLUE
COLOR_OPCION = BLACK
COLOR_OPCION_SELECCIONADA = DARK_GRAY

COLOR_AYUDA = BLUE

ancho_pantalla = 800
alto_pantalla = 600

opciones_visuales_es = [ ['Sonido On','Sonido Off'],
                     ['0 Jugadores','1 Jugador','2 Jugadores'],
                     ['Español', 'English', 'Deutch'],
                     ['Fácil', 'Difícil', 'Pesadilla'],   
                     ['Jugar','Salir'] ]

opciones_visuales_en = [ ['Sound On','Sound Off'],
                     ['0 Players','1 Player','2 Players'],
                     ['Español', 'English', 'Deutch'],
                     ['Easy', 'Hard', 'Nightmare'],
                     ['Play','Exit'] ]

opciones_visuales_de = [ ['Ton ein', 'Ton aus'],
                     ['0 Spieler', '1 Spieler', '2 Spieler'],
                     ['Español', 'English', 'Deutch'],
                     ['Einfach', 'Schwierig', 'Alphaum'],   
                     ['Play', 'Exit'] ]

str_Player = ['Jugador','Player','Playerborn']

opciones_visuales = [opciones_visuales_es, opciones_visuales_en, opciones_visuales_de]
str_pausa = ['Pausa','Pause','Pausen']
str_ayuda_titulo = ['Ayuda','Help','Ayuden']
ayuda_str_es = ['P - Pausa','H - Ayuda',
             'w - s Jugador 1','^ - v Jugador 2',
             '0, 1, 2 Número judadores',   
             'm Sonido on/off',
             'd, f, g Nivel dificultad',   
             'e, n, a Idioma',
             'q - Salir']

ayuda_str_en = ['P - Pause','H - Help',
             'w - s Player 1','^ - v Player 2',
             '0, 1, 2 Players number',
             'm Sound on/off',   
             'd, f, g Dificulty Level',
             'e, n, a Language',
             'q - Quit']

ayuda_str_de = ['P - Pausen','H - Ayuden',
             'w - s Player 1','^ - v Player 2',
             '0, 1, 2 Players number',
             'm Soniden on/off',                
             'd, f, g DificultyLevelsborn',
             'e, n, a Languajen',   
             'q - Aoufirdensen']

ayuda_str = [ayuda_str_es, ayuda_str_en, ayuda_str_de]

OPCION_SONIDO_ON = 0
OPCION_SONIDO_OFF = 1
OPCION_N_0_JUGADORES = 2
OPCION_N_1_JUGADORES = 3
OPCION_N_2_JUGADORES = 4
OPCION_ESPANOL = 5 # No ñ
OPCION_INGLES = 6
OPCION_ALEMAN = 7
OPCION_FACIL = 8
OPCION_DIFICIL = 9
OPCION_PESADILLA = 10
OPCION_JUGAR = 11
OPCION_SALIR = 12