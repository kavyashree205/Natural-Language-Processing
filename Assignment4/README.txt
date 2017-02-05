README: ASSIGNMENT 5
--------------------

The LESK algorithm has been implemented in Python using nltk library(for accessing WordNet)

Commands used for downloading the corpus:

>>>import nltk
>>>nltk.download()

Source Code : lesk_algorithm.py

Method of execution:
--------------------

Command Usage: python lesk_algorithm.py <input-sentence> <ambiguous-word-from-the-input-sentence>

Example : python lesk_algorithm.py "We went to the bank to withdraw money." "bank"

(NOTE : The ambiguous word from the input sentence needs to be a noun. In the program, only the noun definitions of the ambiguous word have been used for comparison/overlapping
with the input context)

EXAMPLES:
---------

POSITIVE EXAMPLES:
   
1. K:\GDrive\MS-CS\3rdSem\NLP\HW5>python lesk_algorithm.py "Several men are fishing on the bank of the river" "bank"      
   Maximum Overlap:  1                                                                                                     
   Best Sense:  Synset('bank.n.01') Definition: sloping land (especially the slope beside a body of water)
   
2. K:\GDrive\MS-CS\3rdSem\NLP\HW5>python lesk_algorithm.py "Plants are one of the two groups into which all living things are divided" "Plants"  
   Maximum Overlap:  1                                                                                                     
   Best Sense:  Synset('plant.n.02') Definition: (botany) a living organism lacking the power of locomotion 
   
3. K:\GDrive\MS-CS\3rdSem\NLP\HW5>python lesk_algorithm.py "The actors in the play performed very well." "play"            
   Maximum Overlap:  1                                                                                                     
   Best Sense:  Synset('play.n.01') Definition: a dramatic work intended for performance by actors on a stage 
   
NEGATIVE EXAMPLES:

1. K:\GDrive\MS-CS\3rdSem\NLP\HW5>python lesk_algorithm.py "The purpose of the decision taken by the board was not known." "board"   
   Maximum Overlap:  1                                                                                                     
   Best Sense:  Synset('board.n.03') Definition: a flat piece of material designed for a special purpose

2. K:\GDrive\MS-CS\3rdSem\NLP\HW5>python lesk_algorithm.py "The play was canceled due to bad weather." "play"             
   Maximum Overlap:  0                                                                                                     
   Best Sense:  None
   

   
   


