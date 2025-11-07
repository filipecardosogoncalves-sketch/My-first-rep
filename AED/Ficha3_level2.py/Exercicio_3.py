#Exercicio 2.0

def numCities(list):
    print(f" O número de cidades é: {len(list)}")
    for citie in list:
        print(f"- {citie}")# o for vai percorrer todos os elementos da lista e vai imprimi-los com uma virgula antes

Cidades={"Braga", "Porto", "Lisboa", "Faro", "Setúbal"}
numCities(Cidades)
