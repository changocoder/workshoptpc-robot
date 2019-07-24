# coding=UTF-8
from Laberinto import *
"""
probando hacer un commit
"""

class Visualizacion(object):

  """


  :version:
  :author:
  """

  """ ATTRIBUTES



  laberinto  (private)

  """

  def graficar(self):
    """


    @return  :
    @author
    """
    pass

#######################MAIN######################################

from Laberinto import *
from Obstaculo import *
from Robot import *
#from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)


dim_x = 50
dim_y = 50

laberinto = Laberinto(dim_x, dim_y)
laberinto.generar_solucion()
mapa = laberinto.mapa


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)


PIXEL_size = 50
WIDTH = 1000
HEIGHT = 1000

#-------------INICIALIZACION DE GRAFICOS-----------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
reloj = pygame.time.Clock()
#--------------------------------------------------------

no_ceros = np.nonzero(mapa)
pantalla.fill(BLANCO)


for j in range(len(no_ceros[0])):
    pygame.draw.rect(pantalla, NEGRO,[no_ceros[0][j]*PIXEL_size, no_ceros[1][j]*PIXEL_size, PIXEL_size, PIXEL_size] )

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)

    pygame.display.flip()
