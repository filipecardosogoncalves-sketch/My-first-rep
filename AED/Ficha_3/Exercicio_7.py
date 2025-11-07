#Password and Name

def generatePassword(userName):
    if " " in userName:
        return "Username is invalid"
    

    import random
    password=" "
    for i in range(0,len(userName),2):#Isto serve para que o ciclo so percorra as posiçoes pares do nome, por isso ele vai de 2 em 2
        password+= userName[i]#vai ser adicionada á password as letras no username nas posições "i"
        password+=str(random.randint(1,9))#vai adicionar  á password, depois de cada letra, um número random de 1 a 9
    password+=str(len(userName))#Depois da pass ja estar composta ele adiciona á pass o numero de digitos do userName
    return password




nome=input("Digite um nome: ")
print("Password: ", generatePassword(nome))
