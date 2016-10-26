NATURAL LANGUAGE PROCESSING - CS6320.001
========================================

README
------

Method of execution : 
---------------------
python corpus_bigram.py <corpus_filename> <random_input_sentence>

Example : python corpus_bigram.py "NLPCorpusTreebank2Parts.txt" "The size of the company's board has been reduced to eight directors from 13."


(Note : The arguments need to be enclosed within "")


Random User Input: "The size of the company's board has been reduced to eight directors from 13."

Total probability (without smoothing) - 0.0
Total probability (with add-one smoothing) - 2.073710879068967e-39
Total probability (with Good-Turing discounting) - 7.515386035462189e-40

Sentence 1: "The president has relinquished his control of the company's board."

Total probability (without smoothing) - 0.0
Total probability (with add-one smoothing) - 9.548360132141142e-28
Total probability (with Good-Turing discounting) - 1.4823851457612548e-18

Sentence 2: "The chief executive officer said the last year revenue was good."

Total probability (without smoothing) - 0.0
Total probability (with add-one smoothing) - 3.962241905219507e-28
Total probability (with Good-Turing discounting) - 3.807029981114749e-20

From the above probabilities(between Sentence 1 and Sentence 2), we can see that Sentence 1 is more probable than Sentence 2(because of higher probability values)

NOTE : corpus_bigram_Output.txt has the output contents 
		corpus.txt has the corpus bigram counts
