# AMS Election
Calculating an approximation of the House of Commons using the Additional Member System.

## Reasoning
The devolved parliament of Scotland, as well as the devolved assemblies for Wales and London, all use the Additional Member System (AMS) to assign representatives to seats.

Instead of having a single vote, the vote for your local Member of Parliament for your constituency, you also have a second vote; this is the 'party vote'.
The idea behind AMS is to have local representation with your constituency MP, whilst attempting to keep proportionality with the overall vote of the area.
An MP is either a constituency MP, or a 'List MP', one that is elected from a party's list of candidates that they field for the party vote.

This program is designed to take in results for set regions of the UK and attempt to convert them to what the result could look like under AMS.

## Assumptions
The flavour of AMS used here is akin to that seen in the Scottish and Welsh devolved elections, where regions are given a set number of party vote MPs to elect.

We will assume: 
- The party vote is the popular vote for a party in a given region 
- There are 650 MPs elected to the House of Commons
	- 400 of these are from constituencies
	- 250 of these are for regional list MPs
- The number of list MPs for each region is based on local population
	- 32 for London
	- 34 for South East England
	- 21 for South West England
	- 23 for East of England
	- 18 for East Midlands
	- 22 for West Midlands
	- 21 for Yorkshire and the Humber
	- 10 for North East England
	- 28 for North West England
	- 12 for Wales
	- 22 for Scotland
	- 7 for Northern Ireland
- The number of constituency MPs for a given region is a proportion of the currently elected MPs for that region
	- If there are constituency seats left unfilled, give these seats to parties in accordance with the Scottish version of the D'Hondt method
- List MPs are assigned using the Scottish version of the D'Hondt method to ensure proportionality

## Drawbacks
- Proportionally assigning constituency seats that are left over defeats the purpose of FPTP constituency seats
	- Can also lead to some parties that wouldn't have a majority gain a constituency seat which they wouldn't win in the traditional FPTP system
	- Also leads to smaller parties losing seats that they wouldn't (sorry Brighton Pavilion!)
