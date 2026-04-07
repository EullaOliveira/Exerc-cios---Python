import math

area = float(input("Digite a área em metros quadrados: "))
caixas = math.ceil(area / 1.5)
print("Quantidade de caixas necessárias: ", caixas)