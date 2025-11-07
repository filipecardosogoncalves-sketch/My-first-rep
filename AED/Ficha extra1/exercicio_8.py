#TBM

def tbmCalculator(genero, idade, peso, altura):
    if genero=="M":
        return 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    else:
        return 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)

genero = input("Digite o gênero (M/F): ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (cm): "))

tbm = tbmCalculator(genero, idade, peso, altura)
print(f"A Taxa de Metabolismo Basal (TMB) é: {tbm:.2f} calorias/dia")

