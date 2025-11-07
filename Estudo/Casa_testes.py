# Teste exercicio 9 Ficha 3

def generatepassword(username):
    if " " in username:
        return "Username inválido" #recebe um texto com espaços e retorna "Username inválido"
    
    import random
    for i in range(0,len(username),2):
        password+=username[i]# vai adicionar à password as letras das posiÇões i 
        password+=str(random.randint(1,9))# add a random number between 1 and 9 after


    
    


name=input("Digite um username: ")
print=("Password: ", generatepassword(name))