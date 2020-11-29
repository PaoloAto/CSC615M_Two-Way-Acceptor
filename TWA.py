import csv
import time

#Method for inserting the hastags '#' in the first and last index to simulate the tape
def insert_hashtag(string, index):
	return string[:index] + '#' + string[index:]

#Method for inserting an arrow "->" to indicate position in the tape
def insert_pointer(string, index):
	return string[:index] + "->" + string[index:]

#Simulates the TWA machine 
class TWA:
	def __init__(self, states):
		self.states = states

	def simulateMachine(self, test):
		self.currPosition = 1

		# temp = test
		# # print(f"Temporary String Test: {temp}")
		# temp = insert_pointer(temp, 1)
		# print(f"Tape Input: {temp}")

		# Starts at state 1
		self.currentState = 1
		
		try:
			#while loop runs as long as the accept and reject states are not yet reached
			inv = ''
			while self.states[self.currentState].getMove() != 'accept' and self.states[self.currentState].getMove() != 'reject':
				time.sleep(1.5)
				print("==============================================================================")
				print(f"Currently at State: {str(self.currentState)}")

				char = test[self.currPosition]
				inv = char
				print(f"Input: {char}")
				transition = self.states[self.currentState].getTransition(char)
				self.currentState = int(transition)

				print(f"Moving to State: {str(transition)}")
				if (self.states[self.currentState].getMove() == 'right' or self.states[self.currentState].getMove() == 'left'):
					print(f"Action: Moving arrow to the {self.states[self.currentState].getMove()}")
				else:
					print("Action: Last State Reached")

				if self.states[self.currentState].getMove() == 'right':
					self.currPosition += 1
				elif self.states[self.currentState].getMove() == 'left':
					self.currPosition -= 1

			print(f"Result of the input: {self.states[self.currentState].getMove()}")
			print("==============================================================================")
		except KeyError:
			print(f"Invalid Character '{inv}' Found (Not in List of Accepted Input Characters)")
			print("Input is Rejected for this TWA")
			print("==============================================================================")

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
with open(test1) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	state_count = 0
	states = {}
	print ("=========TWO WAY ACCEPTER SIMULATION=========")
	print(f"Loading TWA File: {test1}")

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

#Main Program
# eval = "aabb"
eval = input("Enter String: ") 

eval = insert_hashtag(eval, 0)
eval = insert_hashtag(eval, len(eval))

print(f"Evaluating String: {eval}")

sm = TWA(states)
sm.simulateMachine(eval)
