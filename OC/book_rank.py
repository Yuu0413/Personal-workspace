from bs4 import BeautifulSoup
import requests

#初期URL
url = "https://bookmeter.com/rankings"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#ランキングのジャンルを取得
def get_book_genres():
    genres = []
    book_genre = soup.find_all('h3')
    for genre in book_genre:
        genres.append(genre.text)
    return genres

print(get_book_genres())