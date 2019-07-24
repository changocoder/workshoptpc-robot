from Laberinto import *
from Obstaculo import *
from Robot import *
from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)
if __name__ == "__main__":
    ada_bot = Robot()
    laberinto = Laberinto(10,10)

laberinto.generar_obstaculos()
laberinto.generar_ada(ada_bot)
#Primer sensado para ada_BOT
sensor = laberinto.get_vecinos()
print(sensor)
print (laberinto.mapa)
ada_bot.sensar(sensor)
#index devuelve el primer lugar en lista del objeto que busco
first_front=sensor.index(0)
ada_bot.direccion[first_front] = 1
print(ada_bot.direccion)
ada_bot.seguir_pared()

'''    
  
'''                       
'''
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
'''    
