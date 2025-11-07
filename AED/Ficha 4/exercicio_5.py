#Encontar as posiçoes de um número repetido

List_num=[]
tentativa=1

while tentativa<10:
    try:
      num=int(input(f"{tentativa}ª número: "))
    except ValueError:
       print("O número inserido não é inteiro, insira novamente")
    except: print("Número invalido")
    else:
       List_num.append(num)
       tentativa+=1

def searchNumber(List_num, numberSearch):
    cont=List_num.count(numberSearch)
    if cont == 0:
       return -1
    

Num_search=int(input("Número de pesquisa: "))
print(f"O número {Num_search} encontra-se nas posições:", searchNumber(Num_search))

