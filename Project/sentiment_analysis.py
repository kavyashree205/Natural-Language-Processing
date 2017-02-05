#SENTIMENT ANALYSIS OF RESTAURANT REVIEWS

#Training_data : business_id	review_text	stars	sentiment
#Testing_data : business_id	review_text	stars	sentiment

import random
import csv
import pandas as pd

import numpy as np 
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer   
from sklearn.model_selection import train_test_split    
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report#for evaluating accuracy
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from nltk.stem.porter import PorterStemmer

test_data_file = 'test_data'
training_data_file = 'training_data'

test_data_df = pd.read_csv(test_data_file, header=None, delimiter="\t", quoting=3, usecols=[1,3])
test_data_df.columns = ["Review_Text","Sentiment"]

training_data_df = pd.read_csv(training_data_file, header=None, delimiter="\t", quoting=3, usecols=[1,3])
training_data_df.columns = ["Review_Text","Sentiment"]#only the sentiment(for cross-evaluation) and review_text are required

#(5472, 2)
print(training_data_df.shape)
#(32657, 1)
print(test_data_df.shape)

#Positive    5040
#Negative     432
#Name: Sentiment, dtype: int64
training_data_df.Sentiment.value_counts()

#find average number of words per sentence/review_text
np.mean([len(rev.split(" ")) for rev in training_data_df.Review_Text])#Output : 122.21655701754386 (i.e., 122 words per review on an average)

#creating a corpus - 
#1.Remove stopwords,remove punctuations,convert to lowercase etc. 
#2. Obtain tokens after performing stemming. The individual tokens and their counts are later calculated. 
#Bag of words model is being used here (same as n-grams where n=1)
stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    # remove non letters(punctuations,digits etc.)
    text = re.sub("[^a-zA-Z]+", " ", text)
    # tokenize
    tokens = nltk.word_tokenize(text)
    # stemming
    stems = stem_tokens(tokens, stemmer)
    return stems

#max_features = 200,500,1000
vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    stop_words = 'english',
    max_features = 200
)

vectorizer_for_testdata = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    stop_words = 'english',
	max_features = 200
)
#convert the original training dataset to a corpus
corpus_features = vectorizer.fit_transform(
    training_data_df.Review_Text.tolist())
#convert the original testing dataset to a corpus
corpus_features_testing = vectorizer_for_testdata.fit_transform(
    test_data_df.Review_Text.tolist())
	
#corpus_features_numpy contains features from the original training data
#has length 5472
corpus_features_numpy = corpus_features.toarray()
#corpus_feat_testnpy contains features from the original training data
corpus_feat_testnpy = corpus_features_testing.toarray()

#corpus_features_numpy contains all of our 
#original train and test data, so 
#the unlabeled test entries(from test_data_df) need to be excluded
X_train, X_test, y_train, y_test  = train_test_split(
        corpus_features_numpy[0:len(training_data_df)], 
        training_data_df.Sentiment,
        train_size=0.85, 
        random_state=1234)
		
		
#train the logistic regression classifier
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)

#predict the class value(sentiment tag) for the test data(X_test)
y_pred = log_model.predict(X_test)

#accuracy evaluation - compare the true sentiment tag with the 
#predicted tag (y_test: actual sentiment tag(true value), y_pred: predicted tag)
print("Classification report for Logistic Regression\n",classification_report(y_test, y_pred))
#accuracy
print("Logistic Regression Training accuracy\n",accuracy_score(y_test, y_pred))
#Confusion Matrix
print("Logistic Regression confusion matrix\n",confusion_matrix(y_test, y_pred))

#re-train the classifier on the original training data
log_model1 = LogisticRegression()
log_model1 = log_model1.fit(X=corpus_features_numpy[0:len(training_data_df)], y=training_data_df.Sentiment)

# get sentiment predictions for unlabeled test data(i.e., corpus_features_numpy[len(training_data_df):])

test_pred = log_model1.predict(corpus_feat_testnpy[0:len(test_data_df)])

#Testing Accuracy
print("Classification report for Logistic Regression\n",classification_report(test_data_df.Sentiment, test_pred))

