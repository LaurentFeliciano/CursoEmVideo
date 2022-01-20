# Faça um programa que leia um número Inteiro qualquer 
# e mostre na tela a sua tabuada.
Num= int(input('Digite um número:'))
for C in range(1,11):
    print(f'{Num}*{C}={Num*C}')