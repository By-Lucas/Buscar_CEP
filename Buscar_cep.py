"""
BUSCAR CEP DOS ESTADOS
EM CASOS DE ERROS SERÁ USADO LOOP while PARA REPETIÇÃO.
E ADICIONADO ERRO AO DIGITAR CEP INCORRETO

GITHUB = https://github.com/by-lucas
LINKEDIN = https://www.linkedin.com/in/lucastk/
WHATISAPP = 74981199190 PARA CONTRATAR FREELANCER
"""


# BIBLIOTECAS
import requests
import os
import sys

os.system('cls')

while True:
    try:
        cep = input("Digite seu CEP: ")

        if len(cep) != 8:
            print("[+] O CEP deve conter apenas 8 digitos.\n")
            novamente = input("Deseja tentar novamente?\nDigite S para sim ou N para não: ").upper()
        else:
            break
    except:
        print('\n Opção invalida')

    if novamente == 'S':
        continue
    elif novamente == 'N':
        print("Até mais...")
        exit()
    else:
        print("\nOpção digitada é invalidada!\nTente novamente:\n")

r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

# Convertendo dados
data = r.json()

# Mostrandos dados encontrados ou CEP inválido
if 'erro' not in data:
    print("\n[+] Dados do CEP encontado.\n")
    print("| Estado: {}".format(data['uf']))
    print("| CEP: {}".format(data['cep']))
    print("| Cidade: {}".format(data['localidade']))
    print("| Logradouro: {}".format(data['logradouro']))
    print("| Complemento: {}".format(data['complemento']))
    print("| Bairro: {}".format(data['bairro']))
else:
    print("O CEP {} não é válido!".format(cep))
