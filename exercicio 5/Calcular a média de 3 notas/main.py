
nota1 = float(input("digite a primeira nota\n"))
nota2 = float(input("digiete a segunda nota\n"))
nota3 = float(input("digite a terceira nota\n"))

soma = nota1+nota2+nota3
media = soma / 3

if media >= 7:
            #A média é 7. Aprovado.
    print(f"the average grede is: {media:.2f} PASSED")
else:
    print(f"the average grade is:{media:.2f} FAILED")
