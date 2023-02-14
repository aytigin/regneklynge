class Node:
	#Oppretter en node med gitt minne-storrelse og antall prosessorer
	def __init__(self, minne, antPros):
		self._minne = minne
		self._antPros = antPros

	#Henter antall prosessorer i noden
	def antProsessoreriNode(self):
		return self._antPros

	def mengdeMinne(self):
		return self._minne

	#Sjekker om noden har tilstrekkelig minne for et program
	def nokMinne(self, paakrevdMinne):
		if self._minne == paakrevdMinne:
			return True
		elif self._minne > paakrevdMinne:
			return True
		else:
			return False
