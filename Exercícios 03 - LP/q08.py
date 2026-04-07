import math

tempo = float(input("Digite o tempo em horas: "))
horas = math.floor(tempo)
minutos = math.floor((tempo - horas) * 60)
print("Tempo:", horas, "hora(s) e", minutos, "minuto(s)")