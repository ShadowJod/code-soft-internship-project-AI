def chatbot():
    print("Hello! I'm chatbot created by Nikhil. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if 'hi' in user_input or 'hello' in user_input:
            print("Chatbot: Hello! How are you?")
        
        elif 'how are you' in user_input or 'kaise ho' in user_input:
            print("Chatbot: I'm Doing Great what about You?")
        
        elif 'fine' in user_input or 'good' in user_input:
            print("Chatbot:That hilarious. How can I Help you?")
        
        elif 'help' in user_input:
            print("Chatbot: What do you need Help with?")
        
        elif 'name' in user_input:
            print("Chatbot: I don't have a name , but you can call me what you want to wish , My code name is chatBotAi")
        
        elif 'bye' in user_input or 'exit' in user_input or 'quit' in user_input:
            print("Chatbot: sayonara! Have a Good day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please retype ?")

chatbot()
