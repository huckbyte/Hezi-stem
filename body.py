from tkinter import *
import datetime
import os
import random
import json
from time import strftime, time
from tkinter import filedialog
import pyttsx3
import torch
import pyjokes

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

bot_name = "<B♦o♣t>"
global msg

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def time():
    window = Tk()
    window.title("main window")
    window.geometry("120x60")
    
    time_label = Label(window,font=("Arial",50),fg="green",bg="black")
    time_label.pack()
    
    hour = int(datetime.datetime.now().hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    time_str = strftime("%I:%M:%S")
    time_label.config(text=time_str)
    
    return Time
    
 
class All_functions():
    def get_responces(msg):
        
    #json responces 
    
        sentence = tokenize(msg)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)
        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    
                    ans = random.choice(intent['responses'])
                    speak(ans)
                    #print(ans)
                    return  ans
                
                    # wrongResponce = (f"{bot_name}: I do not understand...")
                    # speak(wrongResponce)
                    # return wrongResponce
                
                    
        elif 'time' in msg:
                    
            bot  = (f" {time()}")
            speak(bot)
            return  bot
        
        elif "quit" or "close" in msg:
            pass
        
    

            
    
        wrongResponce = (f"{bot_name}: I do not understand...")
        # speak(wrongResponce)
        return wrongResponce
    
    
    def time():
        window = Tk()
        window.title("main window")
        window.geometry("120x60")
        
        time_label = Label(window,font=("Arial",50),fg="green",bg="black")
        time_label.pack()
        
        hour = int(datetime.datetime.now().hour)
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        Time = datetime.datetime.now().strftime("%I:%M:%S") 
        time_str = strftime("%I:%M:%S")
        time_label.config(text=time_str)
        
        return Time
