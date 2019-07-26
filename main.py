from Laberinto import *
from Robot import *
from Visualizacion import *
import pygame, sys
from pygame.locals import *
#Importo asi para usar pygame.event (https://www.pygame.org/docs/ref/locals.html)

#-------------------INPUTS------------------------------------------------------
dim_x = 10
dim_y = 10

pixelSize = 50
velocidad_inicial = 0.1
BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
#-------------------------------------------------------------------------------
ada_bot = Robot()
laberinto = Laberinto(dim_x,dim_y)
#Construir el laberinto
laberinto.generar_obstaculos()
laberinto.generar_ada(ada_bot)
#----------------------INICIALIZACION DE GRAFICOS-------------------------------
WIDTH = pixelSize * (dim_x+2)
HEIGHT = pixelSize * (dim_y+2)
pygame.init()
pantalla = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Ada-BOT Maze")
#-------------------------------------------------------------------------------


#----------------------Visualizacion DEL LABERINTO------------------------------
# imagen de fondo
fondo = Icono()
fondo.set_imagen('space.png')
fondo.set_tamano((WIDTH, HEIGHT))
pantalla.blit(fondo.imagen, (0,0))


# imagen para los bloques
metal = Icono()
metal.set_imagen('metal.jpg')
metal.set_tamano((pixelSize, pixelSize))

unos_mapa = np.where(laberinto.mapa == 1)
for j in range(len(unos_mapa[0])):
    bloque_pos  = (unos_mapa[1][j]*pixelSize, unos_mapa[0][j]*pixelSize)
    bloque_size = (pixelSize, pixelSize)
    bloque = pygame.Rect(bloque_pos, bloque_size)
    #pygame.draw.rect(pantalla, BLANCO, bloque)
    pantalla.blit(metal.imagen, bloque)
#pinto el inicio
nave = Icono()
nave.set_imagen('nave.png')
nave.set_tamano((pixelSize, pixelSize))
inicio_pos  = (laberinto.y_ini*pixelSize, laberinto.x_ini*pixelSize)
inicio = pygame.Rect(inicio_pos, bloque_size)
pantalla.blit(nave.imagen, inicio)
#fin_pos  = (laberinto.y_ini*pixelSize, laberinto._ini*pixelSize)
#fin = pygame.Rect(fin_pos, bloque_size)
#pygame.draw.rect(pantalla, [0, 255, 0], fin)

# guardo el laberinto como una IMAGEN en la variable background
# sirve para imprimir el laberinto
background = pantalla.convert()
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


#----------------------CREACION DEL ICONO ROBOT----------------------------------
icono = Icono()
icono.set_imagen("./Ada_bot.png")
icono.set_pixelSize(pixelSize)
icono.set_posicion((laberinto.pos_robot_x,laberinto.pos_robot_y))
icono.set_tamano((pixelSize, pixelSize))
icono.set_velocidad(velocidad_inicial)

pantalla.blit(icono.imagen, icono.rect)
pygame.display.flip()

# esto es: grafica icono.imagen en el rectangulo icono.rect
#pantalla.blit(icono.imagen,icono.rect)
#pygame.display.flip()
# Espero un segundo antes de arrancar
pygame.time.wait(500)
#-------------------------------------------------------------------------------
posicion = (laberinto.pos_robot_x*pixelSize, laberinto.pos_robot_y*pixelSize)
salida = "false"
while salida != "true":  # si encuentra alguna pared se termina la creacción del camino
    cheaquear_cierre_ventana()
    sensor = laberinto.get_vecinos()
    print(sensor)
    ada_bot.set_sensor(sensor)
    #index devuelve el primer lugar en lista del objeto que busco
    print ("adaantes\n",ada_bot.direccion)
    ada_bot.seguir_pared()
    direccion=ada_bot.get_direccion()
    n = direccion.index(1)
    print ("adadespues\n",ada_bot.direccion)
    laberinto.actualizar_laberinto(n)
    print ("segpaso\n",laberinto.mapa)

    # Visualizacion:
    #icono.set_direccion(n)
    new_xy = (laberinto.pos_robot_x, laberinto.pos_robot_y)
    #reloj = pygame.time.Clock()
    print(posicion, new_xy, icono.direccion)
    """
    # saco lo que se ve "continuo"
    while icono.condicion:
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
    print(posicion, new_xy)
    icono.set_posicion(new_xy)
    # para dar efecto de movimiento, debo pisar el grafico anterior
    # es decir, vuelvo a graficar el laberinto y arriba grafico
    # con la nueva posicion
    pantalla.blit(background,[0,0])
    pygame.display.flip()
    pantalla.blit(icono.imagen, icono.rect)
    pygame.display.flip()
    pygame.time.wait(300)
    salida=laberinto.controlar_escape()


pantalla.blit(background,[0,0])
pygame.display.flip()
pantalla.blit(icono.imagen, icono.rect)
pygame.display.flip()


print("SALIO!")
while True:
    cheaquear_cierre_ventana()

#carImg = pygame.image.load('imagen_ginal.png')
