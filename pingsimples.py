import os

ipouhost = input('Digite um ip ou host para ser verificado: ')

os.system(f'ping -c 6 {ipouhost}')
