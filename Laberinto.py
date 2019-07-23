# coding=UTF-8
from Robot import *
from Obstaculo import *
import numpy as np
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
     self.mapa= np.ones((self.dim_x+1,self.dim_y+1))

  def generar_solucion(self):
    """
    @return  : el camino solución del laberinto
    @author  Lucas Farigliano

    La matriz parte de todos ceros. Lo primero que hace el método es 
    cambiar los 0 por 3 para que se pueda trabajar mas facilmente.
    """
    
    pass

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
 laberinto debe tener get_size (tamaño del laberinto)
                      get_neighbor_map (devuelve lista de 4 0 o 1)
                      
 '''

