#! python
produto = {'nome': 'Caneta Chic', 'preco': 14.90, 'estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave}: {valor}')

print(chave, valor)