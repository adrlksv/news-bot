import requests
from pprint import pprint


url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=888eab95d48848cd9a3baaeeb44e3c87')

def get_data():
    req = requests.get(url)
    response = req.json()
    #pprint(response)
    for article in response['articles']:
        author = article['author']
        title =article['title']
        description = article['description']
        url_news = article['url']

        print(f'Author: {author}\n'
            f'Title: {title}\n'
            f'{description}\n'
            f'See more: {url_news}\n\n\n'
            )

if __name__ == '__main__':
    get_data()