import telebot

TOKEN = "8382854520:AAHHwa2IARggV4Kuwbd9gFwVnBRgCwxBKxA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте.\n\n"
        "Вы написали в поддержку ImbaBuild.\n\n"
        "Команды:\n"
        "/support - связаться с поддержкой\n"
        "/report - сообщить о проблеме\n"
        "/payment - вопросы по оплате\n"
        "/account - помощь с аккаунтом\n"
        "/faq - часто задаваемые вопросы"
    )

@bot.message_handler(commands=['support'])
def support(message):
    bot.send_message(message.chat.id, "Опишите вашу проблему. Поддержка ответит позже.")

@bot.message_handler(commands=['report'])
def report(message):
    bot.send_message(message.chat.id, "Опишите найденную ошибку или проблему.")

@bot.message_handler(commands=['payment'])
def payment(message):
    bot.send_message(message.chat.id, "Укажите способ оплаты и проблему.")

@bot.message_handler(commands=['account'])
def account(message):
    bot.send_message(message.chat.id, "Опишите проблему с аккаунтом.")

@bot.message_handler(commands=['faq'])
def faq(message):
    bot.send_message(message.chat.id, "FAQ:\n1. Как купить?\n2. Почему не проходит оплата?\n3. Как восстановить аккаунт?")

@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Если вы отправляли обращение, поддержка ответит в этом чате.")

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, "Связь с поддержкой: @ImbaBuild")

@bot.message_handler(func=lambda m: True)
def auto(message):
    bot.send_message(message.chat.id, "Сообщение получено. Поддержка ответит позже.")

bot.infinity_polling()
