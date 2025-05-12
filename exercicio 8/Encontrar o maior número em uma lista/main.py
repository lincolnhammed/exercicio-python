def numero_maior(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior=numero
    return maior
numero=[]
for i in range(5):
    num = int(input(f"digite{i+1}\n "))
    numero.append(num)

print (f"o maior numero digitado foi {numero_maior(numero)}")