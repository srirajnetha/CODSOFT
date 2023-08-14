import re

# Define your rules and responses
rules = {
    r"(hi|hello|hey)":"Hello there!",
    r"what is your name":"I am a rule-based chatbot.",
    r"how are you":"I'm just a computer program, but I'm functioning well!",
    r"bye|goodbye":"Goodbye! Have a great day!",
    # Add more rules and responses here
}

# Function to process user input and provide responses
def get_response(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that."

# Main loop to simulate conversation
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)