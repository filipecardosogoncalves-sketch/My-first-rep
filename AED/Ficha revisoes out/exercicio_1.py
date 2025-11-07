#Função media

def media_lista(List):
   media=sum(List)/len(List)
   return media

List=[]

for i in range(1,6):
   num=int(input(f"{i}º número:"))
   List.append(num)

print("A media da lista é:", media_lista(List))