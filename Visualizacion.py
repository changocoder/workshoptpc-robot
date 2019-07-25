# coding=UTF-8
import pygame, sys
from pygame.locals import *
from Laberinto import *
class Icono (pygame.sprite.Sprite):
    """
    ## Class Icono(pygame.sprite.Sprite)
    #Atributos
     ---------
      - rect      : *pygame.Rect*
      Es un rectangulo sobre el que se imprime la imagen del robot
      - imagen    : *pygame.Surface*
      Imagen del robot
      - velocidad : *float*
      Velocidad fija en 0.1, se escala con el metodo set_velocidad
      - direccion : *(int, int)* direccion en la que debe actualizar

    #Metodos
     ------
      + set_posicion(posicion = *(int,int)*)
      Determina la posicion de Icono.rect y de Icono.imagen

      + set_tamano(tamano = *(int,int)*)
      Define el tamano del icono del robot. La unidad de medida son *pixeles*. El input es una tupla (ancho,alto)

      + set_imagen(archivo = *str*)
      Determina la imagen a usar como icono del robot. Debo ingresar un string con la ubicacion y el nombre del archivo.
      Ejemplo: set_imagen("/home/imagenes/robot.png")

      + set_velocidad(velocidad = *float*)
      Le doy un numero que se multiplica por la velocidad que viene por defecto. Es decir, escala la velocidad. Sirve, por ejemplo, para duplicar

      + set_direccion(direccion = *(int, int)*)
      Direccion en la cual se debe mover el icono. valores posibles: (0,1), (-1,0), etc...

      + mover(tiempo = *pygame.time.Clocl().tick(60)*):
      Dada la velocidad y el tiempo definido por *pygame*, realiza el movimiento. Se usa dentro de un LOOP. El resultado es la modificacion de la poscion del icono.

      + get_posicion()
      Devuelve la posicion del iconoselfself.
      OUTPUT: *(int, int)*

    # Funciones
      ---------

      cheaquear_cierre_ventana()
      Si se clickea el boton "x" de la ventana, se detiene el programa y se cierra la ventana.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((1,1),(1,1))
        self.imagen = pygame.image.load('alien.jpeg')
        self.velocidad = 0.1
        self.direccion = (1,0)

    def set_posicion(self, posicion):
        # Se usa para setear posicion inicial del robot
        self.rect.left = posicion[0]
        self.rect.top = posicion[1]

    def set_tamano(self, tamano):
        # setea el tamano de la imagen, en pixeles
        # es conveniente darle como entrada: (PIXEL_size, PIXEL_size)
        imagen = self.imagen.convert_alpha()
        self.imagen = pygame.transform.scale(imagen, tamano)
        self.rect.size = tamano

    def set_imagen(self,archivo):
        # archivo es un string con el nomre de la imagen. ej: /home/robot.jpg
        self.imagen = pygame.image.load(archivo)

    def set_velocidad(self,velocidad):
        # le doy un numero que se multiplica por la velocidad que viene por defecto
        self.velocidad = self.velocidad * velocidad

    def set_direccion(self,direccion):
        # direccion en la cual se debe mover
        # direccion: (int, int)
        # valores posibles: (0,1), (-1,0), etc...
        self.direccion = direccion

    def mover(self, tiempo):
        self.rect.left += self.direccion[0] * self.velocidad * tiempo
        self.rect.top  += self.direccion[1] * self.velocidad * tiempo

    def get_posicion(self):
        # posicion actual
        return (self.rect.left, self.rect.top)
####################### funciones ######################################

def cheaquear_cierre_ventana():
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
    return 0
#######################MAIN######################################
"""
IMPORTANTE:

