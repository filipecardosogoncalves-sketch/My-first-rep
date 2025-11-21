import os

# Caminho e nome do ficheiro binário
folder_path= "./files"
file_name = "text.bin"
Pasta_cheia = os.path.join(folder_path, file_name)

def writeText(texto):
    # Garante que a pasta existe
    os.makedirs(folder_path, exist_ok=True)
    #Abre o ficheiro em modo binário para escrita ("wb")
    with open(Pasta_cheia, "wb") as f:
        # Converte o texto para bytes com UTF-8 e escreve no ficheiro
        f.write(texto.encode())# .encode() transforma string → bytes

def readText():
    if not os.path.exists(Pasta_cheia):
        print("Ficheiro não encontrado.")
        return None
    #Abre o ficheiro em modo binário para leitura ("rb")
    with open(Pasta_cheia, "rb") as f:
        #Lê os bytes e converte de volta para string com UTF-8
        return f.read().decode()  # .decode() transforma bytes → string
    
texto = input("Escreve algo para guardar no ficheiro binário: ")  # Recebe input do utilizador
writeText(texto)  # Grava o texto no ficheiro binário

print("\nTexto lido do ficheiro:")
resultado = readText()  # Lê o conteúdo do ficheiro 
if resultado is not None:#Verifica se o ficheiro tem o conteudo
    print(resultado)  # Mostra o texto lido no terminal