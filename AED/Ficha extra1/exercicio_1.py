#Triangulo

def triangle(number) -> None:
    for i in range(1, number+1):
        spaces= number - i
        stars= i
        print(" " * spaces + "* " * stars)

num=int(input("Digite o número de linhas do triangulo: "))
triangle(num)