DE ACA EN ADELANTE, TODO LO QUE ESTA RODEADO DE #### ES PORQUE
NO VA EN EL MAIN POSTA, SINO QUE DEBE SER REEMPLAZADO
"""


from Laberinto import *
from Robot import *
#from Visualizacion import *
import sys
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)

#----------INPUTS---------------------------------------------------------------
dim_x = 30
dim_y = 20

PIXEL_size = 20

velocidad_inicial = 1
#-------------------------------------------------------------------------------

# Definimos algunos colores
#NEGRO = (0, 0, 0)              DESCOMENTAR ESTO EN EL
#BLANCO = (255, 255, 255)       CODIGO FINAL!!!!
########################
BLANCO = (0, 0, 0)     #
NEGRO = (255, 255, 255)#
########################
WIDTH = PIXEL_size * dim_x
HEIGHT = PIXEL_size * dim_y

#----------------------INICIALIZACION DE GRAFICOS-------------------------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
#-------------------------------------------------------------------------------

#----------------------CREACION DEL LABERINTO-----------------------------------
#############################################################################
# invento un mapa random                                                    #
mapa = np.zeros((int(WIDTH/PIXEL_size), int(HEIGHT/PIXEL_size)))            #
mapa[int(100/PIXEL_size):int(301/PIXEL_size),int(100/PIXEL_size)] = 1       #
mapa[int(300/PIXEL_size),int(100/PIXEL_size):int(202/PIXEL_size)] = 1       #
mapa[int(100/PIXEL_size):int(301/PIXEL_size),int(200/PIXEL_size)] = 1       #
#############################################################################
no_ceros = np.nonzero(mapa)
pantalla.fill(BLANCO)
for j in range(len(no_ceros[0])):
    bloque_pos  = (no_ceros[0][j]*PIXEL_size, no_ceros[1][j]*PIXEL_size)
    bloque_size = (PIXEL_size, PIXEL_size)
    bloque = pygame.Rect(bloque_pos, bloque_size)
    pygame.draw.rect(pantalla, NEGRO, bloque)
# guardo el laberinto como una IMAGEN en la variable background
# sirve para imprimir el laberinto
background = pantalla.convert()
#-------------------------------------------------------------------------------

#----------------------CREACION DEL ICONO ROBOT----------------------------------
icono = Icono()
icono.set_imagen("./alien.jpeg")
icono.set_posicion((100,100))
icono.set_tamano((PIXEL_size, PIXEL_size))
icono.set_velocidad(velocidad_inicial)
# esto es: grafica icono.imagen en el rectangulo icono.rect
pantalla.blit(icono.imagen,icono.rect)
pygame.display.flip()
# Espero un segundo antes de arrancar
pygame.time.wait(1000)
#-------------------------------------------------------------------------------

##############invento un movimiento############
nuevo = [(300,100), (300,200), (200,100 )]    #
nueva_dir = [(1,0), (0,1), (-1,0)]            #
i = 0                                         #
###############################################

while True:
    cheaquear_cierre_ventana()
    #########################################
    # ACA VA EL BLOQUE QUE TOMA LA DECISION.#
    # ME DEVUELVE UNA DIRECCION             #
    icono.set_direccion(nueva_dir[i])       # Direccion inventada
    # ME DEVUELVE UNA NUEVA POSICION        #
    new_xy = nuevo[i]                       #
    #########################################
    reloj = pygame.time.Clock()
    posicion = icono.get_posicion()
    condicion = True
    while condicion:
        cheaquear_cierre_ventana()
        tiempo = reloj.tick(60)
        posicion = icono.get_posicion()
        #print(posicion, new_xy)
        #print(tiempo)
        icono.mover(tiempo)
        # para dar efecto de movimiento, debo pisar el grafico anterior
        # es decir, vuelvo a graficar el laberinto y arriba grafico
        # con la nueva posicion
        pantalla.blit(background,[0,0])
        pygame.display.flip()
        pantalla.blit(icono.imagen, icono.rect)
        pygame.display.flip()

        # deja de moverse cuando este a un pixel de distancia. CONDICION CON TOLERANCIA
        # condicion = (posicion[0]-new_xy[0])**2 + (posicion[1]-new_xy[1])**2 > (0.1 * PIXEL_size)**2
        condicion = (posicion != new_xy)
    print(nuevo)

    #########
    i += 1  #
    #########
