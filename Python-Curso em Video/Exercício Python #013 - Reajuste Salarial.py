# Faça um algoritmo que leia o salário de um funcionário e 
# mostre seu novo salário, com 15% de aumento.
def SalaryIncrease(Salary,Increase):
    NewValue= Salary+ (Salary * (Increase/100))
    return NewValue
