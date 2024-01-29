import telebot
import weather

tgApiKey = open("telegramapikey.txt", "r").read()
weatherApiKey = open("weatherapikey.txt", "r").read()

bot = telebot.TeleBot(tgApiKey)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Я здесь...")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    #print(message)
    if message.text.strip() == 'погода':
        answer_json = weather.getWeather('Moscow', weatherApiKey)
        answer = f'Погода в городе {answer_json["city"]}, feels_like: {answer_json["feels_like"]}'
        bot.send_message(message.chat.id, answer)

bot.infinity_polling()
