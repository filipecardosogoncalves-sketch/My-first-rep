#Nota mais alta e mais baixa

def dataGrades(notas):
    maior=max(notas)
    menor=min(notas)
    média=sum(notas)/len(notas)
    acima_media=sum(1 for nota in notas if nota>média)
    return maior,menor,acima_media

notas=[]

i= 1
while len(notas)<10:
    try:
      nota=float(input(f"{i}ª avaliação: "))
      if nota <0 or nota > 20:
         raise ValueError
      notas.append(nota)
      i+=1
    except ValueError:
       print("Valor inválido, tente novamente")

maior, menor, acima_media= dataGrades(notas)
print("\n",notas)
print(f"O maior número é: {maior}")
print(f"A menor nota é: {menor}")
print(f"Nº de valores acima da média é: {acima_media}")

    
    