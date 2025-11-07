#Euromilhões
import random

def generateEuromelhões():
      nums= random.sample(range(1,50),5)
      stars=random.sample(range(1,12),2)
      print(f"Chave do Euromilhões: {nums} \tEstrelas: {stars}")

opção= "S"
while opção.upper()=="S":
      generateEuromelhões()
      opção=input("Deseja gerar uma nova chave: ")

