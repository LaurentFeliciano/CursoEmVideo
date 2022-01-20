#  Faça um algoritmo que leia o preço de um produto 
#  e mostre seu novo preço, com 5% de desconto.

def Sale(Value):
    NewValue= Value + (Value * (5/100))
    return NewValue
