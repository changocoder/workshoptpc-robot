# coding=UTF-8
import pygame, sys
from pygame.locals import *
from Laberinto import *


class Visualizacion(object):

    def __init__(self, pixelSize):
        self.pixelSize = pixelSize
        self.icono = pygame.Surface((1,1))
        self.laberinto = laberinto
        self.pantalla= pygame.Surface((1,1))
        self.background = self.pantalla.convert()

    def inicializar_visualizacion(self, dim_x, dim_y):
        WIDTH = dim_x * self.pixelSize
        HEIGHT = dim_y * self.pixelSize
        pygame.init()
        self.pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Ada-BOT Maze")

    def crear_visualizacion_mapa(self):
        """
        INPUT:
          pantalla  : objeto de clase pygame.Surface()
          laberinto : objeto de clase Laberinto()
          pixelSize : int

        OUTPUT:
          imagen de background : objeto de clase pygame.Surface.convert()
        """
        NEGRO = (0, 0, 0)
        BLANCO = (255, 255, 255)
        unos_mapa = np.where(laberinto.mapa == 1)
        pantalla.fill(BLANCO)
        for j in range(len(unos_mapa[0])):
            bloque_pos  = (unos_mapa[0][j]*self.pixelSize, unos_mapa[1][j]*self.pixelSize)
            bloque_size = (pixelSize, pixelSize)
            bloque = pygame.Rect(bloque_pos, bloque_size)
            pygame.draw.rect(pantalla, NEGRO, bloque)
        # guardo el laberinto como una IMAGEN en la variable background
        # sirve para imprimir el laberinto
        self.background = pantalla.convert()

        def visualizar_mapa(self):
            self.pantalla.blit(self.background,[0,0])

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


from icono import *
from Laberinto import *
from Robot import *
#from Visualizacion import *
import sys
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)

#----------INPUTS---------------------------------------------------------------
dim_x = 30
dim_y = 20

pixelSize = 20

velocidad_inicial = 1
#-------------------------------------------------------------------------------

# Definimos algunos colores
#NEGRO = (0, 0, 0)              DESCOMENTAR ESTO EN EL
#BLANCO = (255, 255, 255)       CODIGO FINAL!!!!
########################
BLANCO = (0, 0, 0)     #
NEGRO = (255, 255, 255)#
########################
WIDTH = pixelSize * dim_x
HEIGHT = pixelSize * dim_y

#----------------------INICIALIZACION DE GRAFICOS-------------------------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
#-------------------------------------------------------------------------------

#----------------------CREACION DEL LABERINTO-----------------------------------
#############################################
# invento un mapa random                    #
mapa = np.zeros((dim_y, dim_x))             #
mapa[5:16,3] = 1                            #
mapa[15,3:11] = 1                           #
mapa[5:16,10] = 1                           #
#############################################
no_ceros = np.nonzero(mapa)
pantalla.fill(BLANCO)
for j in range(len(no_ceros[0])):
    bloque_pos  = (no_ceros[0][j]*pixelSize, no_ceros[1][j]*pixelSize)
    bloque_size = (pixelSize, pixelSize)
    bloque = pygame.Rect(bloque_pos, bloque_size)
    pygame.draw.rect(pantalla, NEGRO, bloque)
# guardo el laberinto como una IMAGEN en la variable background
# sirve para imprimir el laberinto
background = pantalla.convert()
#-------------------------------------------------------------------------------

#----------------------CREACION DEL ICONO ROBOT----------------------------------
icono = Icono()
icono.set_imagen("./alien.jpeg")
icono.set_posicion((5,3))
icono.set_tamano((pixelSize, pixelSize))
icono.set_velocidad(velocidad_inicial)
# esto es: grafica icono.imagen en el rectangulo icono.rect
pantalla.blit(icono.imagen,icono.rect)
pygame.display.flip()
# Espero un segundo antes de arrancar
pygame.time.wait(1000)
#-------------------------------------------------------------------------------

##############invento un movimiento############
nuevo = [(15,3), (15,10), (5,10)]    #
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
    new_xy = (new_xy[0]*pixelSize, new_xy[1]*pixelSize)
    posicion = icono.get_posicion()
    reloj = pygame.time.Clock()
    while posicion != new_xy:
        cheaquear_cierre_ventana()
        tiempo = reloj.tick(60)
        #print(posicion, new_xy)
        #print(tiempo)
        icono.mover(tiempo)
        posicion = icono.get_posicion()
        # para dar efecto de movimiento, debo pisar el grafico anterior
        # es decir, vuelvo a graficar el laberinto y arriba grafico
        # con la nueva posicion
        pantalla.blit(background,[0,0])
        pygame.display.flip()
        pantalla.blit(icono.imagen, icono.rect)
        pygame.display.flip()

    #########
    i += 1  #
    #########
"""
