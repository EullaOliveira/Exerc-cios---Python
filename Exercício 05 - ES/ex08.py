idade = int(input('Qual a idade do nadador? '))

if idade >= 5 and idade <= 7:
    print('Categoria: PEIXINHO')
elif idade >= 8 and idade <= 10:
    print('Categoria: INFANTIL A')
elif idade >= 11 and idade <= 13:
    print('Categoria: INFANTIL B')
elif idade >= 14 and idade <= 17:
    print('Categoria: JUVENIL')
elif idade < 5:
    print('Não há categoria disponível.')
else:
    print('Adulto')