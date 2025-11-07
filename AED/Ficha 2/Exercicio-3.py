
# Random

import random

num1= random.randrange(1,50)
tentativas = 0
limite = 10
 
while tentativas<limite:
    tentativas+=1
    guess=int(input("{:d}º Tentativa:".format(tentativas)))
    
    if guess<num1:
        print("O número é MAIOR")
    elif guess>num1:
        print("O número é MENOR")
    else:
        print(" Parabéns, acertou o número")
        break
else:
    print("\nEsgotou as sus 10 tentativas")
    

 
   