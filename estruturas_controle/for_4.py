#for i in range(1, 11):
#    if i == 6:
#        break
#    print(i)
#else:
#    print('Fim')

from random import randint


def sortear_dados():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 0:
        continue

    if sortear_dados() == i:
        print(f'Parabéns, você acertou o número {i}!')
        break

else:
    print('Que pena, você não acertou nenhum número.')
