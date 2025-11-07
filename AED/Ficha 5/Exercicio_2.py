#Lista de cidades e meses
import random
import os

meses=['\tJaneiro','\tFevereiro','\tMarço','\tAbril','\tMaio','\tJunho']
cidades=['Edimburgo','Glasgow','Dundee']
ncidades=3
nmeses=6

def showData(matriz):
    os.system("cls")
    print("\n\t\t\tTabela de Pluviosidade")
    i=0
    for cidade in cidades:
        print("\n\t\t {:s}".format(cidade), end="\t")

        for j in range(6):
            print(matriz[i][j], end="\t")
        i+=1
        print("\n")

def dataAnalysis(matriz):
    #media de cada cidade
    media_cidade=[0]*3      #Lista com 3 posições
    media_meses=[0]*6    
    for i in range(ncidades):
       media_cidade[i]= sum(matriz[i])/len(matriz[i])    #Sub-lista i corresponde a uma cidade
       print("Media de pluviosidade de {:s} = {:2f}".format(cidades[i],media_cidade[i]))
    
    sumMeses=[0]*6

    for j in range(nmeses):              #Para cada mes de jan a jun
        for i in range(ncidades):         #Vamos interar as 3 cidades
            sumMeses[j]+= matriz[i][j]  #== matriz[0][j] + matriz[1][j] + matriz[2][j],          
        print("A media do mes {:s} = {:2f}".format(meses[j],sumMeses[j]/nmeses))



matriz = []
for i in range(3):
    print("\n\t\t Pluviosidade em {:s}".format(cidades[i]))
    matriz.append([])
    for j in range(6):
        pluv=int(input("\t\t\t {:s}:".format(meses[j])))
        matriz[i].append(pluv)
    print("\n")


showData(matriz)
dataAnalysis(matriz)