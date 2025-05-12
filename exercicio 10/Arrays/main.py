#Crie uma função que receba uma lista e retorne a soma de todos os elementos.
#digita o numero e converte ele para negativo ou positivo
lista = []

for i in range(+0, 3, +1):

    num= int (input("digie um numero"))

    lista.append (num * -1)

print (f"os numeros degitados foram {lista}")
#####################################################################################
# o numero e convertido novamente e cada repeticao ele soma 
nume =[]
soma=0
for i in range(len(lista)):
  
  lista[i] = lista[i] * -1

  soma += lista[i]
  lista[i] = soma
  nume.append (lista[i])

print (f"invertido {nume}")

###################################################################
for i in range (len(lista)):
   
  lista.reverse()

print (f"{lista}")

##############################################################################
resultado =[]
for i in range(len(lista)):
    
    soma += lista[i]
    lista[i] = soma 
resultado.append(lista[i])


print (f"aaaaaaaa{resultado}")