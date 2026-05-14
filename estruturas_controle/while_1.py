#! python
from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um número entre 0 e 9: '))

print('Número secreto {} encontrado!'.format(numero_secreto))