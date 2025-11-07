
Dias=["Domingo", "Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]

def mediaVisit(visitantes):
    media=sum(visitantes)/len(visitantes)
    return media
def valorProximo(visitantes):
    media=sum(visitantes)/len(visitantes)
    mais_proximo= visitantes[0]
    menor_diferença= abs(mais_proximo - media)

    for n in visitantes:
        diferença= abs(n-media)
        if diferença < menor_diferença:
            menor_diferença= diferença
            mais_proximo = n
    return mais_proximo

visitantes=[]
for i in Dias:
    num=int(input(f"Nº de visitantes {i}: "))
    visitantes.append(num)

ordem_personalizada = ["Sábado", "Domingo", "Sexta", "Quinta", "Quarta", "Terça", "Segunda"]

for dia in ordem_personalizada:
    indice=Dias.index(dia)
    print(f"{dia:<6}",visitantes[indice])



print("\nNº medio de visitantes:", mediaVisit(visitantes))
print("\nValor mais próximo da media:", valorProximo(visitantes))