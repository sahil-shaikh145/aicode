while True:
    msg = input("You: ").lower()

    if "hello" in msg:
        print("Bot: Hi!")

    elif "name" in msg:
        print("Bot: My name is AI Bot")

    elif "how are you" in msg:
        print("Bot: I am fine")

    elif "bye" in msg:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand")