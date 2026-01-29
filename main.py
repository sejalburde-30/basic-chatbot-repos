def basic_chatbot():
    print("Chatbot: Hi! Type 'bye' to end the chat.")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Chatbot: Hi!")

        elif message == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif message == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: I don't understand.")

# Start the chatbot
basic_chatbot()
