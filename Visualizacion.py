# coding=UTF-8
import pygame
from pygame.locals import *
from Laberinto import *
class Icono (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((1,1),(1,1))
        self.imagen = pygame.image.load('alien.jpeg')
        self.velocidad = 0.1
        self.direccion = (1,0)

    def set_posicion(self, posicion):
        self.rect.left = posicion[0]
        self.rect.top = posicion[1]

    def set_tamano(self, tamano):
        """
        #Metodo
         ------
        set_tamano(tamano = *tuple* 2x1)

          Define el tamano del icono del robot. La unidad de medida son *pixeles*.
        El input es una tupla (ancho,alto)
        """
        imagen = self.imagen.convert_alpha()
        self.imagen = pygame.transform.scale(imagen, tamano)
        self.rect.size = tamano

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
        return (self.rect.left, self.rect.top)

    def mover(self, tiempo):
        self.rect.centerx += self.direccion[0] * self.velocidad * tiempo
        self.rect.centery += self.direccion[1] * self.velocidad * tiempo
####################### funciones ######################################

def cheaquear_cierre_ventana():
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
    return 0
#######################MAIN######################################

from Laberinto import *
from Robot import *
#from Visualizacion import *
import sys
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)

dim_x = 30
dim_y = 20

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

PIXEL_size = 20
WIDTH = PIXEL_size * dim_x
HEIGHT = PIXEL_size * dim_y

#----------------------INICIALIZACION DE GRAFICOS-------------------------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
reloj = pygame.time.Clock()
#-------------------------------------------------------------------------------

#----------------------CREACION DEL LABERINTO-----------------------------------
#############################################################################
# invento un mapa random                                                    #
#mapa= np.random.randint(0,2,(int(WIDTH/PIXEL_size), int(HEIGHT/PIXEL_size)))#
mapa = np.zeros((int(WIDTH/PIXEL_size), int(HEIGHT/PIXEL_size)))
mapa[int(100/PIXEL_size):int(300/PIXEL_size),int(100/PIXEL_size)] = 1
#############################################################################
no_ceros = np.nonzero(mapa)
pantalla.fill(BLANCO)
for j in range(len(no_ceros[0])):
    pygame.draw.rect(pantalla, NEGRO,[no_ceros[0][j]*PIXEL_size, no_ceros[1][j]*PIXEL_size, PIXEL_size, PIXEL_size] )
# guardo el laberinto como una IMAGEN en la variable background
# sirve para imprimir el laberinto
background = pantalla.convert()
#-------------------------------------------------------------------------------

#----------------------CREACION DEL ICONO ROBOT----------------------------------
icono = Icono()
icono.set_imagen("./alien.jpeg")
icono.set_posicion((100,100))
icono.set_tamano((PIXEL_size, PIXEL_size))
print(icono.rect, icono.get_posicion())
pantalla.blit(icono.imagen,icono.rect)
pygame.display.flip()
# Espero un segundo antes de arrancar
pygame.time.wait(1000)
#-------------------------------------------------------------------------------


nuevo = [(300,100), (300,200), (200,100 )]
nueva_dir = [(1,0), (0,1), (-1,0)]
i = 0
while True:
    cheaquear_cierre_ventana()
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
        cheaquear_cierre_ventana()
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
