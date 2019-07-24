# coding=UTF-8
from Robot import *
from Obstaculo import *
import numpy as np
from random import randrange


class Laberinto(object):
    """
    :version: Camino de la Solución. (requisito para que el laberinto tenga solución)
    :author: Lucas Farigliano y Hugo Chanampe
    """

    """ ATTRIBUTES
    size_x  (private)
    size_y  (private)
    ada_boot  (private)
    lista_obstaculos_  (private)
    """
    def __init__(self,dim_x,dim_y):
        self.dim_x=dim_x
        self.dim_y=dim_y
        self.x_ini=0
        self.y_ini=0
        self.mapa= np.ones((self.dim_x+2,self.dim_y+2))

    def generar_solucion(self):
        """
        @return  : el camino solución del laberinto
        @author  Lucas Farigliano

        La matriz parte de todos unos. Y se cambian ceros por uno para
        establecer uno de las soluciones del laberinto. El robot de
        coloca en una posición random para comenzar, y si o si sale por una pared
        les laberinto.
        El contructor va armando el camino sin pisar el camino recorrido, salvo
        que se encuentre en un entorno de (0,0,0,0) entonces sigue con el movimiento que traia
        (testear si esa idea esta bien)
        """
        self.x_ini=randrange(1,self.dim_x)   #posición inicial randon sin contar paredes
        self.y_ini=randrange(1,self.dim_y)
        self.mapa[self.x_ini][self.y_ini]=0
        i=0 #contador de pasos en el while
        x=self.x_ini
        y=self.y_ini
        salida = "false"
        while salida != "true":  # si encuentra alguna pared se termina la creacción del camino
            i+=1
            n=randrange(4) #0=arriba 1=derecha 2=abajo 3=izquierda
            if i<10: # este if es para evitar que encuentre la solución rapido. (se puede mejorar la implementación)
                if n == 0 and (x-1) > 0 and self.mapa[x-1][y]!=0:
                    x -= 1
                if n == 1 and (y+1) < (self.dim_y+1) and self.mapa[x][y+1]!=0:  # el +2 porque el arreglo tiene 2 extras a la dimension por las paredes
                    y += 1
                if n == 2 and (x+1) < (self.dim_x+1) and self.mapa[x+1][y]!=0: # el +2 porque el arreglo tiene 2 extras a la dimension por las paredes
                    x += 1
                if n == 3 and (y-1) > 0 and self.mapa[x][y-1]!=0:
                    y -= 1
                self.mapa[x][y]=0
            else:
                if n == 0 and self.mapa[x-1][y]!=0:
                    x -= 1
                if n == 1 and self.mapa[x][y+1]!=0:
                    y += 1
                if n == 2 and self.mapa[x+1][y]!=0:
                    x += 1
                if n == 3 and self.mapa[x][y-1]!=0:
                    y -= 1
                self.mapa[x][y]=0
            #el if siguiente hace que si el sistema se encuentra en un entorno de ceros siga por donde vino
            if self.mapa[x-1][y]==0 and  self.mapa[x][y+1]==0 and self.mapa[x+1][y]==0 and self.mapa[x][y-1]==0:
                if n == 0:
                    x -= 1
                if n == 1:
                    y += 1
                if n == 2:
                    x += 1
                if n == 3:
                    y -= 1
            if x==0:     #Evaluar las condiciones para encontrar la salida (capaz que convenga crear un nuevo metodo para esto)
                salida="true"
            elif x ==(self.dim_x+1):
                salida="true"
            elif y==0:
                salida="true"
            elif y ==(self.dim_y+1):
                salida="true"
    def generar_obstaculos(self):
        """
        @return  :
        @author
        """
        pass

    def generar_ada(self, ada_robot):
        """
        @param Robot ada_robot :
        @return  :
        @author
        """
        pass

    def actualizar_laberinto(self, x, y):
        """
        @param int x :
        @param int y :
        @return  :
        @author
        """
        pass

        '''
        laberinto debe tener get_neighbor_map (devuelve lista de 4 0 o 1)

        '''
