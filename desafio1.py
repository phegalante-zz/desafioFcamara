"""Um funcionário de uma empresa recebe, anualmente, aumento salarial.
Sabe-se que:
Esse funcionário foi contratado em 2005 com salário inicial de R$ 1.000,00;
Em 2006 ele recebeu aumento de 1,5% sobre seu salário inicial; e
A partir de 2007, os aumentos salariais sempre corresponderam ao dobro
do percentual do ano anterior.
Faça um algoritmo que determine o salário atual deste funcionário."""

from datetime import datetime

sal_base = 1000;
aumento = 0.015;
anoatual = datetime.now();
anoatual = anoatual.year;
for i in range(2006,anoatual+1):
	sal_base = sal_base+(sal_base*aumento);
	aumento=aumento*2;
print("O salário atual desse funcionário é de R$ %.2f"%sal_base);