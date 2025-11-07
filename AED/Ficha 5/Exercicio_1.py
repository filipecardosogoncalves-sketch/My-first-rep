import random

def showTable():
    print("\n Tabela aleatoria")
    for linha in matriz:
        print("\t\n", linha, end=" \n\n")

def verifyTable():
    for i in range(3):
        print(f"Linha {i+1}:",sum(matriz[i]))

    listaSomasColuna=[0]*3
    for i in range(3):
        for j in range(3):
            listaSomasColuna[i]+=matriz[j][i]
    print("Soma das colunas da tabela", listaSomasColuna)


matriz=[]
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(random.randint(0,9))

showTable()
verifyTable()




