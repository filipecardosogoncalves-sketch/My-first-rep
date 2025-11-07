#Codificar uma mensagem


def codificar(Name):
    chave = {'a': '1', 'e': '2' , 'i': '3', 'o': '4', 'u': '5'}
    codigo=""
    for letra in Name:
        codigo+=chave.get(letra.lower(),letra)# get é usado em dicionarios
    return codigo
    
nome=input("Digite o seu nome: ")
print(codificar(nome))


#chave = {'a': '1', 'e': '2'}

#print(chave.get('a'))         # → '1' (existe)
#print(chave.get('i'))         # → None (não existe)
#print(chave.get('i', 'X'))    # → 'X' (valor padrão)
