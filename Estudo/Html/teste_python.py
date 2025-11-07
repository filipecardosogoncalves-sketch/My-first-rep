
# Teste de Estudo

import random

num= random.randint(1,20)


tentativas=0
limite= 10

while tentativas< limite:
    tentativas+=1
    guess= int(input(" {:d}º tentativa: ".format(tentativas)))
    
    if num > guess:
        print("O número é MAIOR")
    elif num < guess:
        print("O número é MENOR")
    else:
        print("Parabéns acertou em {:d} tentativas".format(tentativas))
print("\n Esgotou as 10 tentativas")