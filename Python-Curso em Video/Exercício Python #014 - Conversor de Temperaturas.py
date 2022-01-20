# Escreva um programa que converta uma temperatura digitando 
# em graus Celsius e converta para graus Fahrenheit.

def TemperatureConversion(Value):
        try:
            Question = int(input('''
            Painel de conversões de Temperaturas:
            Celcius (°C) – [1]
            Kelvin(°K) – [2]
            Fahrenheit(°F)– [3]
            Rankine(°Ra)  – [4]

            Qual será o tipo de temperatura que será recebido?:'''))
            while Question >4 or Question< 1:
                Question = int(input('Digite um dos números acima:'))
            Question2 = int(input('''
            Painel de conversões de Temperaturas:
            Celcius (°C) – [1]
            Kelvin(°K) – [2]
            Fahrenheit(°F)– [3]
            Rankine(°Ra)  – [4]

            Para qual temperatura será convertido?:'''))

            if Question == Question2:
                return Question

            if Question == 1:
                if Question2 ==2:
                    NewValue = Value + 273.15
                elif Question2 ==3:
                    NewValue = Value * 1.8 + 32
                else:
                    NewValue = Value * 1.8 + 32 + 459.67

            elif Question == 2:
                if Question2 == 1:
                    NewValue = Value - 273.15
                elif Question2 ==3:
                    NewValue = Value * 1.8 - 459.67
                else:
                    NewValue = Value * 1.8      

            elif Question == 3:   
                if Question2 == 1:
                    NewValue = (Value - 32) / 1.8
                elif Question2 == 2:
                    NewValue = (Value + 459.67) / 1.8
                else:
                    NewValue = Value + 459.67

            elif Question == 4:
                if Question2 == 1:
                    NewValue = (Value - 32 - 459.67) / 1.8
                elif Question2 == 2:
                    NewValue = Value / 1.8
                else:
                    NewValue = Value - 459.67

            return NewValue
            
        except Exception as Error: print(f'Erro:{Error}')
    
print(TemperatureConversion(30))