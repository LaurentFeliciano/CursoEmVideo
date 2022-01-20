# crie um script em python que leia o dia, 
# o mês e o ano de nascimento de uma pessoa 
# e mostre uma mensagem com a data formatada
def FormatDate():
    '''That Function returns Birth Date of user in DateTime format.  '''
    import datetime
    while True:
        try:
            CurrentDate= datetime.datetime.now()

            Year=input('Digite o ano do seu nascimento(formato ####):')
            while len(Year) != 4 or int(Year)> CurrentDate.year :
                Year=input('Digite o ano do seu nascimento da maneira correta(formato ####):')

            Month=input('Digite o mês do seu nascimento(formato #):')
            while len(Month) < 1 or len(Month) > 2 or int(Month)> 12 or int(Month)<1 :
                Month=input('Digite o mês do seu nascimento da maneira correta(formato ## ou #):')  

            Day= input('Digite o dia do seu nascimento(formato ## ou #):')
            while len(Day) < 1 or len(Day) > 2:
                Day = input('Digite o dia do seu nascimento da maneira correta(formato ## ou #):')

            Date = datetime.datetime(int(Year),int(Month),int(Day))

            return Date
        except Exception as Error:print(f'Erro: {Error}')
