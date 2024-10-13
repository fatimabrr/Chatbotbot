import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
streamlit
chatterbot
chatterbot_corpus

# Create a chatbot instance
chatbot = ChatBot("AdvancedBot")

# Create a trainer for the chatbot and train with the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Streamlit App UI
st.title("Advanced AI Chatbot")
st.write("Start chatting with the bot by typing your message below.")

# Get user input
user_input = st.text_input("You: ")

# If the user has entered something, generate a response
if user_input:
    bot_response = chatbot.get_response(user_input)
    st.write(f"Bot: {bot_response}")