print("Logistic Regression testing accuracy\n",accuracy_score(test_data_df.Sentiment, test_pred))
#Confusion Matrix
print("Logistic Regression confusion matrix\n",confusion_matrix(test_data_df.Sentiment, test_pred))


#WRITING PREDICTED SENTIMENTS AND TEST REVIEWS TO A CSV FILE

#convert predicted sentiments(in numpy array format) to data frame
test_pred2df=pd.DataFrame(test_pred)
test_pred2df.columns=["Sentiment"]#give a column name
#concat both the test reviews(which is already a data frame) and the predicted sentiments and get one single result data frame
result = pd.concat([test_pred2df, test_data_df], axis=1)
#write the result data frame to a csv file
result.to_csv('LogisticRegression_Output.csv',header=True,index=True, mode='w')
	
##SVM
clf = svm.LinearSVC()
clf.fit(X=X_train, y=y_train)
y_predicted=clf.predict(X_test)
print("Classification report for SVM\n",classification_report(y_test, y_predicted))

print("SVM Training Accuracy\n", accuracy_score(y_test, y_predicted))

print("SVM Confusion_matrix\n", confusion_matrix(y_test, y_predicted))

#re-train on the original training data
clf1 = svm.LinearSVC()

clf1.fit(X=corpus_features_numpy[0:len(training_data_df)], y=training_data_df.Sentiment)

y_predicted1 = clf1.predict(corpus_feat_testnpy[0:len(test_data_df)])

#Testing Accuracy
print("Classification report for SVM\n",classification_report(test_data_df.Sentiment, y_predicted1))

print("SVM testing accuracy\n",accuracy_score(test_data_df.Sentiment, y_predicted1))
#Confusion Matrix
print("SVM confusion matrix\n",confusion_matrix(test_data_df.Sentiment, y_predicted1))

#WRITING PREDICTED SENTIMENTS AND TEST REVIEWS TO CSV FILE

#convert predicted sentiments(in numpy array format) to data frame
y_pred_svm=pd.DataFrame(y_predicted1)
y_pred_svm.columns=["Sentiment"]#give a column name
#concat both the test reviews(which is already a data frame) and the predicted sentiments and get one single result data frame
result_svm = pd.concat([y_pred_svm, test_data_df], axis=1)
#write the result data frame to a csv file
result_svm.to_csv('SVM_Output.csv',header=True,index=True, mode='w')
	
#Naive Bayes classification
naive_bayes = MultinomialNB()
naive_bayes.fit(X=X_train, y=y_train)
y_predicted_nb=naive_bayes.predict(X_test)
print("Classification report for Naive Bayes\n", classification_report(y_test, y_predicted_nb))
print("Naive Bayes Accuracy\n", accuracy_score(y_test, y_predicted_nb))
print("Naive Bayes Confusion_matrix\n", confusion_matrix(y_test, y_predicted_nb))

#re-training the original training data
naive_bayes1 = MultinomialNB()

naive_bayes1.fit(X=corpus_features_numpy[0:len(training_data_df)], y=training_data_df.Sentiment)

y_predicted_nb1 = naive_bayes1.predict(corpus_feat_testnpy[0:len(test_data_df)])

#Testing Accuracy
print("Classification report for Naive Bayes\n",classification_report(test_data_df.Sentiment, y_predicted_nb1))

print("Naive Bayes testing accuracy\n",accuracy_score(test_data_df.Sentiment, y_predicted_nb1))
#Confusion Matrix
print("Naive Bayes confusion matrix\n",confusion_matrix(test_data_df.Sentiment, y_predicted_nb1))

#WRITING PREDICTED SENTIMENTS AND TEST REVIEWS TO CSV FILE

#convert predicted sentiments(in numpy array format) to data frame
y_pred_naiveb=pd.DataFrame(y_predicted_nb1)
y_pred_naiveb.columns=["Sentiment"]#give a column name
#concat both the test reviews(which is already a data frame) and the predicted sentiments and get one single result data frame
result_naiveb = pd.concat([y_pred_naiveb, test_data_df], axis=1)
#write the result data frame to a csv file
result_naiveb.to_csv('NaiveBayes_Output.csv',header=True,index=True, mode='w')
