"""Bacteria Culture Simulation
Aim
Code up a simple model that calculates the growth of a certain species of bacteria (BitBact) over a period of time, given the initial state.
 
Description 
A newly discovered species of bacteria named BitBact reproduces as per the following rules
The time unit used for this simulation is 1 second 
Every bacterium splits into K new bacterium after RC seconds. [RC : Reproductive cycle]
Once a bacterium splits, each of the K new bacterium have CD seconds of cooldown time before they can start their reproductive cycle. [CD = cooldown]
After CD days, each of these K bacteria split into K new ones after (the usual) RC days.
Input
An integer array (InitCulture) consisting of what age each bacterium is in. e.g [1,4,2,6,7] means at the start we have 5 bacterium at an age of 1,4,2,6,7 seconds respectively.
An integer (SimTime) representing number of seconds for which we need to run the simulation.
Values of RC, CD
Output
An Integer representing the total number of bacteria present at the end of the simulation.

Example Simulation
 
Input :
InitCulture = [1,3] | SimTime = 10 |  RC = 5 | CD = 2

spawn_count = {
			count *= 2
			}

Simulation
after 1 sec => [2,4]
after 2 sec => [3,5]
after 3 sec => [4, 0, 0]
after 4 sec => [5, 0, 0]
after 5 sec => [0, 0, 1, 1]
after 6 sec => [0, 0, 2, 2]
after 7 sec => [1, 1, 3, 3]
after 8 sec => [2, 2, 4, 4]
after 9 sec => [3, 3, 5, 5]
after 10 sec => [4, 4, 0, 0, 0, 0]
 
OUTPUT
6"""
from typing import List
from collections import defaultdict

def bacteria_reproduction(init_culture: List, simtime: int, rc: int, cd: int) -> int:
	"""
	Calculates the bacteria reproduction rate
	"""
	culture = init_culture.copy()
	cd_state = defaultdict(int)
	current_lenght = len(culture)
	expired_index = []
	#Simulation Loop
	for time in range(simtime):
		for index, value in enumerate(culture):
			#Spawn Check
			if value == rc:
				cd_state[index] = cd - 1
				culture[index] = 0
				culture.append(0)
				cd_state[current_lenght] = cd - 1
				current_lenght += 1
			if index not in cd_state.keys():
				culture[index] += 1
		#Cooldown Check
		for i in cd_state.keys():
			if cd_state[i] != 0:
				cd_state[i] -= 1
			else:
				expired_index.append(i)
		for i in expired_index:
			del cd_state[i]
		expired_index = []
	return len(culture)


def bacteria_reproduction_v2(init_culture: List, simtime: int, rc: int, cd: int) -> int:
	"""
	Calculates the bacteria reproduction rate
	"""
	culture = {}
	# create the culture dict structure
	for i in range(len(init_culture)):
		culture[i] = {
  			'value': init_culture[i],
  			'count': 1,
  			'cd': 0
	 	}
	#Simulation Loop
	for time in range(simtime):
		for culture_key in culture.keys():
			#Cooldown Check
			if culture[culture_key]['cd'] > 0:
				culture[culture_key]['cd'] -= 1
				continue
			#Spawn Check
			if culture[culture_key]['value'] >= rc:
				culture[culture_key]['value'] = 0
				culture[culture_key]['count'] *= 2
				culture[culture_key]['cd'] = cd - 1
			else:
				culture[culture_key]['value'] += 1
	#sum of count of culture
	return sum([i['count'] for i in culture.values()])



InitCulture = [1,3]
SimTime = 10
RC = 5
CD = 2
print(bacteria_reproduction_v2(InitCulture, SimTime, RC, CD))


InitCulture = [1, 2, 3, 4, 1]
SimTime = 100
RC = 5
CD = 2
print(bacteria_reproduction_v2(InitCulture, SimTime, RC, CD))


InitCulture = [1, 2, 3, 4, 1]
SimTime = 200
RC = 5
CD = 2
print(bacteria_reproduction_v2(InitCulture, SimTime, RC, CD))


InitCulture = [1, 2, 3, 4, 1]
SimTime = 2000
RC = 5
CD = 2
print(bacteria_reproduction_v2(InitCulture, SimTime, RC, CD))


InitCulture = [1, 2, 3, 4, 1]
SimTime = 100000
RC = 5
CD = 2
print(bacteria_reproduction_v2(InitCulture, SimTime, RC, CD))