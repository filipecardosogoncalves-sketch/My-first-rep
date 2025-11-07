#Menu de tickets
fila=[]

def tirarSenha(fila):
    if len(fila)>=20:
        print("“It is not possible to generate more tickets at the moment")
    else:
        nova_senha=len(fila)+1
        fila.append(nova_senha)
        print(f"Nova senha gerada: {nova_senha}")

def atendimento(fila):
    if fila:
        senha_atendida = fila.pop(0)
        print(f"Atendendo senha: {senha_atendida}")
    else:
        print("Não há senhas na fila.")

def estado_fila(fila):
    print(f"Senhas à espera: {fila}")
    print(f"Número de senhas na fila: {len(fila)}")
    print(f"Senhas disponíveis: {20 - len(fila)}")

while True:
    print("\nMENU")
    print("1 - Tirar Senha")
    print("2 - Atendimento")
    print("3 - Estado da fila de espera")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        tirarSenha(fila)
    elif opcao == "2":
        atendimento(fila)
    elif opcao == "3":
        estado_fila(fila)
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")