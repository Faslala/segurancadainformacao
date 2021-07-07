import random
import string

tamanho = 112345
chars = string.ascii_letters + string.digits + '@#$%*()'
rnd = random.SystemRandom()
print(''.join(rnd.choice(chars) for i in range(tamanho)))
