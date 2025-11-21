import os
pasta= './files/'
ficheiro="paises.txt"
ficheiro= pasta + ficheiro



def paisExiste(pais):
    with open(ficheiro, "r", encoding="utf_8") as f:#Abrir o ficheiro como f e com "r"(serve para ler o ficheiro)
        for linha in f:
            if linha.split(";")[0] == pais:#Vai criar uma lista e verificar para cada linha  a posiçao 0 da list se é igual ao pais
                return True#Vai returnar true
    return False
def AddCountry():
    os.system("cls")#Dar clear no terminal
    os.makedirs(pasta, exist_ok=True)  # Garante que a pasta existe

    pais = input("País: ")
    continente = input("Continente: ")
    if paisExiste(pais):#Chamar uma funçao para verificar se o pais existe
        print("O país já existe no ficheiro!")
    else:
        with open(ficheiro, "a", encoding="utf_8") as f:#Abrir o ficheiro como f e com o "a"(serve para adicionar)
            f.write(f"{pais};{continente}\n")
        print("País adicionado com sucesso!")

def showCountries():
    os.system("cls")
    try:
        with open(ficheiro, "r", encoding="utf_8") as f:
            for linha in f:#Para cada linha no ficheiro f vamos printar seguidamente
                print(linha.strip())
    except FileNotFoundError:
        print("Ficheiro não encontrado.")

def showContinents():
    os.system("cls")
    cont = input("Indica o continente: ")
    with open(ficheiro, "r", encoding="utf_8") as f:#F e apenas uma variavel que e temporaria
        for linha in f:
            partes = linha.split(";")#Vai criar uma lista 
            if len(partes) == 2:#Vai verificar se essa lista tem 2 objetos
                pais, continente = partes
                if continente.lower() == cont.lower():#Usamos o lower para garantir que mesmo escrevendo em minuscula ele aceita
                    print(pais, continente)
def numberCountries():
      os.system("cls")
    

opcao = ""
while opcao != "0":
        print("\n\t\t\tMENU")
        print("\t\t1 - Adicionar País")
        print("\t\t2 - Consultar Países")
        print("\t\t3 - Consultar por Continente")
        print("\t\t4 - Consultar nº de Países")
        print("\t\t0 - Sair")
        opcao = input("Digite uma opção: ")
        match opcao:
            case "1": AddCountry()
            case "2": showCountries()
            case "3": showContinents()
            case "4": numberCountries()
            case "0": print("A sair...")
            case _: print("Opção inválida!")
