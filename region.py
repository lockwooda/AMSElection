from party import Party
import csv
import math
import copy

class Region:

	def __init__(self, name, file, conMPs, listMPs):
		self.name = name
		self.file = file
		self.conMPs = conMPs
		self.listMPs = listMPs
		self.parties = []
		self.readFile()

	def getName(self):
		return self.name

	def addParty(self, party):
		self.parties.append(party)

	def readFile(self):
		with open(self.file) as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			lineCount = 0
			for row in reader:
				self.addParty(Party(row[0], int(row[1]), int(row[2])))

	def convertToAMS(self):
		allVotes = 0
		leftOverMPs = self.conMPs
		newConMPs = []

		for x in range(0, len(self.parties)):
			allVotes += self.parties[x].getVote()
			newConMPs.append(math.floor(self.parties[x].getConOld() / float(self.conMPs + self.listMPs) * self.conMPs))
			leftOverMPs -= newConMPs[x]

		votes = list(map(lambda x: x.getVote(), self.parties))
		if(leftOverMPs > 0):
			newConMPs = self.dHondtConMethod(leftOverMPs, newConMPs, votes)

		newListMPs = self.dHondtListMethod(self.listMPs, copy.copy(newConMPs), votes)
		newMPs = [sum(x) for x in zip(newConMPs, newListMPs)]
		return list(zip(map(lambda x: x.getName(), self.parties), newConMPs, newListMPs))

	def dHondtConMethod(self, seatsLeft, seats, votes):
		while (seatsLeft > 0):
			maxValue = -1
			seatToAdd = 0
			for x in range(0, len (seats)):
				if(seats[x] > 0 and (votes[x] / (seats[x] + 1)) > (votes[seatToAdd] / (seats[seatToAdd] + 1))):
					seatToAdd = x
			seats[seatToAdd] += 1
			seatsLeft -= 1
		return seats

	def dHondtListMethod(self, seatsLeft, seats, votes):
		newListMPs = [0] * len(votes)
		# Whilst there are seats to assign, check values
		while (seatsLeft > 0):
			maxValue = -1
			seatToAdd = 0
			# For each set for values, compare the D'Hondt value to the current maximum
			for x in range(0, len (seats)):
				if(votes[x] / (seats[x] + 1)) > (votes[seatToAdd] / (seats[seatToAdd] + 1)):
					seatToAdd = x
			newListMPs[seatToAdd] += 1
			seats[seatToAdd] += 1
			seatsLeft -= 1
		return newListMPs 