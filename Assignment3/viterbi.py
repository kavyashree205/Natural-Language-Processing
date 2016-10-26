import sys

class Viterbi:
	def __init__(self, sequence, start_state_prob, transition_prob, emission_prob):
		#since number of states are fixed in this case(HOT and COLD), create a 2D array of size (2+2, length of observation sequence)
		self.prob_matrix=[[0.0 for x in range(len(sequence))] for y in range(4)]
		self.backpointer=[[-1 for x in range(len(sequence))] for y in range(4)]
		
		#Initialization step
		#3 is the number of states(HOT, COLD)+1
		for i in range(1,3):
			#i=1 represents HOT, i=2 represents COLD
			
			self.prob_matrix[i][0]=(start_state_prob[i-1]*emission_prob[i-1][int(sequence[0])-1])
			self.backpointer[i][0]=0
		
			
	def recursion_step(self,sequence, start_state_prob, transition_prob, emission_prob):
		for t in range(1, len(sequence)):
			for s in range(1, 3):
				#get the maximum among the N state values				
				val=[(self.prob_matrix[s1][t-1]*transition_prob[s1-1][s-1]*emission_prob[s-1][int(sequence[t])-1]) for s1 in range(1, 3)]
				argmax=[(self.prob_matrix[s1][t-1]*transition_prob[s1-1][s-1]) for s1 in range(1, 3)]
				self.prob_matrix[s][t]=max(val)
				#backpointer stores the index of the previous state that has highest prob value
				self.backpointer[s][t]=argmax.index(max(argmax))+1
				
		
		#Termination step
		vals=[(self.prob_matrix[s1][t]) for s1 in range(1, 3)]
		self.prob_matrix[3][t]=max(vals)
		last_state=vals.index(max(vals))+1
			
		#backtracing
		result_seq=[]
		result_seq.append(last_state)		
		back_track=last_state
		T=len(sequence)-1
		while(T!=-1):			
			#store the backtraced states in result_seq list
			result_seq.append(self.backpointer[back_track][T])
			back_track=self.backpointer[back_track][T]
			T-=1
		#printing the result sequence in reverse order to get the correct output sequence
		for st in reversed(result_seq):
			if(st==1):
				print("HOT", end=' ')
			elif(st==2):
				print("COLD",end=' ')
			else:
				continue
				

def main():
	if(len(sys.argv)==2):
		#hard-coding of HMM values from Figure 6.3
		start_state_prob=[0.8, 0.2]#0-HOT, 1-COLD
		
		'''transition_prob
			HOT	COLD
		HOT[[0.7 0.3],
		COLD[0.4 0.6]]
		'''
		transition_prob=[[0.7, 0.3],[0.4, 0.6]]
		'''emission_prob
					1 	2 	3
		HOT		[[0.2 0.4 0.4],
		COLD	[0.5 0.4 0.1]]
		'''
		emission_prob=[[0.2,0.4,0.4],[0.5,0.4,0.1]]
		user_sequence=sys.argv[1]
		if(user_sequence=="S1" or user_sequence=="s1"):
			sequence1=['3','3','1','1','2','2','3','1','3']
			seq1=Viterbi(sequence1, start_state_prob, transition_prob, emission_prob)
			print("Sequence1 ",sequence1)
			seq1.recursion_step(sequence1, start_state_prob, transition_prob, emission_prob)
			print("\n\n")
		elif(user_sequence=="S2" or user_sequence=="s2"):
			sequence2=['3','3','1','1','2','3','3','1','2']
			seq2=Viterbi(sequence2, start_state_prob, transition_prob, emission_prob)
			print("Sequence2 ",sequence2)
			seq2.recursion_step(sequence2, start_state_prob, transition_prob, emission_prob)
			print("\n\n")
		else:
			user_sequence=user_sequence.split(" ")
			if(len(user_sequence)<=1):
				print("Invalid Input.Sequence should have numbers which are permutations of 1,2,3")
				exit(0)
			#print(user_sequence)
			for w in user_sequence:
				if(w.isalpha() or int(w)>=4 or int(w)<=0 ):
				#print(w)
					print("Invalid input.Sequence should have numbers which are permutations of 1,2,3")
					exit(0)
			user_seq=Viterbi(user_sequence, start_state_prob, transition_prob, emission_prob)
			print("User Input Sequence ", user_sequence)
			user_seq.recursion_step(user_sequence, start_state_prob, transition_prob, emission_prob)
		
		
		
	else:
		print("Invalid number of arguments")
		print("Command Usage: python viterbi.py <sequence>")
		exit(0)


if __name__ == '__main__':
	main()