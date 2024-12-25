import random
import re
from nltk.chat.util import Chat, reflections

def chatbot():
    pairs = [
        [
            r"hi|hello|hey", 
            ["Hello! How can I assist you today?", "Hi there! What's on your mind?", "Hey! How can I help?"]
        ],
        [
            r"how are you(.*)?", 
            ["I'm just a bot, but I'm doing great! How about you?", "I'm here to help. How are you doing?"]
        ],
        [
            r"(.*) your name(.*)?", 
            ["I am ChatBot, your friendly assistant.", "You can call me ChatBot. What's your name?"]
        ],
        [
            r"(.*) help (.*)", 
            ["I'm here to help! What do you need assistance with?", "Sure, let me know how I can help you."]
        ],
        [
            r"(.*) weather(.*)", 
            ["I'm not equipped to provide weather updates, but you can check online!", "Weather information is just a quick search away."]
        ],
        [
            r"(.*) created you(.*)?", 
            ["I was created by a programmer to assist you.", "A developer built me to make your life easier!"]
        ],
        [
            r"what is your purpose(.*)?", 
            ["My purpose is to assist and provide information whenever you need it.", "I'm here to make your life easier by answering questions and having conversations."]
        ],
        [
            r"(.*) favorite color(.*)?", 
            ["I like all colors equally! What's your favorite color?", "Colors are fascinating. Do you have a favorite?"]
        ],
        [
            r"(.*) time(.*)?", 
            ["I don't have a clock, but you can check the current time on your device!", "Time is a concept I can't perceive, but your clock knows!"]
        ],
        [
            r"(.*) hobby(.*)?", 
            ["I enjoy chatting with people like you!", "My hobby is assisting users. What's yours?"]
        ],
        [
            r"(.*) know programming(.*)?", 
            ["Yes, I know quite a bit about programming. Do you have any questions about it?", "Programming is one of my specialties! Feel free to ask."]
        ],
        [
            r"tell me a joke", 
            ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
        ],
        [
            r"quit|bye|exit", 
            ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Come back soon!"]
        ],
        [
            r"(.*)", 
            ["Interesting! Tell me more.", "Why do you say that?", "Can you elaborate?", "I see. Please continue."]
        ]
    ]
    chat = Chat(pairs, reflections)

    print("Hello! I'm your chatbot. Type 'quit' to end the conversation.")
    chat.converse()
if __name__ == "__main__":
    chatbot()
