#! python
# List comprehension é uma forma rápida de criar listas a partir de iteráveis.
# A sintaxe é a seguinte:   # [expressão for item in iterável if condição]
# A expressão é o valor que será adicionado à lista para cada item do iterável que satisfaz a condição (se houver). O item é a variável que representa cada elemento do iterável durante a iteração.
# O iterável é a coleção de elementos que você deseja percorrer, como uma lista, um conjunto, um dicionário ou uma string. A condição é opcional e é usada para filtrar os elementos do iterável com base em uma expressão booleana. Se a condição for verdadeira, o item será incluído na lista resultante; caso contrário, ele será ignorado.
# Exemplo 1: Criar uma lista de quadrados de números de 0 a 9 usando list comprehension:
dobros = [i * 2 for i in range(10)]
print(dobros)  # Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Exemplo 2: Criar uma lista de números pares de 0 a 9 usando list comprehension com uma condição:
pares = [i for i in range(10) if i % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]

# Exemplo 3: Criar um generator expression para calcular os quadrados dos números pares de 0 a 9:
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) # Saída: 0
print(next(generator)) # Saída: 4
print(next(generator)) # Saída: 16
print(next(generator)) # Saída: 36
print(next(generator)) # Saída: 64

# Exemplo 4: Iterar sobre o generator expression usando um loop for:
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)