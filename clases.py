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

    def __init__ ( self , id_elemento : str , potencia_min : float,
                  potencia_max: float, costo_operativo:float) :   
        super() . __init__ ( id_elemento) # Llamada al padre
        if potencia_min < 0 or potencia_max < 0:
            raise ValueError("Las potencias no pueden ser negativas.")
        if potencia_min > potencia_max:
            raise ValueError("La potencia mínima no puede ser mayor a la potencia máxima.")
        if costo_operativo < 0:
            raise ValueError("El costo operativo no puede ser negativo.")

        self.__potencia_min = potencia_min 
        self.__potencia_max = potencia_max
        self.__potencia_despachada = 0.0   
        self.__costo_operativo = costo_operativo

    def get_potencia_maxima(self) -> float:
        """ Entrega la potencia máxima del generador.
            Returns: float: Potencia máxima del generador. """
        return self.__potencia_max

    def get_potencia_minima(self) -> float:
        """ Entrega la potencia mínima del generador.
            Returns: Potencia mínima del generador. """
        return self.__potencia_min


    def get_potencia_despachada(self) -> float:
        """ Entrega la potencia actual del generador.
            Returns: Potencia actual del generador. """
        return self.__potencia_despachada


    def set_potencia_despachada(self, new):
        """ Modifica la potencia despachada del generador."""
        if new == 0:
            self.potencia_despachada = 0.0   # El generador está apagado.

        if self.__potencia_min <= new <= self.__potencia_max:
            self.__potencia_despachada = new

        elif new < self.__potencia_min:
            raise ValueError("La potencia despachada es menor al límite inferior del generador.")

        else:
            raise ValueError("La potencia despachada es mayor al límite superior del generador")


    def get_costo(self):
            """ Entrega el costo operativo.
                Returns: float: costo operativo del generador. """
            return self.__costo_operativo


    def set_costo(self,new):
            """ Modifica el costo operativo del generador."""
            if new >= 0:
                self.__costo_operativo = new
            else:
                raise ValueError("El costo debe ser positivo")


class  Carga ( ElementoRed ) :
    """ Representa una carga eléctrica perteneciente al sistema.
    Atributos: id (str): Código único de la carga. """
    def __init__ ( self , id_elemento : str, potencia_demandada: float) :
        super().__init__( id_elemento ) # Llamada al padre
        if potencia_demandada < 0:
            raise ValueError("La potencia demandada no puede ser negativa.")
        self.__potencia_demandada = potencia_demandada

    def get_potencia(self):
        """
        Entrega potencia demandada.
        Returns: float: Potencia demandada.
        """
        return self.__potencia_demandada

    def set_potencia_demandada(self, potencia):
        """
        Modifica la potencia demandada.
        Args: potencia (float): potencia demandada
        """
        if potencia >= 0:
            self.__potencia_demandada = potencia
        else:
            raise ValueError("La potencia demandada no puede ser negativa.")

class Barra(ElementoRed):
    def __init__(self, id_elemento: str):
        super().__init__(id_elemento)
        self.__generadores = []
        self.__cargas = []

    def agregar_generador(self, generador):
        if not isinstance(generador, Generador):
            raise ValueError("El elemento debe ser un objeto de la clase Generador.")
        self.__generadores.append(generador)

    def agregar_carga(self, carga):
        if not isinstance(carga, Carga):
            raise ValueError("El elemento debe ser un objeto de la clase Carga")
        self.__cargas.append(carga)

    def calcular_generacion_total(self):
        generacion_total = 0.0
        for generador in self.__generadores:
            generacion_total = generacion_total + generador.get_potencia_despachada()
        return generacion_total

    def calcular_demanda_total(self):
        demanda_total = 0.0
        for carga in self.__cargas:
            demanda_total = demanda_total + carga.get_potencia()
        return demanda_total

    def calcular_potencia_neta(self):
        """
        Calcula la potencia neta inyectada a la barra (potencia generada - potencia demandada)
        """
        return self.calcular_generacion_total() - self.calcular_demanda_total()




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
