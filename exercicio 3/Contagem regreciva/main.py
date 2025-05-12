from repeticaoFor import Contagem 

print ("digite um numero inteiro para uma contagem regreciva")
num =int(input())

p = Contagem(num)
contagem_resultado = p.regrecivo()

for numero in contagem_resultado:
    print(numero)
print("FIM")