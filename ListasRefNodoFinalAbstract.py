

from abc import ABC, abstractmethod
 
class ListaRefNodoFinalAbstract(ABC):
    @abstractmethod
    def esta_vacia():
        pass
    
    @abstractmethod
    def vaciar():
        pass
    
    @abstractmethod
    def tamanio():
        pass
    
    @abstractmethod
    def agregar_inicio():
        pass
   
    @abstractmethod
    def agregar_final():
        pass
    
    @abstractmethod
    def contiene():
        pass
    
    @abstractmethod
    def primer_elemento():
        pass
    
    @abstractmethod
    def ultimo_elemento():
        pass
    
    @abstractmethod
    def eliminar_primero():
        pass
    
    @abstractmethod
    def eliminar_ultimo():
        pass
    
    @abstractmethod
    def sustituir(actual,nuevo):
        pass
      
    @abstractmethod
    def imprimir():
        pass
    
    @abstractmethod
    def iterador():
        pass      
        
    
    