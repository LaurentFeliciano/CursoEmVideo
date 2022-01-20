# Crie um programa que leia quanto dinheiro uma pessoa tem na 
# carteira e mostre quantos dólares ela pode comprar.

# Made by morphetux
# https://wiki.python.org.br/CotacaoDolar

import requests
import json


def DollToday(Value):
    """This function returns the buy and sell price of dollar today as tuple(in brazillian real)
    *Attencion*
    It's necessary download the "request" library in your python project through pip installer
    """
    try:
        Request = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        Price = Request.json()
        Coin  = Price['USD']['name']
        Date = Price['USD']['create_date']
        DollToday =Price['USD']['bid']
        return Value*float(DollToday)
    except Exception as Error: print(f'Erro:{Error}')