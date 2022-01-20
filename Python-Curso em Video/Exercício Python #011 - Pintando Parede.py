# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
from math import ceil
def MeasurementWallInk(Height,Length,InkYield,AmountDemao):
    """This function returns the amount of ink(in liters(L)) will be used to paint a wall.
    Parameters: Height of wall, Length of wall, InkYield per 'demão'(described in tin),
                Amount of 'demão' will be used
    """
    Area = Height * Length
    Yield = Area/(InkYield/AmountDemao)
    return Yield,ceil(Yield)

def MeasurementWallInk2():
    """This function returns the amount tin of ink will be used to paint a wall.
    """
    Rooms = int(input('Quantas cômodos serão pintados?:'))
    Dictionary= {}
    for C in range(1,Rooms+1):
        AmountWalls= int(input(f'Digite a quantidade de paredes do {C}° cômodo:'))
        for D in range(1,AmountWalls+1):
            Height = float(input(f'Digite a altura da {D}° parede [em metros]:'))
            Length = float(input(f'Digite o comprimento da {D}° parede [em metros]:'))
            Answer = input(f'Há algum objeto( porta, janela) nesta parede? [Digite \'sim\' caso tenha]:')
            Area = Length*Height
            if Answer == 'sim':
                Object = float(input('Digite a área do objeto [em metros quadrados]:'))
                Area -= Object 
            else:   continue
            InkYield = float(input('Digite a quantidade de rendimento de tinta a lata proporciona por demão [em metros quadrados]:'))
            AmountDemao = int(input('Digite a quantidade de demãos de tinta que serão passadas:'))
            Result = InkYield/AmountDemao
            Total = Area/ Result         
            Dictionary[f'Quarto{C}']= Total
    return Dictionary
