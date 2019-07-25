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

    def set_sensar(self, sensor):
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
            print("primero")
            if(sensor_left != 0):
                #este pass stands for "seguir por donde venía"
                #self.dirección = self.direccion
                print("segundo")
        else:
            print("ptercero")
            if(sensor_left == 0):
                print("cuarto")
                """permutación cíclica en el atributo dirección, mover el 1 al
                indice anterior al que está moverse hacia la izquierda
                """
                self.direccion = turn_left(self.direccion)

            else:
                print("quinto")
                if (sensor_right == 0):
                    print("sexto")
                    """
                    moverse hacia la derecha
                    permutación cíclica en dirección , mover el 1 al indice j-3
                    """
                    self.direccion = turn_right(self.direccion)

                else:
                    print("fuck_it")
                    """
                    moverse hacia atrás
                    permutación cíclica en dirección, mover el 1 al índice j-2
                    """
                    self.direccion = turn_back(self.direccion)

        print("self.direccion: ", self.direccion)

    def turn_right(self, direccion):
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
        return [direccion[i-1] for i in range(len(direccion))]

    def turn_back(self, direccion):
        return [direccion[i-2] for i in range(len(direccion))]

    def turn_left(self, direccion):
        return [direccion[i-3] for i in range(len(direccion))]
