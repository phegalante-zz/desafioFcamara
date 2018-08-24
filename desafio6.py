"""
6) Crie uma classe que modele um retângulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a
escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
informe as medidas de um local. Depois, deve criar um objeto com as
medidas e calcular a quantidade de pisos e de rodapés necessárias para o
local.
"""
import math

class Retangulo:

	def __init__ (self, base, altura):
		self.base = base;
		self.altura = altura;

	def setBase(self, base):
		self.base = base;

	def setAltura(self, altura):
		self.altura = altura;

	def getAltura(self):
		return self.altura;

	def getBase(self):
		return self.base;

	def calcArea(self):
		area = self.base*self.altura;
		return area;

	def calcPerimetro(self):
		perimetro = 2 * self.base + 2 * self.altura;
		return perimetro;





def main():

	altura = float(input("Digite o comprimento do LOCAL (em metros): "));
	base = float(input("Digite a base do LOCAL (em metros): "));
	local = Retangulo(base, altura);
	print("\n");
	altura = float(input("Digite o comprimento do PISO (em centímetros): "));
	base = float(input("Digite a base do PISO (em centímetros): "));
	piso = Retangulo(base/100, altura/100);
	print("\n");
	qtd_pisos_area = local.calcArea()/piso.calcArea();

	print("Você precisará de %.2f"%qtd_pisos_area,"pisos para a área do local informado.");
	print("Porém, estudos da engenharia civil recomendam uma margem de 10% de segurança para eventuais imprevistos...");

	qtd_pisos_area += qtd_pisos_area*0.1
	print("Sugiro que você compre:",math.ceil(qtd_pisos_area), "pisos para a área do local informado.");

	print("\n");
	altura_rodape = float(input("Digite a altura do rodapé (em centímetros): "));
	qtd_pisos_rodape = local.calcPerimetro() * (altura_rodape/100);
	qtd_pisos_rodape = qtd_pisos_rodape/piso.calcArea();

	print("Você precisará de %.2f"%qtd_pisos_rodape,"pisos para o rodapé do local informado.");
	qtd_pisos_rodape += qtd_pisos_rodape*0.1
	print("Adicionando os 10% recomendados pelos engenheiros civil, como margem de segurança, você precisará de:",math.ceil(qtd_pisos_rodape), "pisos para o rodapé do local informado.");

	print("\n");

	print("No total, você precisará de: ",math.ceil(qtd_pisos_rodape+qtd_pisos_area), "pisos para a área e para o rodapé desta obra.");

if __name__ == '__main__':
    main()


"""
	#Teste Retangulo

retangulo1 = Retangulo(40, 20);
print (retangulo1.base);
print (retangulo1.altura);
retangulo2 = Retangulo(213, 120);
print (retangulo2.base);
print (retangulo2.altura);
retangulo3 = Retangulo(112, 42);
print (retangulo3.base);
print (retangulo3.altura);
retangulo3.setAltura(155);
retangulo3.setBase(194);
print (retangulo3.base);
print (retangulo3.altura);
print ("\n");
print(retangulo1.calcArea());
print(retangulo2.calcPerimetro());
"""