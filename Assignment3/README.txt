NATURAL LANGUAGE PROCESSING - CS6320.001
========================================

README
------

Method of execution : 
---------------------
python viterbi.py <sequence>

Example : 	python viterbi.py "3 3 1 1 2 2 3 1 3"  

	or		python viterbi.py "S1"  (if Sequence 1 needs to be displayed)
			
	or		python viterbi.py "S2"  (if Sequence 2 needs to be displayed)

	or		python viterbi.py "3 1 2 3 1 2 1 3 2 1 2 3 2 1 2 3 2"  (for a random sequence)
			
(Note : The arguments need to be enclosed within "" and each of the numbers in the sequence need to be separated by a space(if random sequence is given))


OUTPUT:
-------


python viterbi.py "S1"

Sequence1  ['3', '3', '1', '1', '2', '2', '3', '1', '3']
HOT HOT COLD COLD HOT HOT HOT HOT HOT

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
python viterbi.py "S2" 

Sequence2  ['3', '3', '1', '1', '2', '3', '3', '1', '2']
HOT HOT COLD COLD HOT HOT HOT HOT HOT

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
python viterbi.py "3 1 2 3 1 2 1 3 2 1 2 3 2 1 2 3 2"

User Input Sequence  ['3', '1', '2', '3', '1', '2', '1', '3', '2', '1', '2', '3', '2', '1', '2', '3', '2']
HOT HOT HOT HOT COLD COLD COLD HOT HOT HOT HOT HOT HOT HOT HOT HOT HOT
