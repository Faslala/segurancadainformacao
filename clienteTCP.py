import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!')
        print(f'Error: {e}')
        sys.exit()
    print('Socket criado com sucesso!')


    HostAlvo = input('Digite um host ou ip a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f'Cliente TCP conectado com sucesso no host {HostAlvo} e na porta {PortaAlvo}')
        s.shutdown(3)
    except socket.error as e:
        print('A conexão falhou!!')
        print(f'Error {e}')
        sys.exit()

if __name__ == '__main__':
    main()

