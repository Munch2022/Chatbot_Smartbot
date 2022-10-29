# Chatbot_Personal
This repo consists all related files to build an interactive GUI application chatbot which can answer questions about me

### Simple chatbot implementation with Python using tkinter for gui app.

•	Created the chatbot from the scratch with python 

•	NLP techniques are used to clean and process the data 

•	Used a simple Dense neural net with 2 layers along with dropout

•	One can customize own use case with just modifying the intents.json file with possible patterns and responses and re-run the training

😎 I have trained this bot with my own details/basic information and the bot itself; named him SmartBot. So anybody can know about me chatting with my bot
Eg: greetings(hi, hello, whats up), who are you, what is your name, why do you call yourself smart?, who is Manjula, what are her skills, when is her birthday, what are her hobbies, what is her marital status?/ is she married, what is her past experience, who created you?, etc.. 

![resized_bot1](https://user-images.githubusercontent.com/111883941/198621847-302bd5ca-f102-4cc1-9f83-ac09943150c7.png)
### Description of files: 

•	intents.json file consists of intents with patters, responses and tag

•	training.py contains the code for training(Dense neural net used) along with words and classes sorted from the intents file

•	Sorted words and classes are dumped to pickle files for further use during chatbot creation and the trained model is saved to h5 file

•	chatbot.py file contains the creation of chatbot. All the functions for cleaning the text, bag of words, prediction, get response are used in the same file

•	GUI is built using tkinter in app.py file along with some style and looks of the chatbox 

•	Once the data is trained, the result will be automaticalled stored in db.sqlite

•	app.py makes call to chatbot.py to reply back to user with relavant answers

### Output of how the bot works: 
![image](https://user-images.githubusercontent.com/111883941/198577838-9c23e14d-99ee-48e7-abc6-519cbfc154bd.png)

