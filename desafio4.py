"""
4) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
area=0
while area<=0:
	area=float(input("Digite o tamanho em metros quadrados da área a ser pintada (maior que 0): "));

valor_total=0;
litros=area//3;
qtd_latas=0;
if area%3>0:
	litros+=1;
qtd_latas = litros//18;
if litros%18 > 0:
	qtd_latas+=1;
valor_total = qtd_latas*80;

print("Para pintar uma area de",area,"metros quadrados, você precisará de",int(qtd_latas),"latas de tinta. O valor total será de R$ %.2f"%valor_total);
