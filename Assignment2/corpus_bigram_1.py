class Bigram_Table:
	def __init__(self, input_sentence):
		bigram_counts=[['0' for x in range(len(input_sentence)+1)] for y in range(len(input_sentence)+1)]
		bigram_probabilities=[[0.0 for x in range(len(input_sentence)+1)] for y in range(len(input_sentence)+1)]

	

def remove_duplicates(l):
	without_dup=set()
	out=[]
	for word in l:
		if word not in without_dup:
			without_dup.add(word)
			out.append(word)
			
	
	return out



def main():
	#input="The president has relinquished his control of the company's board. The president company's board."
	input=open("NLPCorpusTreebank2Parts.txt","r")
	
	input_text=input.read()
	input_text=input_text.lower().strip()
	input_text=input_text.replace("\n"," ")
	#print(input_text)
	input_list=input_text.split(" ")
	#print(input_list)
	bigrams_dic={}
	for x in range(len(input_list)-1):
		bigram_pair=[]
		bigram_pair.append(input_list[x].strip())
		bigram_pair.append(input_list[x+1].strip())
		#print(str(bigram_pair))
		key=str(bigram_pair)
		#print(key)
		#bigram_set=set(bigram_pair)
		if(key not in bigrams_dic):
			bigrams_dic[key]=1
		else:
			bigrams_dic[key]=bigrams_dic.get(key,0)+1
	
	#print(bigrams_dic)
	input.close()
	output=open("corpus.txt","w")
	output.write(str(bigrams_dic))
	output.close()
	
	#bigram counts
	any_input="The president has relinquished his control of the company's board."
	any_input=any_input.lower().strip()
	any_input=any_input.replace("\n"," ")
	any_input_list=any_input.split(" ")
	#remove duplicates
	any_input_list=remove_duplicates(any_input_list)
	
	#table of bigram counts;initialization
	table=[['0' for x in range(len(any_input_list)+1)] for y in range(len(any_input_list)+1)]
	#add header row and column
	for i in range(1, len(any_input_list)+1):
		table[0][i]=any_input_list[i-1]
	
	#print(type(table[0]))
	print('\t'.join(table[0]))
	#calculate bigram counts
	for j in range(1, len(any_input_list)+1):
		table[j][0]=any_input_list[j-1]
		for k in range(1, len(any_input_list)+1):
			
			#header_row=[]
			##header_row.append(any_input_list[j])
			#table values
			pair=[]
			pair.append(table[j][0])
			pair.append(table[0][k])
			pair=str(pair)
			if(pair in bigrams_dic):
				table[j][k]=str(bigrams_dic.get(pair))
			else:
				table[j][k]='0'
		
		print('\t'.join(table[j]))
			
	#find individual word counts
	'''
	bigram probabilty
	P(word2|word1)=C(word1 word2)/C(word1)
	'''

	
if __name__ == '__main__':
	main()
	

	

	
	
'''
def main():
	corpus_file=open("NLPCorpusTreebank2Parts.txt","r")
	lines=[]
	for x in range(1,10):
		#lines.append(line)
		print(corpus_file.read())
	
	print(lines)

if __name__ == '__main__':
	main()
'''