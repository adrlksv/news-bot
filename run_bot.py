import telebot
import requests
from auth_data import token


def telegram_bot(token):


    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hi, here's the popular news lately")

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

                bot.send_message(message.chat.id, f'\U0001F468Author: {author}\n'
                                f'\U0001F4F0Title: {title}\n'
                                f'\U0001F4DCDescription: {description}\n'
                                f'\U0001F310See more: {url_news}\n\n\n'
                                )
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, 'Check valid of date')

    bot.polling()




if __name__ == '__main__':
    telegram_bot(token)