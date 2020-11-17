import pandas as pd     
import numpy as np
import psutil
from googletrans import Translator
import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sys

# maximumMemory = sys.maxsize * 0.8
# print(maximumMemory)

translator = Translator()

# x = pd.read_csv('tweet_dataset.csv',error_bad_lines=False).text
# y = pd.read_csv('covid19_tweets.csv',error_bad_lines=False).text 
# z = pd.read_csv('bigtweetdata.csv',error_bad_lines=False,encoding = "ISO-8859-1").iloc[:,-1:]


# for i in range(1,10):
#     i = i * 0.1
#     if maximumMemory > (len(x[0:int(len(x)*(1-i))]) + len(y[0:int(len(x)*(1-i))])+ len(z[0:int(len(x)*(1-i))])):
#         text = x[0:int(len(x)*(1-i))] 
#         if (psutil.cpu_percent() > 0.9):
#             break
#         text += y[0:int(len(x)*(1-i))]
#         if (psutil.cpu_percent() > 0.9):
#             break
#         for j in range(10000):
#             if (psutil.cpu_percent() > 0.9):
#                 break
#             binSize = int(len(z) / 10000)
#             text += z[(binSize*j):(binSize*j+1)]


# #<Chatbot Trainer>
# text = [str(i) for i in text]

chatbot = ChatBot("excalibur")
# conversation = text

# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

# </Chatbot Trainer>


# # <TEST>



# inputTExt = input("Enter your input: ")
# inputTExt = str(inputTExt)
# print(translator.detect(inputTExt).lang)
# translatedText = translator.translate(inputTExt).text
# response = chatbot.get_response(translatedText)  
# response_data = response.serialize()
# print(response_data['text'])

# # </TEST>




# <STREAMLIT PART>

st.title("Tweet Mention System. Create Mentions with This Tool")
st.header("Write Here the Tweet")
text_result = st.text_area("You can enter you tweet or text here",height=150)


if text_result:
    for i in range(5):
        try:
            if translator.detect(text_result).lang == "en":
                text = text_result
                break
            else:
                text = translator.translate(text_result).text
            break
        except:
            continue

        
    st.write("English version of the enterance",text)
    response = chatbot.get_response(text) 
    response_data = response.serialize()
    st.write("Reponse: ",response_data['text'])

# </STREAMLIT PART>
            