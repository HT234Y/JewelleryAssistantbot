from telebot import TeleBot
from telebot import types
from config import *

bot = TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    start_m = types.ReplyKeyboardMarkup(True, False)
    start_m.row('Покупки', 'Поддержка')
    bot.send_message(message.chat.id,
                     'Привет, %s!' % (message.from_user.first_name) + '\n' + txt[0],
                     reply_markup=start_m)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'Покупки' or message.text == '/pay':
        bot.send_message(message.chat.id, str(message.from_user.first_name) + txt[2], reply_markup=catalog())

    if message.text == 'Поддержка' or message.text == '/support':
        bot.send_message(message.chat.id, txt[1], reply_markup=geolocation())

    if message.text == 'Геолокация':
        bot.send_message(message.chat.id, txt[4])
        bot.send_location(message.chat.id, 46.47179, 30.73869)

    if [s for s in message.text if s in '@']:
        bot.send_message(message.chat.id, 'Спасибо, наш оператор в скором времени отправит посылку')
        bot.send_message(message.chat.id, txt[5], reply_markup=inline_delivery())

@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data == 'Купить':
        bot.send_message(call.message.chat.id, txt[3])
    if call.data == 'Кольца':
        bot.send_photo(call.message.chat.id,
                       open('img/0.jpg', 'rb'),
                       description[0],
                       reply_markup=inlineKeyboard())

        bot.send_photo(call.message.chat.id,
                       open('img/4.jpg', 'rb'),
                       description[4],
                       reply_markup=inlineKeyboard())

        bot.send_photo(call.message.chat.id,
                       open('img/8.jpg', 'rb'),
                       description[8],
                       reply_markup=inlineKeyboard())

    if call.data == 'Подвески':
        bot.send_photo(call.message.chat.id,
                       open('img/1.jpg', 'rb'),
                       description[1],
                       reply_markup=inlineKeyboard())

        bot.send_photo(call.message.chat.id,
                       open('img/6.jpg', 'rb'),
                       description[6],
                       reply_markup=inlineKeyboard())

    if call.data == 'Серьги':
        bot.send_photo(call.message.chat.id,
                       open('img/2.jpg', 'rb'),
                       description[2],
                       reply_markup=inlineKeyboard())

        bot.send_photo(call.message.chat.id,
                       open('img/5.jpg', 'rb'),
                       description[5],
                       reply_markup=inlineKeyboard())

    if call.data == 'Браслеты':
        bot.send_photo(call.message.chat.id,
                       open('img/3.jpg', 'rb'),
                       description[3],
                       reply_markup=inlineKeyboard())

        bot.send_photo(call.message.chat.id,
                       open('img/7.jpg', 'rb'),
                       description[7],
                       reply_markup=inlineKeyboard())

    if call.data == 'уркпочта':
        bot.send_message(
            call.message.chat.id,
            'Спасибо за заказ, вскоре ваш заказ будет отправлен через Укрпочту. Ожидайте реквизиты и штрих-код.')

    if call.data == 'новая почта':
        bot.send_message(
            call.message.chat.id,
            'Спасибо за заказ, вскоре ваш заказ будет отправлен через Новую почту. Ожидайте реквизиты и штрих-код.')


def inlineKeyboard():
    key = types.InlineKeyboardMarkup()
    buttPay = types.InlineKeyboardButton(text='Купить', callback_data='Купить')
    key.add(buttPay)
    return key

def geolocation():
    start_m = types.ReplyKeyboardMarkup(True, False)
    start_m.row('Покупки', 'Поддержка')
    start_m.row('Геолокация')
    return start_m

def inline_delivery():
    key = types.InlineKeyboardMarkup()
    buttUkrpochta = types.InlineKeyboardButton(text='Укрпочта', callback_data='уркпочта')
    buttNewpochta = types.InlineKeyboardButton(text='Новая почта', callback_data='новая почта')
    key.add(buttUkrpochta, buttNewpochta)
    return key

def catalog():
    key = types.InlineKeyboardMarkup()
    buttRings = types.InlineKeyboardButton(text='Кольца', callback_data='Кольца')
    buttEarrings = types.InlineKeyboardButton(text='Серьги', callback_data='Серьги')
    buttStakes = types.InlineKeyboardButton(text='Подвески', callback_data='Подвески')
    buttBracelets = types.InlineKeyboardButton(text='Браслеты', callback_data='Браслеты')
    key.add(buttRings, buttEarrings)
    key.add(buttStakes, buttBracelets)
    return key

if __name__ == '__main__':
    bot.polling(none_stop=True)