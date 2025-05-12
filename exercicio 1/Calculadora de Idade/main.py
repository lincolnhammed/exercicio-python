from calcularIdade import Pessoa

print ("digite se nome")
nome = input()
print ("digite seu ano de nascimento")
ano_denacimento = int(input())


pessoa = Pessoa(nome, ano_denacimento)
pessoa.calcular_idade()

#print(f"{pessoa.nome} tem aproximadamente {idade} anos.")
print (pessoa.maior_18())


