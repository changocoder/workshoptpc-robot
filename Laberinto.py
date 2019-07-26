# coding=UTF-8

from Robot import *
from Obstaculo import *

import numpy as np
from random import randrange,shuffle, randint
from itertools import product           # Producto cartesiano


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
        self.pos_robot_x=0
        self.pos_robot_y=0
        self.ada_robot = None
        self.X=(0,0)
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
            if i<20: # este if es para evitar que encuentre la solución rapido. (se puede mejorar la implementación)
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
        self.pos_robot_x= pos_robot[0][0][0]
        self.pos_robot_y= pos_robot[1][0][0]
        n_0=self.mapa[self.pos_robot_x-1][self.pos_robot_y]
        n_1=self.mapa[self.pos_robot_x][self.pos_robot_y+1]
        try:
            n_2=self.mapa[self.pos_robot_x+1][self.pos_robot_y]
        except IndexError:
            # EN CASO DE QUE HAYA ENCONTRADO LA SALIDA
            n_2=1
        try:
            n_3=self.mapa[self.pos_robot_x][self.pos_robot_y-1]
        except IndexError:
            n_3=1
        self.vecinos[0]=n_0
        self.vecinos[1]=n_1
        self.vecinos[2]=n_2
        self.vecinos[3]=n_3

        return self.vecinos.tolist()


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

    def controlar_escape(self):
        """
        Este metodo devuelve el array para poder generar el laberinto
        @return  :self.mapa
        @author Hugo Chanampe
        """
        salida="false"
        if self.pos_robot_x==0:     #Evaluar las condiciones para encontrar la salida (capaz que convenga crear un nuevo metodo para esto)
            salida="true"
        elif self.pos_robot_x ==(self.dim_x+1):
            salida="true"
        elif self.pos_robot_y==0:
            salida="true"
        elif self.pos_robot_y==(self.dim_y+1):
            salida="true"
        return salida


    def generar_estructura_laberinto(self, robot):
        """
        Este metodo devuelve el array para poder generar el laberinto
        @return  :self.mapa
        @author Hugo Chanampe
        """
        self.ada_robot = robot
        self.generar_obstaculos()
        self.generar_ada()



    def generar_ada(self):
        """
        @param Robot ada_robot :
        @return  : Inicializar el robot en el laberinto
        @author : Hugo, Gustavo, Lucas
        """
        self.mapa[self.x_ini][self.y_ini]=3

    def actualizar_laberinto(self, n):
        """
        @return : actualizar matriz despues del movimiento del robot
        @author Hugo y Lucas:
        """
        pos_robot=list(zip(np.where(self.mapa==3))) #Busca en el mapa donde esta el robot y lo mete en una lista
        self.pos_robot_x= pos_robot[0][0][0]
        self.pos_robot_y= pos_robot[1][0][0]
        self.mapa[self.pos_robot_x][self.pos_robot_y]=0
        if n ==0:
            self.mapa[self.pos_robot_x-1][self.pos_robot_y]=3
        if n ==1:
            self.mapa[self.pos_robot_x][self.pos_robot_y+1]=3
        if n ==2:
            self.mapa[self.pos_robot_x+1][self.pos_robot_y]=3
        if n ==3:
            self.mapa[self.pos_robot_x][self.pos_robot_y-1]=3

        self.pos_robot_x= pos_robot[0][0][0]
        self.pos_robot_y= pos_robot[1][0][0]

    def get_direccion_robot(self):
        """
        @return : True or False si el robot esta en la salida
        @author Hugo
        """
        pos_robot=list(zip(np.where(self.mapa==3))) #Busca en el mapa donde esta el robot y lo mete en una lista
        self.pos_robot_x= pos_robot[0][0][0]
        self.pos_robot_y= pos_robot[1][0][0]
        return (self.pos_robot_x, self.pos_robot_y)

    # Crear un laberinto aleatorio en Python3 usando el algoritmo de recorrido en profundidad.
    #
    # Autor: Lucas Farigliano
    # Fecha: 2019/07/26
    def constructor_laberinto_2(self):
        self.mapa = [[1]*(self.dim_y+2) for i in range (self.dim_x+2)]  # Tablero
        for i, j in product(range(1,(self.dim_x+2), 3), range(1,(self.dim_y+2), 2)):
            self.mapa[i][j] = 0                   # Poner celdas blancas
            self.X = set()                           # Conjunto de celdas visitadas
            self.laberinto_2_visitar(randint(0, self.dim_x + 2 - 1), randint(0, self.dim_y + 2 - 1))  # Inicio en celda aleatoria
        self.mapa=np.asarray(self.mapa)
#    #return('\n'.join(''.join(fila) for fila in self.mapa))  # Unir símbolos en un str
    def laberinto_2_vecinos(self,i, j):                  # Conjunto de celdas aledañas a (i, j)
        if 0 < i: yield i - 1, j
        if i < (self.dim_x + 2 - 1): yield i + 1, j
        if 0 < j: yield i, j - 1
        if j < (self.dim_y + 2 - 1): yield i, j + 1
    def laberinto_2_visitar(self,i, j):                  # Alg. de recorrido en profundidad:
        self.X.add((i, j))                   # Marcar celda actual como visitada
        N = list(self.laberinto_2_vecinos(i, j)); shuffle(N)  # Desordenar celdas vecinas
        for h, k in N:                  # Para cada celda vecina
            if (h, k) in self.X: continue    # ...que no haya sido visitada:
            self.mapa[h][k] = 0  # Tumbar el muro que las separa
#            self.laberinto_2_visitar(h, k)               # Visitar vecina recursivamente
#
