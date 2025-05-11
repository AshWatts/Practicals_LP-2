import nltk
import random
from nltk.tokenize import word_tokenize

# Download NLTK data (first-time setup)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading NLTK data...")
    nltk.download('punkt')

# Chatbot knowledge
RESPONSES = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye! Take care."],
    "question": ["I'm not sure.", "That's an interesting question.", "What do you think?"],
    "statement": ["I see.", "Tell me more.", "Interesting. Go on."],
    "feeling": [
        "Why do you feel {}?",
        "I understand feeling {}. Can you tell me more?",
        "How long have you felt {}?"
    ]
}

KEYWORDS = {
    "greeting": ["hi", "hello", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you", "quit"],
    "feeling": ["happy", "sad", "angry", "excited", "tired", "nervous"]
}

def chatbot_response(user_input):
    # Tokenize and lowercase the input
    tokens = word_tokenize(user_input.lower())
    
    # Check for greeting
    if any(word in tokens for word in KEYWORDS["greeting"]):
        return random.choice(RESPONSES["greeting"])
    
    # Check for goodbye
    if any(word in tokens for word in KEYWORDS["goodbye"]):
        return random.choice(RESPONSES["goodbye"])
    
    # Check for feelings
    for word in tokens:
        if word in KEYWORDS["feeling"]:
            return random.choice(RESPONSES["feeling"]).format(word)
    
    # Check for questions
    if "?" in user_input:
        return random.choice(RESPONSES["question"])
    
    # Default response
    return random.choice(RESPONSES["statement"])

# Main chat loop
print("Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.")
print("Chatbot: You can tell me how you're feeling or ask me questions.")

while True:
    user_input = input("You: ")
    if user_input.lower() in KEYWORDS["goodbye"]:
        print("Chatbot:", random.choice(RESPONSES["goodbye"]))
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)