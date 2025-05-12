import random
segredo = random.randint(1, 10)
num = int(input("adivinhe o numero de 1 a 10"))

if num == segredo:
    print("acertou")
else:
    print(f" o numero {num}")
    