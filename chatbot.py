# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:08:15 2022

@author: Manjula
"""
# Creating Chatbot

# lets import all the libraries we need here 
import numpy as np
import pickle
import random
import json


import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model  


lemmatizer= WordNetLemmatizer()
intents= json.loads(open('intents.json'). read())   # we are reading the file from json file

# reading pickle files
words= pickle.load(open('words.pkl', 'rb'))
classes= pickle.load(open('classes.pkl', 'rb'))

# loading the model that we trained and saved 
model= load_model('chatbotmodel.h5')


# lets give name to our bot
bot_name= "Smart Bot"
#print("Hey! I'm smartBot. How are you doing?")

# now we are going to setup a bunch of 4 different functions to clean up, predict, bagofwords the sentences
# also the trained model will output in the numeric data but we need it in the text form
# the model is trained but we need to use it in right way 

# function for cleaning up the sentence
def clean_up_sentence(sentence):
    sentence_words= nltk.word_tokenize(sentence)
    sentence_words= [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


# function for bag of words. will convert a list of words in 0's and 1's 
def bag_of_words(sentence):
    sentence_words= clean_up_sentence(sentence)
    bag= [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]= 1
    return np.array(bag)


# function to predict. we will use both above functions for predict function
def predict_class(sentence):
    bow= bag_of_words(sentence)
    res= model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD= 0.25     # keeping teh threshold so that if probability is above threshold then we dont tak it
    results= [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    
    # will sort the result in reverse order so that we can get highest proba
    results.sort(key= lambda x: x[1], reverse= True)
    return_list= []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list 


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents= intents_json['intents']
    
    for i in list_of_intents:
        if i['tag'] == tag:
            result= random.choice(i['responses'])
            break
    return result

print("")


def get_reply(msg):
    ints= predict_class(msg)
    res= get_response(ints, intents)
    return res
       
       


 





