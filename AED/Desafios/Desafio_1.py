#Desafio 1 Code 4 digits


#Função
def openSafe():
    import random

    print("\t\t\t\t\t ==DIGITAL SAFE==")
    print("\t\t\t Try to guess the SECRET CODE(4 between 0 and 9)")
    print("\t\t\t\t\t You have 10 attempts")
    nums= random.sample(range(10), 4)
    
    tentativas = 0
    limite = 10
    #O programa corre enquanto o numero de tentativas nao exceder o limite
    while tentativas<limite:
        tentativas+=1
        enter=input("{:d}º Tentativa:".format(tentativas))
        codigo=enter.strip().split(" ")
        codigo = [int(n) for n in codigo]#O programa nao estva a dar um lista no split, por isso usei isto para criar a lista

        list_num=[]
        for n in range(4):
            if codigo[n]==nums[n]:
                list_num.append(codigo[n])
                
        if list_num:
            print(f"Os números {" ".join(map(str,list_num))} esta(ão) correto(s) e na(s) posição(s) certa(s)")
        else:
            print("Nenhum número certo")

        if codigo == nums:
            print("Acertaste o codigo")
            break
    
    print("As suas tentativas acabaram, o código era:", nums)

openSafe()
    


    

    
                


