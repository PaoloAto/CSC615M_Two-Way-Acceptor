import csv
import time

#Method for inserting the hastags '#' in the first and last index to simulate the tape
def insert_hashtag(string, index):
	return string[:index] + '#' + string[index:]

#Simulates the TWA machine 
class TWA:
	def __init__(self, states):
		self.states = states

	def simulateMachine(self, test):
		# Starts at state 1
		self.currPosition = 1
		self.currState = 1
		moveCtr = 0
		
		try:
			#while loop runs as long as the accept and reject states are not yet reached
			inv = ''
			while self.states[self.currState].getMove() != 'accept' and self.states[self.currState].getMove() != 'reject':
				time.sleep(1.5)
				print("==========================================")
				print(f"Currently at State: {str(self.currState)}")

				char = test[self.currPosition]
				inv = char
				print(f"Input: {char}")
				transition = self.states[self.currState].getTransition(char)
				self.currState = int(transition)

				print(f"Moving to State: {str(transition)}")
				if (self.states[self.currState].getMove() == 'right' or self.states[self.currState].getMove() == 'left'):
					print(f"Action: Moving arrow pointer to the {self.states[self.currState].getMove()}")
				else:
					print("Action: Last State Reached")
					moveCtr += 1

				if self.states[self.currState].getMove() == 'right':
					self.currPosition += 1
					moveCtr += 1
				elif self.states[self.currState].getMove() == 'left':
					self.currPosition -= 1
					moveCtr += 1

			print("==========================================")
			print(f"Number of total moves taken: {moveCtr}")
			print(f"Result of the input: {self.states[self.currState].getMove().upper()}")
			print("==========================================")
		except KeyError:
			print(f"Invalid Character '{inv}' Found (Not in List of Accepted Input Characters)")
			print("Input is Rejected for this TWA")
			print("==========================================")

#Object that holds the information of each state from the CSV File
class State:
	def __init__(self, stateNo, move):
		self.stateNo = stateNo
		self.move = move
		self.transitions = {}

	def getIndex(self,stateNo):
		return self.stateNo

	def getMove(self):
		return self.move

	def getTransition(self, char):
		return self.transitions[char]

	def setTransition(self, transition):
		self.transitions[transition[0]] = int(transition[1])

#TWA CSV Files 
test1 = "Even-a.csv"
test2 = "Even-ab.csv"
test3 = "Even-a_Odd-b.csv"
test4 = "5a_3b.csv"
test5 = "3a_More-b.csv"

#Open CSV Files
with open(test3) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	state_count = 0
	states = {}
	print ("======= TWO WAY ACCEPTER SIMULATION ======")
	print(f"Loading TWA File: {test3}")

	# CSV FORMAT: row[0] = state number, row[1] = action taken, row [2] = char input and transitions
	for row in csv_reader:
		stateNo = int(row[0])
		move = row[1]
		if stateNo not in states:
			states[stateNo] = State(stateNo, move)
		for index in range(2, len(row)):
			transition = row[index]
			if transition != '':
				transition = transition.split(',')
				states[stateNo].setTransition(transition)
		state_count += 1
	print(f'Finished loading {state_count} number of states.')
	print("==========================================")

#Main Program
# eval = "aabb"
eval = input("Enter String: ") 

eval = insert_hashtag(eval, 0)
eval = insert_hashtag(eval, len(eval))

print(f"Evaluating String: {eval}")

sm = TWA(states)
sm.simulateMachine(eval)
