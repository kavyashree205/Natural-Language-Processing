from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import re
import sys

def simplified_lesk(sentence, word):
	
	best_sense=None
	#stop_words=['a','an','and','are','as','at','be','by','for','from','has','he','in','is','it','its','of','on','that','the','to','was','were','will','with','if','but','not','or','there']
	max_overlap=0
	modified_sentence=list(set(sentence)-set(stopwords.words("english")))#modified_sentence is the input context(input sentence) with all stopwords removed
	
	
	try:
		senses=wn.synsets(word, pos=wn.NOUN)#to get all the noun senses of the ambiguous word
		
		for snset in senses:#for each of the definitions of the ambiguous word available from wordnet, 
			
			defn=snset.definition()#store the definition 
			#print("def",defn)
			defn=defn.lower()#convert it into lower case(if there are any upper case letters)
			
			example=snset.examples()#consider the examples
			#print("EXamples", example)
			for ex in example:#concatenate the definition with all the examples pertaining to that sense
				ex=ex.lower()#loop throught the list of examples and convert each example into lower case sentence
				defn=defn+" "+ex
				
			defn=re.sub('[^A-Za-z\']+',' ',defn)#to remove all special characters and replace them with ' '
			
			signature=defn.split()#the list containing gloss and examples of sense
			
			signature=list(set(signature)-set(stopwords.words("english")))#remove all stopwords 
			
			overlap=len(list(set(modified_sentence).intersection(set(signature))))#find the number of common words(intersection/overlap) between the input context and the signature
			
			if overlap>max_overlap:#finding the maximum overlap count
				max_overlap=overlap
				best_sense=str(snset)+" Definition: "+snset.definition()
		
		print("Maximum Overlap: ", max_overlap)
		print("Best Sense: ", best_sense)
	except LookupError as le:
		print(le)
	

def main():
	if(len(sys.argv)==3):
		#input_sentence=input("Enter the input sentence\n")
		input_sentence=sys.argv[1]
		ambiguous_word=sys.argv[2]
		
		input_sentence=re.sub('[^A-Za-z\']+',' ',input_sentence)#remove all special characters and replace them with ' '
		input_sentence=input_sentence.replace(ambiguous_word,'')#removing the ambiguous word from the input context since there is no need to consider it
		input_sentence=input_sentence.lower()		
		input_sentence=input_sentence.strip().split()
		
		#ambiguous_word=input("Enter an ambiguous word from the input sentence\n")		
		ambiguous_word=re.sub('[^A-Za-z]+','',ambiguous_word)
		
		simplified_lesk(input_sentence, ambiguous_word.lower())
		
	else:
		print("Invalid number of arguments\n")
		print("Command Usage: python lesk_algorithm.py <input-sentence> <ambiguous-word-from-the-input-sentence>")
		print("Example : python lesk_algorithm.py \"I sat by the river bank staring at the moon.\" \"bank\"")
		exit(0)



if __name__ == '__main__':
	main()