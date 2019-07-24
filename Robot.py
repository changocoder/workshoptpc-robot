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

    #sensar is setter
    def sensar(self, sensor):
    
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
            if(sensor_left != 0):
                #self.dirección = self.direccion
                pass
            
        else:
            if(sensor_left == 0):
                """permutación cíclica en dirección , mover el 1 al indice anterior al que está
                moverse hacia la izquierda
                """
                self.direccion = turn_left(self.direccion)

            elif(sensor_left != 0):
                if (sensor_right == 0):
                    """
                    moverse hacia la derecha
                    permutación cíclica en dirección , mover el 1 al indice j-3
                    """
                    self.direccion = turn_right(self.direccion)
                
                elif(sensor_right != 0):
                    """
                    moverse hacia atrás 
                    permutación cíclica en dirección, mover el 1 al índice j-2
                    """
                    self.direccion = turn_back(self.direccion)

#---------------------------------------------------------------------------------------------------
#------------------------------------FUNCIONES------------------------------------------------------


def turn_right(direccion):
    """
    turn_right(direccion):
        Toma la lista direccion y hace una permutacion ciclica de manera
        que la nueva direccion sea hacia la derecha de la direccion anterior

        INPUT:
        direccion: lista de 4 elementos (CEROS O UNOS)

        OUTPUT:
        lista de 4 elementos

        lo mismo para turn_back y turn_left
    """
    return [direccion[i-1] for i in range(len(direccion))]

def turn_back(direccion):
    return [direccion[i-2] for i in range(len(direccion))]

def turn_left(direccion):
    return [direccion[i-3] for i in range(len(direccion))]

#MAIN BORRADOR: PASAR A SANTI
"""
if __name__ == "__main__":
    ada_bot = Robot()
    laberinto = Laberinto()
    
    
    
    """Primer sensado para ada_BOT 
    sensor = laberinto.get_vecinos()"""
    
    ada_bot.sensar(laberinto.get_vecinos())
    
    
    """index devuelve el primer lugar en lista del objeto que busco"""
    first_front = ada_bot.slabyrinthnsor.index(0)
    
    ada_bot.direccion[first_front] = 1
    
    print(ada_bot.direccion)
    
    ada_bot.seguir_pared()
"""    
