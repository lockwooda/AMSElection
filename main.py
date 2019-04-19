from party import Party
from region import Region

def main():
	east_england = Region("East of England", "data/east_england.csv", 35, 23)
	east_midlands = Region("East Midlands", "data/east_midlands.csv", 28, 18)
	london = Region("London", "data/london.csv", 41, 32)
	north_east_england = Region("North East England", "data/north_east_england.csv", 19, 10)
	north_west_england = Region("North West England", "data/north_west_england.csv", 47, 28)
	northern_ireland = Region("Northern Ireland", "data/northern_ireland.csv", 11, 7)
	scotland = Region("Scotland", "data/scotland.csv", 37, 22)
	south_east_england = Region("South East England", "data/south_east_england.csv", 50, 34)
	south_west_england = Region("South West England", "data/south_west_england.csv", 34, 21)
	wales = Region("Wales", "data/wales.csv", 28, 12)
	west_midlands = Region("West Midlands", "data/west_midlands.csv", 37, 22)
	yorkshire_humber = Region("Yorkshire and the Humber", "data/yorkshire_humber.csv", 33, 21)

	regions = []
	regions.append(east_england)
	regions.append(east_midlands)
	regions.append(london)
	regions.append(north_east_england)
	regions.append(north_west_england)
	regions.append(northern_ireland)
	regions.append(scotland)
	regions.append(south_east_england)
	regions.append(south_west_england)
	regions.append(wales)
	regions.append(west_midlands)
	regions.append(yorkshire_humber)

	computedRegions = []
	for x in regions:
		computed = x.convertToAMS()
		computedRegions.append(computed)
		print(x.getName())
		for y in computed:
			print(y[0] + "\t" + "Constituency MPs: " + str(y[1]) + "   List MPs: " + str(y[2]))
		print()
	computeUKWide(computedRegions)

def computeUKWide(computedValues):
	isEmptyList = False
	print("United Kingdom")
	while(not isEmptyList):
		conMP = 0
		listMP = 0
		party = computedValues[0][0][0]
		for x in computedValues:
			values = list(filter(lambda y: y[0] == party, x))
			if(len(values) > 0):
				conMP += values[0][1]
				listMP += values[0][2]
		print(party + "\t" + "Constituency MPs: " + str(conMP) + "   List MPs: " + str(listMP))

		newComputedValues = []
		for x in computedValues:
			values = list(filter(lambda y: y[0] != party, x))
			if(len(values) > 0):
				newComputedValues.append(values)
		if len(newComputedValues) > 0:
			computedValues = newComputedValues
		else:
			isEmptyList = True

if __name__ == "__main__":
	main()