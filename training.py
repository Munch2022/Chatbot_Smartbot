import random
import json
import numpy as np
import pickle

import nltk 
from nltk.stem import WordNetLemmatizer


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer= WordNetLemmatizer()

intents= json.loads(open('intents.json'). read())

words= []
classes= []
documents= []
ignore_letters= ['?', '!', '.', ',']

# iterate over the intent
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list= nltk.word_tokenize(pattern)
        words.extend(word_list)                   # extend means taking the content and appending to list and append means taking list and appending to list
        documents.append((word_list, intent['tag'])) 
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


words= [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# to eliminate duplicates 
words= sorted(set(words))

# print(words)

# similarly we can eliminate duplicate from classes too

classes= sorted(set(classes))
# print(classes)

# now lets dump/save words and classes to pickle file as we need it later 
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# we will now get into ML part. but we need out data in numerical form as the learns only number form data
# neural network needs numerical values so we are going to use bag of words where individual words will have 
# value 0 or 1 depending on its occurence in that particular pattern and will do the same with classes
training= []
ouptput_empty= [0] * len(classes)

for document in documents:
    bag= []
    word_patterns= document[0]
    word_patterns=  [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    
    output_row= list(ouptput_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

# will do one last preprocessing. thats shuffle data 
random.shuffle(training)
training= np.array(training)

# lets get our training X, Y ; featires will be x value and labels will be y value
train_x= list(training[:, 0])
train_y= list(training[:, 1])  

# we can now start to build our neural network
model = Sequential()
model.add(Dense(128, input_shape= (len(train_x[0]),), activation= 'relu'))
model.add(Dropout(0.5))

model.add(Dense(64, activation= 'relu'))
model.add(Dropout(0.5))

model.add(Dense(len(train_y[0]), activation= 'softmax')) 

# Stochastic Gradient Descent(SGD) initialize
sgd= SGD(lr= 0.1, decay= 1e-6)               # I havent added these as getting low accuracy ->(momentum= 0.9, nesterov= True)

# compile the model
model.compile(loss='categorical_crossentropy', optimizer= sgd, metrics= ['accuracy'])


# lets fit/train the model

hist= model.fit(np.array(train_x), np.array(train_y), epochs= 25, batch_size= 5, verbose= 1)
model.save('chatbotmodel.h5', hist)
print("Done")


# neural network is trained and now we need to create a chatbot application 
# we will do that in a new file named chatbot.py




















   
            
 








