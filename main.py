import aiml 

bot = aiml.Kernel()
bot.learn("q2.xml")

print(bot.respond("inicio"))

while True:
    print ("> ", end='')
    entrada = input()
    response = bot.respond(entrada)
    print(response)
    if entrada.upper() == "SAIR":
        break



