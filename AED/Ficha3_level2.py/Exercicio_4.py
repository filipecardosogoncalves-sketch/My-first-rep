#Calculos Complexos  Mifflin-St. Jeor, esta é uma forma preditiva para determinar o gasto energético  

def calculatorTBM(genero,peso,altura,idade):
    if genero=="M":
        return 10*peso + 6.25*altura - 5*idade + 5
    else:
        return 10*peso + 6.25*altura - 5*idade - 161


genero=input("Digite o seu género(M/F): ")
peso=float(input("Peso: "))
altura=int(input("Altura: "))
idade=int(input("Idade: "))
tbm = calculatorTBM(genero, peso, altura, idade)
print(f"O seu gasto energético diário é de {tbm:.2f}")