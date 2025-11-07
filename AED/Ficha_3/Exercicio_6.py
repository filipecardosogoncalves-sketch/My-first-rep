#Srandard_Name

def standardName(name):
    partes=name.split()
    primeiro = partes[0]
    ultimo = partes[-1]
    iniciais=["."+ p[0] for p in partes[1:-1]]#p[0], vai ser a primeira letra de cada palavra que estiver no meio
    return ' '.join([primeiro] + iniciais + [ultimo])
    

nome=input("Escreve o nome completo: ")
print(standardName(nome))