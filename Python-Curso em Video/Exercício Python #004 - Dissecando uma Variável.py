# Faça um programa que leia algo pelo teclado e mostre na tela o seu 
# tipo primitivo e todas as informações possíveis sobre ele.
def Informations(Value):
    '''This function returns informations about the specified value.'''
    Dictionary = dict()
    Dictionary['Type']= type(Value)
    Dictionary['IsNumeric']= Value.isnumeric()
    Dictionary['IsLower']= Value.islower()
    Dictionary['IsUpper']= Value.isupper()
    Dictionary['IsTitle']= Value.istitle()
    Dictionary['IsSpace']= Value.isspace()
    Dictionary['IsAlpha']= Value.isalpha()
    Dictionary['IsAlphanum']= Value.isalnum()
    return Dictionary
