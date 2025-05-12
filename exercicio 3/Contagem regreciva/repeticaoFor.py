class Contagem():
    def __init__(self,num):
        self.numero = num  

    def regrecivo (self):
        contagem = []
        for i in range(self.numero, -1, -1):
            contagem.append(i)  
        return contagem
           