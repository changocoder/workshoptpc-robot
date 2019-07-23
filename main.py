from Laberinto import *
from Obstaculo import *
from Robot import *
from Visualizacion import *

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

WIDTH = 1000
HEIGHT = 1000
nn = 10.0

#-------------INICIALIZACION DE GRAFICOS-----------------
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
reloj = pygame.time.Clock()
#--------------------------------------------------------

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
    #pygame.draw.rect(pantalla, VERDE,[ 500, -int(reloj.get_time()/1000.0) , nn*10, nn*10] )
