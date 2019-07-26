# coding=UTF-8
import pygame, sys
from pygame.locals import *
from Laberinto import *

class Icono (pygame.sprite.Sprite):
    """
    @author  Santiago Maldonado Ochoa
    ## Class Icono(pygame.sprite.Sprite)
    #Atributos
     ---------
      - rect      : *pygame.Rect*
      Es un rectangulo sobre el que se imprime la imagen del robot
      - imagen    : *pygame.Surface*
      Imagen del robot
      - velocidad : *float*
      Velocidad fija en 0.1, se escala con el metodo set_velocidad
      - direccion : *(int, int)* direccion en la que debe actualizar

    #Metodos
     ------
      + set_posicion(posicion = *(int,int)*)
      Determina la posicion de Icono.rect y de Icono.imagen

      + set_tamano(tamano = *(int,int)*)
      Define el tamano del icono del robot. La unidad de medida son *pixeles*. El input es una tupla (ancho,alto)

      + set_imagen(archivo = *str*)
      Determina la imagen a usar como icono del robot. Debo ingresar un string con la ubicacion y el nombre del archivo.
      Ejemplo: set_imagen("/home/imagenes/robot.png")

      + set_velocidad(velocidad = *float*)
      Le doy un numero que se multiplica por la velocidad que viene por defecto. Es decir, escala la velocidad. Sirve, por ejemplo, para duplicar

      + set_direccion(direccion = *(int, int)*)
      Direccion en la cual se debe mover el icono. valores posibles: (0,1), (-1,0), etc...

      + mover(tiempo = *pygame.time.Clocl().tick(60)*):
      Dada la velocidad y el tiempo definido por *pygame*, realiza el movimiento. Se usa dentro de un LOOP. El resultado es la modificacion de la poscion del icono.

      + get_posicion()
      Devuelve la posicion del iconoselfself.
      OUTPUT: *(int, int)*

    # Funciones
      ---------

      cheaquear_cierre_ventana()
      Si se clickea el boton "x" de la ventana, se detiene el programa y se cierra la ventana.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pixelSize = 20
        self.rect = pygame.Rect((1,1),(1,1))
        self.imagen = pygame.image.load('alien.jpeg')
        self.velocidad = 1
        self.direccion = (1,0)

    def set_pixelSize(self, pixelSize):
        # pixelSize = int
        self.pixelSize = pixelSize

    def set_posicion(self, posicion):
        # Se usa para setear posicion inicial del robot
        self.rect.left = posicion[1] * self.pixelSize
        self.rect.top = posicion[0] * self.pixelSize

    def set_tamano(self, tamano):
        # setea el tamano de la imagen, en pixeles
        # es conveniente darle como entrada: (pixelSize, pixelSize)
        imagen = self.imagen.convert_alpha()
        self.imagen = pygame.transform.scale(imagen, tamano)
        self.rect.size = tamano

    def set_imagen(self,archivo):
        BLANCO = [255, 255, 255]
        # archivo es un string con el nomre de la imagen. ej: /home/robot.jpg
        self.imagen = pygame.image.load(archivo)
        self.imagen.set_colorkey(BLANCO)

    def set_velocidad(self,velocidad):
        # le doy un numero que se multiplica por la velocidad que viene por defecto
        self.velocidad = self.velocidad * velocidad

    def set_direccion(self,n):
        # direccion en la cual se debe mover
        # direccion: (int, int)
        # valores posibles: (0,1), (-1,0), etc...
        if n==0:
            self.direccion = (-1,0)
        if n==1:
            self.direccion = (0,1)
        if n==2:
            self.direccion = (1,0)
        if n==3:
            self.direccion = (0,-1)

    def mover(self, tiempo):
        self.rect.left += self.direccion[0] * self.velocidad * tiempo
        self.rect.top  += self.direccion[1] * self.velocidad * tiempo

    def get_posicion(self):
        # posicion actual
        return (self.rect.left, self.rect.top)

    def condicion(self):
        pass

####################### funciones ######################################
def cheaquear_cierre_ventana():
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
    return 0
#######################MAIN######################################
