#Retangulo vazio

def frameTable(lin: int, col: int) ->None:
    for i in range(lin):
        if i == 0 or i == lin - 1:
            print('* ' * col)
        else:
            print("*" + "  " * (col-2) + " *")

linhas=int(input("Digite o número de linhas: "))
colunas=int(input("Digite o número de colunas: "))
frameTable(linhas,colunas)



