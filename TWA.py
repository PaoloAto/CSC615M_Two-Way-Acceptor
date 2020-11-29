import csv

#Method for inserting the hastags '#' in the first and last index to simulate the tape
def insert_hashtag(string, index):
	return string[:index] + '#' + string[index:]

#Method for inserting an arrow "->" to indicate position in the tape
def insert_pointer(string, index):
	return string[:index] + "->" + string[index:]

#Simulates the TWA machine 
class StateMachine:
	def __init__(self, states):
		self.states = states

	def eval(self, test):
		self.arrow = 1

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
				print("==============================================================================")
				print(f"Currently at State: {str(self.currentState)}")

				char = test[self.arrow]
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
					self.arrow += 1
				elif self.states[self.currentState].getMove() == 'left':
					self.arrow -= 1

			print(f"Result of the input: {self.states[self.currentState].getMove()}")
			print("==============================================================================")
		except KeyError:
			print(f"Invalid Character '{inv}' Found (Not in List of Accepted Input Characters)")
			print("Input is Rejected for this TWA")
			print("==============================================================================")

#Object that holds the information of each state from the CSV File
class State:
	def __init__(self, sid, move):
		self.sid = sid
		self.move = move
		self.transitions = {}

	def getIndex(self,sid):
		return self.sid

	def addTransition(self, transition):
		self.transitions[transition[0]] = int(transition[1])

	def getTransition(self, symbol):
		return self.transitions[symbol]

	def getMove(self):
		return self.move

#TWA CSV Files 
test1 = "Even-a.csv"
test2 = "Even-ab.csv"
test3 = "Even-a_Odd-b.csv"
test4 = "5a_3b.csv"
test5 = "3a_More-b.csv"

#Open CSV Files
with open(test1) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	states = {}
	print ("=========TWO WAY ACCEPTER SIMULATION=========")
	print(f"Loading TWA File: {test1}")

	# CSV FORMAT: row[0] = state number, row[1] = action taken, row [2] = char input and transitions
	for row in csv_reader:
		sid = int(row[0])
		move = row[1]
		if sid not in states:
			states[sid] = State(sid, move)
		for index in range(2, len(row)):
			transition = row[index]
			if transition != '':
				transition = transition.split(',')
				states[sid].addTransition(transition)
		line_count += 1
	print(f'Finished loading {line_count} number of states.')

#Main Program
# eval = "aabb"
eval = input("Enter String: ") 

eval = insert_hashtag(eval, 0)
eval = insert_hashtag(eval, len(eval))

print(f"Evaluating String: {eval}")

sm = StateMachine(states)
sm.eval(eval)
