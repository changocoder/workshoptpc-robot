from Laberinto import *
from Obstaculo import *
from Robot import *
from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)


#+++++++++++++++++++++ CREACION LABERINTO ++++++++++++++++++++++++++++++++++++++
dim_x = 10
dim_y = 10
laberinto = Laberinto(dim_x,dim_y)
laberinto.generar_obstaculos()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++ CREACION ROBOT ++++++++++++++++++++++++++++++++++++++++++
ada_bot = Robot()
laberinto.generar_ada(ada_bot)
sensor = laberinto.get_vecinos()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++ INICIO VENTANA ++++++++++++++++++++++++++++++++++++++++++
# creacion de pantalla: MAPA e ICONO
# INPUTS
pixelSize = 30
velocidad_inicial = 1
WIDTH = pixelSize * dim_x
HEIGHT = pixelSize * dim_y
# inicializo graficos
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
# CREACION INICIAL DEL GRAFICO DEL MAPA, y lo guardo para regraficar
background = crear_visualizacion_mapa(pantalla, laberinto, pixelSize)
visualizar_mapa(pantalla, background)

# CRECION DEL ICONO
icono = Icono()
icono.set_posicion((laberinto.y_ini,laberinto.x_ini))
icono.set_tamano((pixelSize, pixelSize))
icono.set_velocidad(velocidad_inicial)
# esto es: grafica icono.imagen en el rectangulo icono.rect
pantalla.blit(icono.imagen,icono.rect)
pygame.display.flip()
# Espero un segundo antes de arrancar
pygame.time.wait(1000)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# LOOP PRINCIPAL:
while True:
    cheaquear_cierre_ventana()
    #########################################
    # ACA VA EL BLOQUE QUE TOMA LA DECISION.#
    # ME DEVUELVE UNA DIRECCION             #
    icono.set_direccion((0,1))      # Direccion inventada
    # ME DEVUELVE UNA NUEVA POSICION        #
    new_xy = (6,6)                       #
    #########################################
    new_xy = (new_xy[0]*pixelSize, new_xy[1]*pixelSize)
    posicion = icono.get_posicion()
    reloj = pygame.time.Clock()
    """
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
    """
##fin-SANTI######################################################################
##fin-SANTI######################################################################
##fin-SANTI######################################################################


# BUSCAR PARED
while np.count_nonzero(sensor)==0:
    ada_bot.set_sensor(sensor)
    first_front=sensor.index(0)
    laberinto.actualizar_laberinto(first_front)
    print ("inicial\n",laberinto.mapa)
    sensor = laberinto.get_vecinos()
    print(sensor)
