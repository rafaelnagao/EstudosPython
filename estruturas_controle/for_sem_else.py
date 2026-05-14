PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        print('Texto possui pelo menos uma palavra proibida: ', palavra)
        found = True
        break

    if not found:
        print('Texto autorizado: ', texto)