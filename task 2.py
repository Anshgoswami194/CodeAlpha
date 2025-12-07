def bot_reply(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Heyyy! What's poppin'?"

    elif "how are you" in msg:
        return "Running smooth and lag-free. What about you?"

    elif "joke" in msg:
        return "Why don't programmers play hide and seek? Because good luck hiding when your code has logs everywhere 😂"

    elif "compliment" in msg:
        return "Bro, you're not just smart… you're *RAM-level fast* smart"

    elif "motivate" in msg or "motivation" in msg:
        return "You got this! One day your success will be so big even Google will search you"

    elif "roast me" in msg:
        return "Bro, even error 404 has more direction than your life right now"

    elif "fact" in msg:
        return "Fun fact: Computers were once the size of rooms. Now your phone is more powerful than NASA's 1969 computers!"

    elif "game" in msg:
        return "Mini game coming soon: Type 'guess' to play a guessing game!"

    elif "guess" in msg:
        return "I'm thinking of a number between 1 and 5… but I won’t tell you  (Just kidding, it's 3!)"

    elif "your name" in msg:
        return "I'm ChatBro. Built for chaos, jokes, and fun."

    elif "age" in msg:
        return "My age? Same as your WiFi ping… always changing "

    elif "food" in msg:
        return "I love junk food… like corrupted files and spicy RAM chips "

    elif "sad" in msg:
        return "Don't worry bro, even the longest night ends with sunrise. I'm with you"

    elif "happy" in msg:
        return "Ayyee let's go!! Keep the vibe up"

    elif "option" in msg or "help" in msg or "commands" in msg:
        return (
            "Here are the commands I understand:\n"
            "- hello / hi\n"
            "- how are you\n"
            "- joke\n"
            "- compliment\n"
            "- motivate\n"
            "- roast me\n"
            "- fact\n"
            "- game / guess\n"
            "- your name\n"
            "- age\n"
            "- food\n"
            "- sad / happy\n"
            "- bye"
        )
        
    elif "bye" in msg:
        return "Bye bro! Stay awesome "

    else:
        return "Huh? I didn’t get that. Type 'option' to see all commands."

print("=== Fun ChatBot ===")
print("Type 'option' to see everything I can do!")
print("Type 'bye' to exit.\n")

while True:
    user_msg = input("You: ")
    reply = bot_reply(user_msg)
    print("Bot:", reply)

    if "bye" in user_msg.lower():
        break
