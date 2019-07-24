from Laberinto import *
from Obstaculo import *
from Robot import *
from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)


dim_x = 10
dim_y = 10

laberinto = Laberinto(dim_x, dim_y)
laberinto.generar_solucion()
mapa = laberinto.mapa


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)


PIXEL_size = 50
WIDTH = 500
HEIGHT = 500
#WIDTH = dim_x*PIXEL_size
#HEIGHT = dim_y*PIXEL_size

#-------------INICIALIZACION DE GRAFICOS-----------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
reloj = pygame.time.Clock()
#--------------------------------------------------------

#no_ceros = np.where(matriz<0.5)
mapa_unos = np.where(mapa==1)
#pantalla.fill(BLANCO)

for j in range(len(mapa_unos[0])):
    pygame.draw.rect(pantalla, VERDE,[mapa_unos[0][j]*PIXEL_size, mapa_unos[1][j]*PIXEL_size, PIXEL_size, PIXEL_size] )
#c=pygame.PixelArray(pantalla)

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)

    pygame.display.flip()
    #pygame.draw.rect(pantalla, VERDE,[ 500, -int(reloj.get_time()/1000.0) , nn*10, nn*10] )
