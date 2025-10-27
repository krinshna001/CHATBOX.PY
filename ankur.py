# simple chatbot program
print("chatbot:Can i help you?")
# Step 2: Keep chatting until user says bye
while True:
    # Ask user for input
    user_text = input("You: ")
    if user_text == "hello":
        print("Chatbot: Hi there!")
    elif user_text=="hi":
        print("chatbot: hello")    
    elif user_text == "how are you":
        print("Chatbot: I'm good, thank you!")
    elif user_text =="what is your name":
        print("chatbot: My name is Chatbot."
              "whats your name?:")

    elif user_text =="what can you do?":
        print("chatbot: I can chat with you and answer simple questions.")
    elif user_text=="you can do anything":
        print("chatbot: No I can't do anything")
    elif user_text=="who created you":
        print("chatbot: I was created by Ankur")
    elif user_text=="you are so helpful":
        print("chatbot: thank you")
        # ...existing code...

    elif user_text.startswith("my name is "):
        user_name = user_text[11:]  
         # Extract name after "my name is "
        print(f"Chatbot: Nice to meet you,{user_name}!")
    elif user_text == "bye":
        print("Chatbot: Goodbye!")
    
    else:
        print("Chatbot: I don't understand that yet.")
        # ...existing code...