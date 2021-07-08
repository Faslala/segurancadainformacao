import itertools

texto = input('Digite um texo para ser permutado: ')
resultado = itertools.permutations(texto, len(texto))
for i in resultado:
    print(''.join(i))

