import telebot
import requests
from auth_data import token
from telebot import types


def telegram_bot(token):


    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=['start'])
    def get_user_question(message):
        markup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='YES', callback_data='yes')

        markup_inline.add(item_yes)
        bot.send_message(message.chat.id, 'Hi, would you like to see the latest news?',
                         reply_markup=markup_inline)


    @bot.callback_query_handler(func = lambda call: True)
    def start_message(call):
        if call.data == 'yes':
            bot.send_message(call.message.chat.id, "Hi, here's the popular news lately")

            url = ('https://newsapi.org/v2/top-headlines?'
                   'country=us&'
                   'apiKey=888eab95d48848cd9a3baaeeb44e3c87')

            try:
                req = requests.get(url)
                response = req.json()
                for article in response['articles']:
                    author = article['author']
                    title =article['title']
                    description = article['description']
                    url_news = article['url']

                    bot.send_message(call.message.chat.id, f'\U0001F468Author: {author}\n'
                                    f'\U0001F4F0Title: {title}\n'
                                    f'\U0001F4DCDescription: {description}\n'
                                    f'\U0001F310See more: {url_news}\n\n\n'
                                    )
            except Exception as ex:
                print(ex)
                bot.send_message(call.message.chat.id, 'Check valid of date')
        else:
            bot.send_message(call.chat.id, 'ok')


    @bot.message_handler(commands=['start_bot'])
    def start_bot(message):
        markup = types.ReplyKeyboardMarkup()
        item_start = types.KeyboardButton('/start')
        markup.row(item_start)

        bot.send_message(message.chat.id, 'Bot started!', reply_markup=markup)

    bot.polling()




if __name__ == '__main__':
    telegram_bot(token)