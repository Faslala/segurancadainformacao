from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto} KM {trajeto}       ')


t_carro = Thread(target=carro, args=[1.0, 'Benjamin'])
t_carroa = Thread(target=carro, args=[1.5, 'Bernardo'])

t_carro.start()
t_carroa.start()