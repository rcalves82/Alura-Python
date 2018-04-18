# -*- coding: utf-8 -*-

class Data(object):
	"""Classe para imprimir uma data"""

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print '%s/%s/%s' % (self.dia, self.mes, self.ano)
    	
class Pessoa(object):
	"""Classe para calcular IMC"""

	def __init__(self, nome, altura, peso):
		self.nome = nome
		self.altura = altura
		self.peso = peso
		

	def imprime(self):
		IMC = round (self.peso/(self.altura*self.altura))
		if IMC >= 18.5 and IMC <= 25:
			print '%s seu IMC: %s - PESINHO NORMAL FLOR, BICHONA TA INDO PRA ACADEMIA MALHAR CLUTEO?' % (self.nome, IMC)
		elif IMC >= 25.5 and IMC <= 30:
			print '%s seu IMC: %s - TA PESADINHO HEIN, DA UMA SEGURADA NO DESCONTROLE' % (self.nome, IMC)
		elif IMC >= 30.5 and IMC <= 35:
			print '%s seu IMC: %s - Xiiiiii MEU CARO!!! TA GORDO DEMAIS NEGO!!! CONTRATA O GYMPASS, VAI NA MINHA' % (self.nome, IMC)
		elif IMC >= 35.5 and IMC <= 40:
			print '%s seu IMC: %s - SEU CORACAO VAI PARAR AMIGAO, FICA ESPERTO' % (self.nome, IMC)
		elif IMC > 40:
			print '%s seu IMC: %s - CARACA FERA!!! SEU CORACAO AINDA ESTA BATENDO AMIGAO??' % (self.nome, IMC)
		else:
			print '%s seu IMC: %s - VOCE ESTA SO O FIU DA RABIOLA, VOCE JA MORREU E NAO SABE AINDA' % (self.nome, IMC)

class Retangulo(object):
	"""Definir area do Retangulo"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.__area = x * y

	def  obter_area(self):
		return self.__area
			
		