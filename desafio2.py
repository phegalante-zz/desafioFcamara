""" 
2) Elabore um algoritmo para mostrar os números primos existentes em um
intervalo.
O usuário deverá fornecer os valores inicial (inicial > 0) e final (inicial <
final) e os números primos existentes no intervalo ([inicial, final]) devem
ser separados por um espaço em branco
Exemplo:
Entrada: 2 13
Saída: 2 3 5 7 11 13
"""

def eprimo(x):
	cont=0;
	e_primo=True
	if x==1:
		e_primo=False;
	else:
		for i in range(int((x+1)/2)):
			if x%(i+1)==0:
				cont=cont+1;
			if cont >1:
				e_primo=False;
				break;
		return e_primo

num_primo = [];
valor_inicial = 0;
valor_final = 0;

while(valor_inicial <1):
	valor_inicial = int(input("Digite um número maior do que zero para o valor inicial : "));

while (valor_final <= valor_inicial):
	valor_final = int(input("Digite um número maior do que o valor inicial para o valor final : "));

for i in range(valor_inicial, valor_final+1):
	e_primo = eprimo(i);
	if e_primo==True:
		num_primo.append(i)

print(" ".join(str(x) for x in num_primo));