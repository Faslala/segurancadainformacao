import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
resposta = urlopen(url)
dados = json.load(resposta)

print(dados)
print(dados['ip'])
