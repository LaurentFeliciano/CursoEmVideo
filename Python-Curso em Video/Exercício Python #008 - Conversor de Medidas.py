# Escreva um programa que leia um valor em metros e o 
# exiba convertido em centímetros e milímetros.
def MeasurementConverter(Value):
    while True:
        try:
            Question = int(input('''
            Painel de conversões de medidas(A partir do metro):
            Comprimento:
            Quilômetro(km) – [3]
            Hectômetro(hm) – [2]
            Decâmetro (dam)– [1]
            Metro     (m)  – [0]
            decímetro (dm) – [-1]
            centímetro(cm) – [-2]
            milímetro (mm) – [-3]
            Deseja converter para qual das medidas acima:'''))
            while Question >3 or Question< -3:
                Question = int(input('Digite um dos números acima:'))
            if Question <0: Answer = Value / (10**abs(Question))
            else: Answer = Value * (10**Question)
            return Answer
        except Exception as Error: print(f'Erro:{Error}')
