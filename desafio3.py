"""
3) Receba o número de horas trabalhadas por uma pessoa e o valor do salário mínimo e mostre o salário a receber baseado nas seguintes regras:
A hora trabalhada equivale a 10% do salário mínimo informado;
O salário bruto é dado pelo número de horas trabalhadas multiplicado pelo valor de cada hora;
O imposto pago é de 3%.
O salário a receber é equivalente ao salário bruto subtraído do imposto.
"""

horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "));
valor_sal_min = int(input("Digite o valor do salário mínimo: "));

salario_bruto = horas_trabalhadas*(valor_sal_min*0.1);
salario_receber = salario_bruto-(salario_bruto*0.03);

print("O salário a receber é de R$",salario_receber);