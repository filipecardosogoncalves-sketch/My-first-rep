# Losango

def geometricDiamond(altura: int) -> None:
    for i in range(1, altura+1):
       spaces = (altura - i) // 2
       print(" "*spaces + "* " *i)
    for i in range(altura,0):
        spaces = (altura - i) // 2
        print(" "*spaces + "* " *i)

alt=int(input("Digite a altura do losango: "))
geometricDiamond(alt)