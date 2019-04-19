class Party:
	conMP = 0
	listMP = 0

	def __init__(self, name, vote, conOld):
		self.name = name
		self.vote = vote
		self.conOld = conOld

	def getName(self):
		return self.name

	def getVote(self):
		return self.vote

	def getConOld(self):
		return self.conOld

	def getConstituencyMP(self):
		return self.conMP

	def getListMP(self):
		return self.listMP

	def setConstituencyMP(self, conMP):
		self.conMP = conMP

	def addListMP(self):
		self.listMP += 1