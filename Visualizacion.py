# coding=UTF-8
import pygame
from pygame.locals import *
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

class Icono (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('Ada_bot.jpeg')
        self.rect = self.imagen.get_rect()
        self.velocidad = 0.1
        self.direccion = (1,0)
        self.rect.centerx = 100
        self.rect.centery = 100


    def set_imagen(self,archivo):
        self.imagen = pygame.image.load(archivo)

    def set_velocidad(self,velocidad):
        """
        velocidad debe ser un numero (todavia no se de que tipo)
        """
        self.velocidad = velocidad

    def set_direccion(self,direccion):
        """
        Direccion debe ser una tupla de dos elementos,
        """
        self.direccion = direccion

    def get_posicion(self):
        return (self.rect.centerx, self.rect.centery)

    def mover(self, tiempo):
        self.rect.centerx += self.direccion[0] * self.velocidad * tiempo
        self.rect.centery += self.direccion[1] * self.velocidad * tiempo
####################### funciones ######################################

def cheaquear_si_cierro_ventana():
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
    return 0
#######################MAIN######################################

from Laberinto import *
from Obstaculo import *
from Robot import *
#from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)

dim_x = 30
dim_y = 20

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

PIXEL_size = 20
WIDTH = PIXEL_size * dim_x
HEIGHT = PIXEL_size * dim_y

#-------------INICIALIZACION DE GRAFICOS-----------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
reloj = pygame.time.Clock()
#--------------------------------------------------------

######## esto en reliadad se hace con las clases, aca lo invento
# invento un mapa random
mapa= np.random.randint(0,2,(int(WIDTH/PIXEL_size), int(HEIGHT/PIXEL_size)))
###############################################################

no_ceros = np.nonzero(mapa)
pantalla.fill(BLANCO)

for j in range(len(no_ceros[0])):
    pygame.draw.rect(pantalla, NEGRO,[no_ceros[0][j]*PIXEL_size, no_ceros[1][j]*PIXEL_size, PIXEL_size, PIXEL_size] )

background = pantalla.convert()

######cREO EL ICONO Robot
icono = Icono()
icono.set_imagen("./Ada_bot.jpeg")
pantalla.blit(icono.imagen, icono.rect)
pygame.display.flip()
pygame.time.wait(2000)
#######


nuevo = [(300,100), (300,200), (200,100 )]
nueva_dir = [(1,0), (0,1), (-1,0)]
i = 0
while True:
    #for eventos in pygame.event.get():
    #    if eventos.type == QUIT:
    #        sys.exit(0)
    cheaquear_si_cierro_ventana()
    #########################################
    # ACA VA EL BLOQUE QUE TOMA LA DECISION.#
    # ME DEVUELVE UNA DIRECCION             #
    icono.set_direccion(nueva_dir[i])  # Direccion inventada
    print(nueva_dir[i])
    # ME DEVUELVE UNA NUEVA POSICION        #
    new_xy = nuevo[i]                       #
    #########################################
    reloj = pygame.time.Clock()
    posicion = icono.get_posicion()
    print(posicion)
    condicion = True
    while condicion:
    #for i in range(10):
        cheaquear_si_cierro_ventana()
        tiempo = reloj.tick(60)
        posicion = icono.get_posicion()
        #print(posicion, new_xy)
        #print(tiempo)
        icono.mover(tiempo)
        pantalla.blit(background,[0,0])
        pygame.display.flip()
        pantalla.blit(icono.imagen, icono.rect)
        pygame.display.flip()
        condicion = (posicion[0]-new_xy[0])**2 + (posicion[1]-new_xy[1])**2 > PIXEL_size**2
        #print(condicion, icono.direccion)
        #print('------------------')
    print(nuevo)
    i += 1
    print('------------------')
