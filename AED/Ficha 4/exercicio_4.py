#Faturação mês

Meses=["Janeiro", "Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]


def maiorValor(faturação):
    maior=max(faturação)
    pos= faturação.index(maior)
    return (Meses[pos])
def menorValor(faturação):
    menor=min(faturação)
    pos= faturação.index(menor)
    return (Meses[pos])
def mediaFat(faturação):
    media=sum(faturação)/len(faturação)
    return media

faturação=[]

for i in range(12):
    valor = float(input(f"Indique a faturação do mês de {Meses}: "))
    faturação.append(valor)


print(f"O mês de maior faturação é {maiorValor(faturação)}")
print(f"O mês de maior faturação é {menorValor(faturação)}")
print(f"A média anual de faturação é {mediaFat(faturação)}")