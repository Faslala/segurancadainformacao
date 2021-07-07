import hashlib

hashesA = 'hashesA.txt'
hashesB = 'hashesB.txt'

hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

hash1.update(open(hashesA, 'rb').read())
hash2.update(open(hashesB, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {hashesA} é diferente do arquivo {hashesB}')
else:
    print(f'O arquivo {hashesA} é igual do arquivo {hashesB}')

print(f'Um hash é ', hash1.hexdigest(), '\ne o outro bash é ' + hash2.hexdigest())

