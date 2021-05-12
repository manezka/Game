import telebot
from config import TOKEN, keys
from extensions import ConverterException, Convertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в след формате: \n<имя валюты> \
<Имя валюты, в котрой в которой надо узнать цену первой валюты> \
<количество первой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in keys.keys():
        text += key + '\n'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConverterException('Неверное количество параметров.')
        quote, base, amount = values

        total = Convertor.get_price(quote, base, amount)
    except ConverterException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total} {keys[base]}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)