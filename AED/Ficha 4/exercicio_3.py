###Gerar um número aleatório###

import random

opção=""
limitInf=1
limitSup=100
Números=[]
while opção != "N":
    number=random.randint(limitInf,limitSup)
    Números.append(number)
    print("\t\t\t Número sorteado é: ")
    if number == 100:
        break
    limitInf= number+1
    opção= input ("Quer gerar outro número(S\N): ").upper()

Números.sort(reverse=True)
print(Números)

      

