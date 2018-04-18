# -*- coding: utf-8 -*-

class Conta(object):
	"""Classe para inserção de contas"""
	def __init__(self, titular, saldo):
		self.titular = titular
		self.saldo = saldo

	def calcular_imposto(self):
		imposto = self.saldo * 0.10
		return imposto

class  ContaCorrente(Conta):
	"""Classe Conta_Corrente"""
	def __init__(self, titular, saldo, bonus):
		super( ContaCorrente, self).__init__(titular, saldo)
		self.bonus = bonus
	
	def calcular_imposto(self):
		return super(ContaCorrente, self).calcular_imposto() + self.bonus

		
		
