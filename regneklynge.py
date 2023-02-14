from rack import Rack
from node import Node

class Regneklynge:
	#Oppretter tom regneklynge for racks med oppgitt maxtall noder per rack
	def __init__(self, noderPerRack):
		self._regneklynge = [] #liste med racks
		self._noderPerRack = noderPerRack

	#Plasserer en node inn i et rack med ledig plass, eller i et nytt
	def settInnNode(self, node):
		if len(self._regneklynge) != 0 and self._regneklynge[-1].getAntNoder() < self._noderPerRack:
			self._regneklynge[-1].settInnNodeiRack(node)
		else:
			rack = Rack()
			self._regneklynge.append(rack)
			rack.settInnNodeiRack(node)

	#Beregner totalt antall prosessorer i hele regneklyngen
	def antProsessoreriRegneklynge(self):
		ant_pros = 0
		for rack in self._regneklynge:
			ant_pros += rack.antProsessoreriRack()
		return ant_pros

	#Beregner antall noder i regneklyngen med minne over angitt grense
	def noderMedNokMinne(self, paakrevdMinne):
		ant_noder_m_nok_minne = 0
		for rack in self._regneklynge:
			ant_noder_m_nok_minne += rack.noderMedNokMinne_Rack(paakrevdMinne)

		return ant_noder_m_nok_minne


	#Henter antall racks i regneklyngen
	def antRacks(self):
		return len(self._regneklynge)
