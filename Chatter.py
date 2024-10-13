import streamlit as st

# Define a simple function to generate a response (you can replace this with a more advanced model)
def get_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you?"
    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

# Create the Streamlit app
st.title("Simple Chatbot")
st.write("Type your message below to chat with the bot:")

# Input from the user
user_input = st.text_input("You: ")

# If the user inputs something, generate a response
if user_input:
    response = get_response(user_input)
    st.write("Bot: " + response)
