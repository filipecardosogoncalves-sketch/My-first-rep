
#Segundos,Minutos,Horas

Tempo_segundos= int(input("Indique um valor em segundos: "))

horas= Tempo_segundos//3600 # usamos // para dividir os segundos de forma a que nos de o valor exato de horas
minutos= (Tempo_segundos%3600)//60 # Uso % para receber o resto das horas e divido por 60 para converter em minutos
segundos= (Tempo_segundos%60)


print("{:d} horas, {:d} minutos, {:d} segundos".format(horas, minutos, segundos))