

from ListasRefNodoFinalAbstract import ListaRefNodoFinalAbstract
from Nodo import Nodo

class ListaRefNodoFinal(ListaRefNodoFinalAbstract):
   
   def __init__(self):
        self.inicio= None
        self.fin = None
        self.cuantos=0

 
#Metodo que egresa true si la lista esta vacia y false en otro caso.
   def esta_vacia(self):
        if self.cuantos==0:
            return True
        else:
            return False 
#Método para eliminar todos los elementos de una lista, no regresa nada
   def vaciar(self):
       self.inicio=None
       self.cuantos=0

# Método que regresa la cantidad de elementos que tiene una lista, debe de ser de complejidad  O(1)
   def tamanio(self,elemento):
       cont=0
       if self.esta_vacia():
           return False
       else:
           pos=self.inicio
           while pos != None:
               if pos ==elemento:
                   cont +=1
               return cont
           
          

# Método para agregar un elemento al inicio de la lista, no regresa nada
   def agregar_inicio(self,elemento):
       nuevo=Nodo(elemento) 
       nuevo.siguiente=self.inicio
       return nuevo
       
       
       
#Metodo para agregar un elemento al final de la lista, no regresa nada
   def agregar_final(self,elemento):
       nuevo=Nodo(elemento)
       self.fin.siguiente=nuevo
       self.fin=nuevo
       self.cuantos +=1

# Método para determinar si un elemento pertenece a la lista, regresa true si el elemento está en la lista y false en otro caso       
   def contiene (self,elemento):   
       if self.esta_vacia():
           return False
       else:
           posicion=self.incio
           while posicion != None:
               if posicion==elemento:
                   return True
           return False
               
#Método que regresa el primer elemento inicial de la lista
   def primer_elemento(self):
       return self.inicio

#Método que devuelve el último elemento de la lista
   def ultimo_elemento(self,elemento):
       temp=elemento
       while temp.siguiente:
           temp=temp.siguiente
       return self.fin

#Método para eliminar el último elemento de la lista, no regresa nada
   def eliminar_primero(self,elemento):
       if self.esta_vacia():
           print("es vacio")
       else:
           pos=self.fin
           while pos.siguiente:
               pos=pos.siguiente
           pos.siguiente=None
           self.inicio=pos
             
# Método para eliminar el último elemento de la lista, no regresa nada
   def eliminar_ultimo (self,elemento):
       if self.esta_vacia():
           print("es vacio")
       else:
           pos=self.inicio
           while pos.siguiente:
               pos=pos.siguiente
           pos.siguiente=None
           self.fin=pos
           
#Método para sustituir un elemento  
   def sustituir(self,actual,nuevo):
        posicion = self.inicio
        while (posicion != None):
            if posicion.elemento == actual:
                posicion.elemento = nuevo
            posicion = posicion.siguiente
              
#Método para imprimir a los elementos en las posiciones impares que se encuentran en la lista de inicio a fin, no regresa nada
   def imprimir(self):
       it= self.iterador()
       print("imprimir...")
       while (it.has_next()):
           print(it.next())
           
#Método que devuelve un iterador sobre la lista
   def iterador(self):
       return _Iterador(self.inicio)
        
#Clase _Iterador

class _Iterador:
    def __init__(self,inicio):
        self.posicion = inicio
        
    def has_next(self):
        return self.posicion!= None
    def next(self):
        if self.posicion == None:
            raise NameError("Se llegó al final de la lista")
                                
        elemento = self.posicion.elemento
        self.posicion = self.posicion.siguiente
        self.posicion = self.posicion.siguiente
            
        return elemento
    
    

  
    
    

