#Parque de estacionamento
Park = [
    [0, 0, 0, 0, 0],  # Fila 1
    [0, 0, 0, 0, 0],  # Fila 2
    [0, 0, 0, 0, 0]   # Fila 3
]

def car_entrance(Park):
    for i in range(3):
        for j in range(5):
            if Park[i][j]==0:
                Park[i][j]==1
                return f"Carro estacionado na Fila {i+1}, Lugar {j+1}"
    print("Parque está completo")
def car_exit(Park):
    fila = int(input("Fila (1 a 3): ")) - 1
    lugar = int(input("Lugar (1 a 5): ")) - 1
    if Park[fila][lugar] == 1:
        Park[fila][lugar] = 0
        print("Carro saiu com sucesso.")
    else:
        print("Esse lugar já está livre.")

def estado_parque(Park):
    ocupados = 0
    for i in range(3):
        for j in range(5):
            if Park[i][j] == 1:
                ocupados += 1
    livres = 15 - ocupados
    print(f"Lugares ocupados: {ocupados}")
    print(f"Lugares livres: {livres}")

while True:
    print("\t\t\t MENU")
    print("\t\t 1-Car Entrance")
    print("\t\t 2-Car Exit")
    print("\t\t 3-Park State")
    print("\t\t 0-Exit")
    opcao = input("Opção: ")
    
    if opcao == "1":
        car_entrance(Park)
    elif opcao == "2":
        car_exit(Park)
    elif opcao == "3":
        estado_parque(Park)
    elif opcao == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")




