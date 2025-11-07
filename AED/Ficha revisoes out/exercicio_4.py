#Calculos 



def max_num(List):
    maximo=max(List)
    return maximo
def min_num(List):
    minimo=min(List)
    return minimo
def media_num(List):
    media=sum(List)/len(List)
    return media


List=[]
for i in range(1,6):
    num=int(input(f"{i}º Número: "))
    List.append(num)


print("Maior valor: ", max_num(List))
print("Menor Valor: ", min_num(List))
print("Média: ", media_num(List))