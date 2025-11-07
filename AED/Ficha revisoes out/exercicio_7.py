#Soma de elementos pares

List=[]

def soma_pares(List):
     for i in range(1,11):
      num=int(input(f"{i}º número: "))
      if num%2==0:
         List.append(num)
         soma=sum(List)
     return soma


print("A soma dos números pares é ",soma_pares(List))
