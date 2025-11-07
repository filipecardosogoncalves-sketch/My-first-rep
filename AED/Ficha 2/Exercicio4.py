

#Random 2.0

 
import random

num= random.randint(1,20)
tentativas=0
limite= 10

opcao= "S"

while opcao=="S":
    while tentativas<limite:
         tentativas+=1
         guess=int(input("{:d}º Tentativa:".format(tentativas)))
    
         if guess<num:
          print("O número é MAIOR")
         elif guess>num:
          print("O número é MENOR")
         else:
          print(" Parabéns, acertou o número")
          break
    else:
       print("\nEsgotou as suas 10 tentativas")
        
    opcao= input("Deseja jogar de novo?:" )
    num= random.randint(1,20)
    tentativas=0
    limite= 10
    tentativas+=1
    guess=int(input("{:d}º Tentativa:".format(tentativas)))





      
    
    