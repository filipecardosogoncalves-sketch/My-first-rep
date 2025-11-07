# test senha

while True:# true é um condiçao que nao para ate colocar break, pois é uma condição infinita sempr verdadeira
    senha=input("Digite uma senha:")
    
    tem_letra=any(char.isdigit() for char in senha)
    # --any-- vai retonar se pelo menos um caractre for numero
    #char.digit serve para verificar se a senha tem algum digito
    # for char in senha, vai percorrer cada letra da senha
    tem_numero=any(char.isalpha() for char in senha)
    tem_espaço=" " in senha

    if len(senha)<8:#len, seignifica comprimento e vai percorrer o numero de elementos da senha
        print("senha inválida, tem de ter pelo menos 8 digitos")
    elif not tem_letra or not tem_numero:
        print("senha inválida, tem de conter letras e números")
    elif tem_espaço:
        print("senha iválida, não pode ter espaços")
    else:
        print("Senha válida")
        break