# coding=UTF-
import numpy as np

from Laberinto import *

class Robot(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  position  (private)

  """
      #add atributes: relative_posit
      """ El parámetro map_size debe ser suministrdo en el main, habiendo sido adquirido previamente
       a través de un metodo (get_size) del laberinto"""
       
  def __init__(self, map_size, speed, curr_position, sensors):
      #position: inicio (origen de coordenadas para Ava) y recorrido del objeto
      self.curr_position=(0, 0)
      """inicializar el array de desiciones de posiciones recorridas guardando 
        en una lista.
         Request maze for variables  [forward, right , backwards, left]=[i,j, k,  l] with i,j,k,l=1, 0
        check maze map relative to ADA!!!!!_"""
      self.sensors=[0, 0 ,0 ,0]

      #4-FACED ADA: has 4 faces and no orientation
      #self.orientation

      # TODO: Consultar dimensiones del mapa de maze
      #starting array filled with zeros
      #map size need getter in : map_size.
      self.memory_map = np.zero(map_size, map_size)
  
  
  def sensar(self, sensors):
      
  """
    

  @return  :
  @author
  """
  
  pass    
      
  def decidir(self): 
    """ 


    @return  :
    @author
    """
    
    pass

  def desplazar(self):
    """
     

    @return  :
    @author
    
    """
    #self.speed = 1
    #from (i,j) to (i+speed, j)
    pass





