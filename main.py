from Laberinto import *
from Obstaculo import *
from Robot import *
from Visualizacion import *
<<<<<<< HEAD
=======
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)


dim_x = 50
dim_y = 50

laberinto = Laberinto(dim_x, dim_y)
laberinto.generar_solucion()
mapa = laberinto.mapa

>>>>>>> Laberinto

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

<<<<<<< HEAD
WIDTH = 1000
HEIGHT = 1000
nn = 10.0
=======

PIXEL_size = 10
WIDTH = dim_x*PIXEL_size
HEIGHT = dim_y*PIXEL_size
>>>>>>> Laberinto

#-------------INICIALIZACION DE GRAFICOS-----------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
reloj = pygame.time.Clock()
#--------------------------------------------------------

<<<<<<< HEAD
'''
Aca defini una matriz para probar, pero en un futuro esa es la matriz
del laberinto. Lo que hace esta seccion es encontrar los indices no nulos
y crear una ventana. en este ejemplo, como no tenia indices no nulos, use
un condicional, pero cuando tenga todo, seria:

matriz = laberinto.mapa_laberinto_
no_ceros = np.nonzero(matriz)
'''
matriz = np.random.rand(WIDTH/nn, HEIGHT/nn)
no_ceros = np.where(matriz<0.5)
pantalla.fill(BLANCO)


for j in range(len(no_ceros[0])):
    pygame.draw.rect(pantalla, NEGRO,[no_ceros[0][j]*nn, no_ceros[1][j]*nn, nn, nn] )

while True:
    #______creacion del grafico:
    #dibujo=pygame.image.load("game.png").convert()
    #pantalla.blit(dibujo,[0,0]) #segundo argumento: posicion
    pygame.display.flip()
    reloj.tick()
=======
matriz = np.random.rand(WIDTH/PIXEL_size, HEIGHT/PIXEL_size)
#no_ceros = np.where(matriz<0.5)
mapa_unos = np.where(mapa==1)
pantalla.fill(BLANCO)

for j in range(len(mapa_unos[0])):
    pygame.draw.rect(pantalla, NEGRO,[mapa_unos[0][j]*PIXEL_size, mapa_unos[1][j]*PIXEL_size, PIXEL_size, PIXEL_size] )
c=pygame.PixelArray(pantalla)

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)

    pygame.display.flip()
>>>>>>> Laberinto
    #pygame.draw.rect(pantalla, VERDE,[ 500, -int(reloj.get_time()/1000.0) , nn*10, nn*10] )
