# Crie um script em Python 
# que leia dois números e faça a soma entre eles
def Sum(*Numbers):
    '''This Function returns Sum of all numbers given by parameters'''
    try:
        Sum = 0
        for C in Numbers:
            Sum+=C
        return Sum
    except Exception as Error: print(f'Erro:{Error}')
