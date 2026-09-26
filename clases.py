# 1. Clase Padre
class ElementoRed :

    """ Representa un elemento general de la red eléctrica. 
    Atributos: id (str): Código único que identifica al elemento. """

    def __init__ ( self, id_elemento) :
        self.id_elemento = id_elemento
  
class SistemaPotencia  :
    """ Representa y administra un sistema eléctrico de potencia.
      Atributos: id (str): Código único que identifica al sistema. """
    def __init__ ( self, id_sistema) :
        self.id_sistema=id_sistema
        self.__elementos = []


    def agregar_elemento(self, elemento):
        """Agrega elemento al sistema"""

        self.__elementos.append(elemento)

    def eliminar_elemento(self, id_elemento: str):
        """Elimina un elemento del sistema"""

        for elemento in self.__elementos:

            if elemento.id_elemento == id_elemento:
                self.__elementos.remove(elemento)
                return

        print("No se encontro elemento")


 # 2. Clase Hija
class  Generador ( ElementoRed ) :
    """ Representa un generador eléctrico perteneciente al sistema. 
    Atributos:
      id (str): Código único del generador. 
      potencia_max (float): Potencia máxima que puede entregar el generador. 
      costo_operativo (float): Costo asociado a la operación del generador. """
    
    def __init__ ( self , id_elemento : str , potencia_max : float,costo_operativo:float ) :
        super() . __init__ ( id_elemento) # Llamada al padre
        self.__potencia_max = potencia_max
        self.__costo_operativo = costo_operativo

    def get_potencia(self):
        """ Entrega la potencia máxima del generador. 
                Returns: float: Potencia máxima del generador. """
        return self.__potencia_max

    
    def set_potencia(self,new): 
        """ Modifica la potencia máxima del generador."""   

        if new > 0:
            self.__potencia_max = new

        else:
                    print("La potencia máxima debe ser positiva")


    def get_costo(self):
            """ Entrega el costo operativo. 
                    Returns: float: costo operativo del generador. """
            return self.__costo_operativo
    
        
    def set_costo(self,new): 
            """ Modifica el costo operativo del generador."""   
    
            if new > 0:
                self.__costo_operativo = new
    
            else:
                        print("El costo debe ser positivo")


class  Carga ( ElementoRed ) :
    """ Representa una carga eléctrica perteneciente al sistema. 
    Atributos: id (str): Código único de la carga. """
    def __init__ ( self , id_elemento : str ) :
        super() . __init__ ( id_elemento ) # Llamada al padre
        

class  LineaDeTransmision ( ElementoRed ) :
    """ Representa una línea de transmisión perteneciente al sistema. 
    Atributos: id (str): Código único de la línea de transmisión. """    
    def __init__ ( self , id_elemento : str ) :
        super() . __init__ ( id_elemento ) # Llamada al padre

class  Transformador ( ElementoRed ) :
    """ Representa un transformador perteneciente al sistema. 
    Atributos: id (str): Código único del transformador. """    
    def __init__ ( self , id_elemento : str ) :
        super() . __init__ ( id_elemento ) # Llamada al padre