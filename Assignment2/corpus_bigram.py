import sys
'''
Example variable values
bigram_counts =  [['','i','am','sam'],['i','9','0','1'],['am','5','7','8'],['sam','0','0','0']]
bigram_probabilities = [['','i','am','sam'],['i','0.9','0.8','0.6'],['am','0.5','0.7','0.8'],['sam','0.6','0.77','0.33']]
'''
class Bigram_Table:
	def __init__(self, input_sentence):
		#scenario a: without smoothing
		self.bigram_counts=[['0' for x in range(len(input_sentence)+1)] for y in range(len(input_sentence)+1)]
		self.bigram_probabilities=[['0.0' for x in range(len(input_sentence)+1)] for y in range(len(input_sentence)+1)]
		
		#scenario b: with add-one smoothing
		self.bigram_counts1=[['0' for x in range(len(input_sentence)+1)] for y in range(len(input_sentence)+1)]
		self.bigram_probabilities1=[['0.0' for x in range(len(input_sentence)+1)] for y in range(len(input_sentence)+1)]
		
	def calc_bigram_counts(self,any_input_list,bigrams_dic,corpus_list):
		#add header row 
		for i in range(1, len(any_input_list)+1):
			self.bigram_counts[0][i]=any_input_list[i-1]
			self.bigram_probabilities[0][i]=any_input_list[i-1]
	
		print("----------BIGRAM COUNTS - WITHOUT SMOOTHING-----------\n")
		
		
		#calculate bigram counts
		for j in range(1, len(any_input_list)+1):
			#header column
			self.bigram_counts[j][0]=any_input_list[j-1]
			self.bigram_probabilities[j][0]=any_input_list[j-1]
			for k in range(1, len(any_input_list)+1):
				
				#table values
				pair=[]
				pair.append(self.bigram_counts[j][0])#word1
				pair.append(self.bigram_counts[0][k])#word2
				pair=str(pair)
				#check if the bigram is present in the corpus bigram dictionary;take the corresponding frequency count if present
				if(pair in bigrams_dic):
					self.bigram_counts[j][k]=str(bigrams_dic.get(pair))
					#bigram probabilty
					#P(word2|word1)=C(word1 word2)/C(word1)
					self.bigram_probabilities[j][k]=str(round((bigrams_dic.get(pair)/corpus_list.count(self.bigram_counts[j][0])),6))
				else:#assign 0 if not present
					self.bigram_counts[j][k]='0'
					self.bigram_probabilities[j][k]='0.0'
			
			
			
		self.display_table(self.bigram_counts)
		
		print('\n\n')
		print("----------BIGRAM PROBABILITY WITHOUT SMOOTHING-----------\n")
		
		self.display_table(self.bigram_probabilities)
		print('\n\n')
			
	def cal_addone_smoothing(self,any_input_list,bigrams_dic,corpus_list,V):
		for i in range(1, len(any_input_list)+1):
			self.bigram_counts1[0][i]=any_input_list[i-1]
			self.bigram_probabilities1[0][i]=any_input_list[i-1]
		
		print("----------BIGRAM COUNTS - ADD ONE SMOOTHING-----------\n")
		
		for j in range(1, len(any_input_list)+1):
			self.bigram_counts1[j][0]=any_input_list[j-1]
			self.bigram_probabilities1[j][0]=any_input_list[j-1]
			for k in range(1, len(any_input_list)+1):
				
				#table values
				pair=[]
				pair.append(self.bigram_counts1[j][0])#word1
				pair.append(self.bigram_counts1[0][k])#word2
				pair=str(pair)
				if(pair in bigrams_dic):
					self.bigram_counts1[j][k]=str(bigrams_dic.get(pair)+1)
					#bigram probabilty
					#P(word2|word1)=(C(word1 word2)+1)/(C(word1)+V)
					self.bigram_probabilities1[j][k]=str(round(((bigrams_dic.get(pair)+1)/(corpus_list.count(self.bigram_counts1[j][0])+V)),6))
				else:#if the pair doesn't exist in the corpus
					self.bigram_counts1[j][k]='1'
					self.bigram_probabilities1[j][k]=str(round((1/(corpus_list.count(self.bigram_counts1[j][0])+V)),6))
			
			#print('\t'.join(self.bigram_counts1[j]))
			#print('\t'.join(self.bigram_probabilities1[j]))
		self.display_table(self.bigram_counts1)
		print('\n\n')
		print("----------BIGRAM PROBABILITY WITH ADD ONE SMOOTHING-----------\n")
		self.display_table(self.bigram_probabilities1)
		
		print('\n\n')
		
	def cal_good_turing_discount(self, any_input_list, bigrams_dic, corpus_list, V):
		
		totalFrequency=0
		FreqOfFreq={}

		#re-using the same instance variables
		#get the total frequency count of all corpus bigrams;
		#FreqOfFreq is the dictionary with key-frequency value-number of bigrams that have this frequency
		for value in bigrams_dic.values():
			totalFrequency+=value
			if value not in FreqOfFreq:
				FreqOfFreq[value]=1
			else:
				FreqOfFreq[value]=FreqOfFreq.get(value,0)+1
		
		print("----------BIGRAM COUNTS - GOOD TURING DISCOUNTING-----------\n")
		
		for j in range(1, len(any_input_list)+1):
			
			for k in range(1, len(any_input_list)+1):
				c=int(self.bigram_counts[j][k])
				#if bigrams have zero count
				if(c==0):
					self.bigram_probabilities[j][k]=str(round((FreqOfFreq.get(1)/totalFrequency),6))
				elif(c>3):#assuming K=3
					self.bigram_probabilities[j][k]=str(round((c/totalFrequency),6))
				else:
					self.bigram_probabilities[j][k]=str(round(((c+1)*FreqOfFreq.get(c+1)/FreqOfFreq.get(c)/totalFrequency),6))
					
		#display the bigram count and bigram probability tables
		self.display_table(self.bigram_counts)
		print('\n\n')
		print("----------BIGRAM PROBABILITY WITH GOOD TURING DISCOUNTING-----------\n")
		self.display_table(self.bigram_probabilities)
		
		print('\n\n')
		
	def calc_total_probability(self, any_input_list, bigrams_dic, corpus_list, V):
		totalProb=1.0
		first_bigram=[]
		#totalprob=P(first-word|.)*P(second-word|first-word)*....so on
		first_bigram.append('.')
		first_bigram.append(any_input_list[0].lower())
		if(str(first_bigram) in bigrams_dic):
			totalProb*=float(bigrams_dic.get(str(first_bigram)))
		for i in range(0, len(any_input_list)-1):
			#gen=[l[k] for k in range(1,len(any_input_list)+1) if bigram_probabilities[k][0]==any_input_list[i]]
			I=i+1
			J=i+2
			totalProb*=float(self.bigram_probabilities[I][J])
		
		last_bigram=[]
		#P(.|last-word) needs to be calculated if it is present in the corpus
		last_bigram.append(any_input_list[len(any_input_list)-1])
		last_bigram.append('.')
		if(str(last_bigram) in bigrams_dic):
			totalProb*=float(bigrams_dic.get(str(last_bigram)))
		print("The total probability for the given sentence is : ", totalProb)
		print('\n')
		
		
	def calc_total_probability_addone_smoothing(self, any_input_list, bigrams_dic, corpus_list, V):
		totalProb=1.0
		first_bigram=[]
		#totalprob=P(first-word|.)*P(second-word|first-word)*....so on
		first_bigram.append('.')
		first_bigram.append(any_input_list[0].lower())
		if(str(first_bigram) in bigrams_dic):
			totalProb*=float(bigrams_dic.get(str(first_bigram)))
		#calculate joint probability using the probability values of every consecutive bigram pairs
		for i in range(0, len(any_input_list)-1):
			#gen=[l[k] for k in range(1,len(any_input_list)+1) if bigram_probabilities[k][0]==any_input_list[i]]
			I=i+1
			J=i+2
			totalProb*=float(self.bigram_probabilities1[I][J])
		
		last_bigram=[]
		last_bigram.append(any_input_list[len(any_input_list)-1])
		last_bigram.append('.')
		if(str(last_bigram) in bigrams_dic):
			totalProb*=float(bigrams_dic.get(str(last_bigram)))
		print("The total probability for the given sentence is : ", totalProb)
		print('\n')
		
	def display_table(self,bigramTable):
		bigramTable[0][0]=''
		s = [[str(e) for e in row] for row in bigramTable]
		lens = [max(map(len, col)) for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		print('\n'.join(table))
		
def remove_duplicates(l):
	without_dup=set()
	out=[]
	for word in l:
		if word not in without_dup:
			without_dup.add(word)
			out.append(word)	
	return out



def main():
	
	if(len(sys.argv)==3):
		try:
			input=open(sys.argv[1],"r")
			input_text=input.read()
			#all the text from the corpus file is converted to lower case and extra characters are stripped. \n is replaced by " "
  			input_text=input_text.lower().strip()
			input_text=input_text.replace("\n"," ")
			#split the entire string into a list based on " "
			input_list=input_text.split(" ")
			
			#generate bigram counts for the corpus file
			bigrams_dic={}
			#get the frequency counts of all bigram pairs and store them in a dictionary
			#dictionary has key-[bigram pair](eg : ['of', 'the]) value-frequency
			for x in range(len(input_list)-1):
				bigram_pair=[]
				bigram_pair.append(input_list[x].strip())
				bigram_pair.append(input_list[x+1].strip())
				
				key=str(bigram_pair)
				
				if(key not in bigrams_dic):
					bigrams_dic[key]=1
				else:
					bigrams_dic[key]=bigrams_dic.get(key,0)+1
			
			
			input.close()
			#write the corpus bigram counts to an output file 
			output=open("corpus.txt","w")
			output.write(str(bigrams_dic))
			output.close()
			
			#to find V-take a count of all the distinct words from the corpus
			
			corpus_input_list=remove_duplicates(input_list)
			V=len(corpus_input_list)
			
			
			#Random input from user
			any_input=sys.argv[2]
			print("Input sentence from user : ",any_input)
			any_input=any_input.lower().strip()
			any_input=any_input.replace("\n"," ")
			any_input_list=any_input.split(" ")
			if(len(any_input_list)!=1):
				#remove duplicates
				any_input_list=remove_duplicates(any_input_list)
				
				#create instance of class Bigram_Table;initialization
				table = Bigram_Table(any_input_list)
				#Scenario a: calculate bigram counts; the method also includes calculating bigram probability without smoothing
				table.calc_bigram_counts(any_input_list,bigrams_dic,input_list)
				#calculate total probability 
				table.calc_total_probability(any_input_list,bigrams_dic,input_list,V)
				#Scenario b: calculate bigram counts and probability with add-one smoothing
				table.cal_addone_smoothing(any_input_list,bigrams_dic,input_list,V)
				#calculate total probability 
				table.calc_total_probability_addone_smoothing(any_input_list,bigrams_dic,input_list,V)
				#Scenario c: calculate bigram counts and probability with good turing discount
				table.cal_good_turing_discount(any_input_list,bigrams_dic,input_list,V)
				#calculate total probability 
				table.calc_total_probability(any_input_list,bigrams_dic,input_list,V)
			else:
				print("Length of the sentence is too less. Please input a sentence that has a minimum of two words\n")
				print("Command Usage: python corpus_bigram.py <corpus_filename> <input_sentence>")
				exit(0)
			
			#Sentence 1 : "The president has relinquished his control of the company's board."
			#bigram counts
			any_input1="The president has relinquished his control of the company's board."
			print("Input Sentence 1 : ", any_input1)
			any_input1=any_input1.lower().strip()
			any_input1=any_input1.replace("\n"," ")
			any_input_list1=any_input1.split(" ")
			#remove duplicates
			any_input_list1=remove_duplicates(any_input_list1)
			
			#create instance of class Bigram_Table;initialization
			table1 = Bigram_Table(any_input_list1)
			#Scenario a: calculate bigram counts; the method also includes calculating bigram probability without smoothing
			table1.calc_bigram_counts(any_input_list1,bigrams_dic,input_list)
			#calculate total probability 
			table1.calc_total_probability(any_input_list1,bigrams_dic,input_list,V)
			#Scenario b: calculate bigram counts and probability with add-one smoothing
			table1.cal_addone_smoothing(any_input_list1,bigrams_dic,input_list,V)
			#calculate total probability 
			table1.calc_total_probability_addone_smoothing(any_input_list1,bigrams_dic,input_list,V)
			#Scenario c: calculate bigram counts and probability with good turing discount
			table1.cal_good_turing_discount(any_input_list1,bigrams_dic,input_list,V)
			#calculate total probability 
			table1.calc_total_probability(any_input_list1,bigrams_dic,input_list,V)
			
			
			#Sentence 2 : "The chief executive officer said the last year revenue was good."
			#bigram counts
			any_input2="The chief executive officer said the last year revenue was good."
			print("Input Sentence 2 : ", any_input2)
			any_input2=any_input2.lower().strip()
			any_input2=any_input2.replace("\n"," ")
			any_input_list2=any_input2.split(" ")
			#remove duplicates
			any_input_list2=remove_duplicates(any_input_list2)
			
			#create instance of class Bigram_Table;initialization
			table2 = Bigram_Table(any_input_list2)
			#Scenario a: calculate bigram counts; the method also includes calculating bigram probability without smoothing
			table2.calc_bigram_counts(any_input_list2,bigrams_dic,input_list)
			#calculate total probability 
			table2.calc_total_probability(any_input_list2,bigrams_dic,input_list,V)
			#Scenario b: calculate bigram counts and probability with add-one smoothing
			table2.cal_addone_smoothing(any_input_list2,bigrams_dic,input_list,V)
			#calculate total probability 
			table2.calc_total_probability_addone_smoothing(any_input_list2,bigrams_dic,input_list,V)
			#Scenario c: calculate bigram counts and probability with good turing discount
			table2.cal_good_turing_discount(any_input_list2,bigrams_dic,input_list,V)
			#calculate total probability 
			table2.calc_total_probability(any_input_list2,bigrams_dic,input_list,V)
		except IOError:
			print("Seems like the file doesn't exist")
			exit(0)
		
	
	else:
		print("Invalid number of arguments\n")
		print("Command Usage: python corpus_bigram.py <corpus_filename> <input_sentence>")
		exit(0)
	

	
if __name__ == '__main__':
	main()
	
