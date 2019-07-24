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
        self.vecinos=np.full(4,5)
        self.mapa = np.full((self.dim_x + 2, self.dim_y + 2), 2)

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
    
    def get_vecinos(self):
        """
        @return:return la lista de vecinos actualizada para que el robot sepa que tiene en su entorno 
        @author: Lucas Farigliano
        Busca la ubicación del robot y devuelve los cuatro vecinos, hay que controlar que pasa cuendo el 
        robot esta en la salida, porque un vecino saldria del arreglo
        """
        pos_robot=list(zip(np.where(self.mapa==3))) #Busca en el mapa donde esta el robot y lo mete en una lista
        pos_robot_x= pos_robot[0][0][0]
        pos_robot_y= pos_robot[1][0][0]
        n_0=self.mapa[pos_robot_x-1][pos_robot_y]
        n_1=self.mapa[pos_robot_x][pos_robot_y+1]
        n_2=self.mapa[pos_robot_x+1][pos_robot_y]
        n_3=self.mapa[pos_robot_x][pos_robot_y-1]
        self.vecinos[0]=n_0
        self.vecinos[1]=n_1
        self.vecinos[2]=n_2
        self.vecinos[3]=n_3

        return self.vecinos


    def generar_obstaculos(self):
        """
        @return  :
        @author
        """
        """
        @return  :
        @author Hugo Chanampe
        codificacion del mapa
        
        0 - solucion
        1 - pared
        2 - obstaculos
        
        
        """
        x = self.dim_x + 2
        y = self.dim_y + 2

        """
        se establecen las paredes de los bordes de la matriz, seteando estos en 1
        """        
        self.mapa[0,:] = 1
        self.mapa[:,0] = 1
        self.mapa[(self.dim_x+1),:] = 1
        self.mapa[:,(self.dim_y+1)] = 1
       
        """ Se genera la solucion del laberinto, invocando el metodo generar_solucion """
        self.generar_solucion()
        
        """ se rellena el resto del array"""
        np.place(self.mapa, self.mapa==2, np.arange(0,2))
        #cantidad_obstaculos = np.count_nonzero(self.mapa==2)
        
        
        #it = np.nditer(self.mapa, flags=['multi_index'], op_flags=['writeonly'])
        #while not it.finished:
        #    print("%d <%d>" % (it[0], it.index), end=' ')
        #    it.iternext()

        #print(cantidad_obstaculos)
        
        
        
    def generar_estructura_laberinto(self):
        """
        Este metodo devuelve el array para poder generar el laberinto
        @return  :self.mapa
        @author Hugo Chanampe
        """
        self.generar_obstaculos
        return self.mapa
        
            

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

