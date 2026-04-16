contador = 1

for contador in range(contador, 10+1, 1):
    if contador % 3 == 0 and contador % 5 == 0 :
        print('fizz')
    elif contador % 3 == 0:
        print('buzz')
    elif contador % 5 == 0:
        print('fizzbuzz')
    else: 
        print(contador)