from Laberinto import *
from Obstaculo import *
from Robot import *
#from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)

#-------------------INPUTS------------------------------------------------------
dim_x = 10
dim_y = 10

pixelSize = 20
velocidad_inicial = 1
BLANCO = (0, 0, 0)
NEGRO = (255, 255, 255)
#-------------------------------------------------------------------------------

ada_bot = Robot()
laberinto = Laberinto(dim_x,dim_y)
#Construir el laberinto
laberinto.generar_obstaculos()
laberinto.generar_ada(ada_bot)

#----------------------INICIALIZACION DE GRAFICOS-------------------------------
WIDTH = pixelSize * dim_x
HEIGHT = pixelSize * dim_y
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
#-------------------------------------------------------------------------------

print ("lala\n",laberinto.mapa)
sensor = laberinto.get_vecinos()
ada_bot.set_sensor(sensor)
first_front=sensor.index(0)
ada_bot.direccion[first_front] = 1
print(ada_bot.direccion)
print(sensor)
# Primer paso
while np.count_nonzero(sensor)==0:
    ada_bot.set_sensor(sensor)
    first_front=sensor.index(0)
    ada_bot.direccion[first_front] = 1
    laberinto.actualizar_laberinto(first_front)
    print ("inicial\n",laberinto.mapa)
    sensor = laberinto.get_vecinos()
    print(sensor)
if sensor[0]==1:
    ada_bot.turn_right()
elif sensor[1]==1:
    ada_bot.turn_back()
print(ada_bot.direccion)

salida = "false"
while salida != "true":  # si encuentra alguna pared se termina la creacción del camino
    sensor = laberinto.get_vecinos()
    print(sensor)
    ada_bot.set_sensor(sensor)
    #index devuelve el primer lugar en lista del objeto que busco
    print ("adaantes\n",ada_bot.direccion)
    ada_bot.seguir_pared()
    direccion=ada_bot.get_direccion()
    n=direccion.index(1)
    print ("adadespues\n",ada_bot.direccion)
    laberinto.actualizar_laberinto(n)
    print ("segpaso\n",laberinto.mapa)
    salida=laberinto.controlar_escape()
