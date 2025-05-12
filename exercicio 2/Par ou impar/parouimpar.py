class Verificar():

    def __init__ (self, numero):
         self.numero = numero 
    
    def parOuImpar(self):
         if self.numero == 0:
              return f"{self.numero} nao é impar nem par"
         elif self.numero %2 == 0:
              return f"{self.numero} o numero é par"
         else:
              return f"{self.numero} o numero é impar" 
        