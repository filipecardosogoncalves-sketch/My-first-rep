#ShortName

def shortName(name):
    partes=name.split()
    return partes[0] + " "  + partes[-1]

nome=input("Escreve o nome completo: ")
print(shortName(nome))