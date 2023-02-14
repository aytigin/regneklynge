from node import Node

class Rack:
	#Oppretter et rack der det senere kan plasseres noder
	def __init__(self):
		self._rack = [] #liste med noder

	#Plasserer en ny node inn i racket
	def settInnNodeiRack(self, node):
		self._rack.append(node)

	#Henter antall noder i racket
	def getAntNoder(self):
		return len(self._rack)

	#Beregner sammenlagt antall prosessorer i nodene i et rack
	def antProsessoreriRack(self):
		ant_Pros = 0
		for node in self._rack:
			ant_Pros += node.antProsessoreriNode()
		return ant_Pros


	#Beregner antall noder i racket med minne over gitt grense
	def noderMedNokMinne_Rack(self, paakrevdMinne):
		ant_noder_med_nok_minne = 0
		for node in self._rack:
			if node.nokMinne(paakrevdMinne):
				ant_noder_med_nok_minne += 1
		return ant_noder_med_nok_minne
