"""
5) Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e
saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No
construtor, saldo é opcional, com valor default zero e os demais atributos
são obrigatórios.
"""

class ContaCorrente:

	def __init__(self, nro_conta, nome_do_correntista, saldo=0.0):
		self.nro_conta = nro_conta;
		self.nome_do_correntista = nome_do_correntista;
		self.saldo = saldo;

	def alterarNome(self, nome_do_correntista):
		self.nome_do_correntista = nome_do_correntista;

	def deposito(self, deposito):
		self.saldo=self.saldo + deposito;

	def saque(self, saque):
		self.saldo = self.saldo - saque

# Teste ContaCorrente

conta1 = ContaCorrente(1, "Joaquim", 1500);
conta2 = ContaCorrente(2, "Marina", 500);
conta3 = ContaCorrente(3, "Marcelly");

conta1.deposito(3000);
print(conta1.saldo);
conta2.saque(50);
print(conta2.saldo);
conta3.deposito(2000);
print(conta3.saldo);
conta2.deposito(2000);
print(conta1.saldo);
conta3.saque(50);
print(conta2.saldo);
conta2.deposito(210);
print(conta3.saldo);
