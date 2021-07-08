import phonenumbers
from phonenumbers import geocoder

phone = input('Digite um número de telefone no formato +5599999999999: ')
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
