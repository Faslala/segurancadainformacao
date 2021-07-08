import hashlib

texto = (input('Digite um texo para ser criado um hash: '))
# resultado = hashlib.md5(texto.encode('utf-8')).hexdigest()
print('Existem várias formas de codificaćão:\n')
print('   md5: ',    hashlib.md5(texto.encode('utf-8')).hexdigest())
print('  sha1: ',   hashlib.sha1(texto.encode('utf-8')).hexdigest())
print('sha256: ', hashlib.sha256(texto.encode('utf-8')).hexdigest())
print('   md5: ',    hashlib.sha512(texto.encode('utf-8')).hexdigest())
