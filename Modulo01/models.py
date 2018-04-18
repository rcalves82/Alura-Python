# -*- coding: utf-8 -*-
class Perfil(object):
	"""Classe para moldar perfis de usuarios"""

	def __init__(self, nome, telefone, empresa):
		if(len(nome) < 3):
			raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')        	
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0
		
		
	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s, Numero de Curtidas: %s' % (self.nome, self.telefone, self.empresa, self.__curtidas)

	def curtir(self):
		self.__curtidas += 1

	def obter_curtidas(self):
		return self.__curtidas		

	def obter_tipo(self):
		return self.__tipo

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			if(len(valores) is not 3):
				raise ArgumentoInvalidoError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis


class Perfil_Vip(Perfil):
	"""Essa classe acrescente créditos para perfil VIP"""
	def __init__(self, nome, telefone, empresa, apelido = ''):

		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0

class ArgumentoInvalidoError(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)
	
		