#!/usr/bin/python

#-*-coding:utf-8 -*-

"""encabezado obligatorio para Ada, no estoy segura por qué
"""

import numpy as np

from Laberinto import *

class Robot(object):

    """
    :version:
    #no se que va aca
    :author:
    #tampoco aca
    """

    """ ATTRIBUTES
    position  (private)
    """

    """     """

    def __init__(self):
        #position: inicio (origen de coordenadas para Ava)
        """sensor
        """
        self.sensor=[0, 0 ,0 ,0]
        self.direccion= [0, 0, 0, 0]
        #int: velocidad = 0
        self.velocidad= 0
        self.esquina_atras_izquierda= 0


    def set_sensor(self, sensor):
        """
        la variable sensor es tipo lista de 4 elementos: [ , , , ] y
        toma su valor del método get_vecinos de Laberinto

        @return  :
        @author
        """

        self.sensor= sensor

    def set_direccion(self, direccion):
        """
        direccion =  [arriba, derecha, abajo , izquierda]  indica hacia donde se va a mover el robot
        comienza con None y el main produce el cambio
        @return  :
        @author
        """
        self.direccion = direccion


    def set_velocidad(self):

        pass
    
    def buscar_pared(self, direccion, esquina_atras_izquierda):
        """Si siguiendo la pared quedo rodeada de ceros entonces buscar pared
        """
        if(self.esquina_atras_izquierda == 0):
            #primer paso rodeada de super ceros metele derecho
            self.buscar_pared(self.direccion)
            
        else:
            #ya tengo un frente
            self.turn_left(self.direccion)
            
        

    def seguir_pared(self):
        """
        Toma de desiciones para salir del laberinto: algoritmo wall follow
        @return  :
        @author

        """
        j = np.nonzero(self.direccion)[0][0]
        sensor_front = self.sensor[j]
        sensor_left = self.sensor[j-1]
        sensor_right = self.sensor[j-3]

        #caso que sigue de largo, ya tengo una dirección
        if (sensor_front == 0):
            
            if(sensor_left != 0):
                #este pass stands for "seguir por donde venía"
                #self.dirección = self.direccion
                pass    
            else:
                self.turn_left()

        else:
            
            if(sensor_left == 0):
                
                """permutación cíclica en el atributo dirección, mover el 1 al
                indice anterior al que está moverse hacia la izquierda
                """
                self.turn_left()

            else:
                
                if (sensor_right == 0):
                    
                    """
                    moverse hacia la derecha
                    permutación cíclica en dirección , mover el 1 al indice j-3
                    """
                    self.turn_right()

                else:
                    
                    """
                    moverse hacia atrás
                    permutación cíclica en dirección, mover el 1 al índice j-2
                    """
                    self.turn_back()


    def turn_right(self):
        """
        turn_right(direccion):
            Toma la lista dirección y hace una permutacion cíclica de manera
            que la nueva dirección sea hacia la derecha de la dirección anterior

            INPUT:
            direccion: lista de 4 elementos (CEROS O UNOS)

            OUTPUT:
            lista de 4 elementos

            lo mismo para turn_back y turn_left
        """
        direccion = self.direccion
        self.direccion = [direccion[i-1] for i in range(len(direccion))]

    def turn_back(self):
        direccion = self.direccion
        self.direccion = [direccion[i-2] for i in range(len(direccion))]

    def turn_left(self):
        direccion = self.direccion
        self.direccion = [direccion[i-3] for i in range(len(direccion))]

    def get_direccion(self):
        return self.direccion
