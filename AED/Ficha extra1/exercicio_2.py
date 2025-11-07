#Square

def square(number: int) -> None:
    for i in range(number):
        print( "*  " * number)

num= int(input("Digite o número de linhas: "))
square(num)


