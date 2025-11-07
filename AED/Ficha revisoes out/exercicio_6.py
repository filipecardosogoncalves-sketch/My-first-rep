fila=[]

def tirar_senha(fila):
    if len(fila)>=20:
        print("“It is not possible to generate more tickets at the moment")
    else:
        nova_senha=len(fila)+1
        fila.append(nova_senha)
        print(f"Nova senha gerada: {nova_senha}")

def atendimento(fila):
    if fila:
        senha_atendida=fila.pop(0)
        print(f"Atendendo senha: {senha_atendida}")

def estado_da_fila(fila):
    print(f"Senhas à espera: {fila}")
    print(f"Número de senhas na fila: {len(fila)}")
    print(f"Senhas disponiveis: {20-len(fila)}")

while True:
    print("\t\t\t 1-Tirar senha")
    print("\t\t\t 2-Atendimento")
    print("\t\t\t 3-Estado da fila")
    print("\t\t\t 4-Sair")
    opçao=input("Opção: ")
    
    if opçao=="1":
        tirar_senha(fila)
    elif opçao=="2":
        atendimento(fila)
    elif opçao=="3":
        estado_da_fila(fila)
    elif opçao=="4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")