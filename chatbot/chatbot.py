replies = {
    "hello": "Hey! How's it going?",
    "hi": "Hi there!",
    "how are you": "I'm good, thanks for asking!",
    "what is your name": "You can call me Chatty.",
    "thanks": "No problem!",
    "thank you": "No problem!",
    "what can you do": "Right now I can just chat about basic stuff.",
    "help": "Try saying hi, or ask me how I'm doing!",
}

exit_words = ["bye", "exit", "quit"]


def get_reply(text):
    if text in replies:
        return replies[text]

    if "name" in text:
        return "You can call me Chatty."
    if "how" in text and "you" in text:
        return "I'm doing great, thanks!"

    return "Sorry, I didn't get that. Try again?"


def run_chat():
    print("Chatty: Hi! Type 'bye' whenever you want to stop.\n")

    while True:
        user_input = input("You: ")
        text = user_input.lower().strip()

        if text in exit_words:
            print("Chatty: Bye, take care!")
            break

        reply = get_reply(text)
        print("Chatty:", reply)


run_chat()