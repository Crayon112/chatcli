def run(bot):
    while True:
        message = input(">>> ")
        if message == "quit":
            break
        response =  bot.send(message)
        print("Bot: ", response)