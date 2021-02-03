import requests
from bs4 import BeautifulSoup
import re

from bookstore.models import Books, Author


def database_update():
    url = f'http://fantasy-worlds.org/lib/1/'
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'lxml')
    find_id = soup.find_all('a', target="_blank")
    id = re.search('id\d+', str(find_id))[0][2:]
    if not Books.objects.exists():
        start_id = 1
        id = 2
    else:
        start_id = Books.objects.latest('id').id_book
        if start_id == 1:
            start_id = 2
    try:
        Books.objects.get(id_book=id)
    except Exception:
        for id_book in range(start_id, int(id)):
            url = f'http://fantasy-worlds.org/lib/id{id_book}/'
            page = requests.get(url).content
            soup = BeautifulSoup(page, 'lxml')
            find_id = soup.find_all('a', target="_blank")
            id_book = re.search('id\d+', str(find_id))[0][2:]
            if id_book != id:
                page = requests.get(url).content
                soup = BeautifulSoup(page, 'lxml')
                title = soup.find('span', itemprop="name").get_text(strip=True)
                author = soup.find('a', itemprop="author").get_text(strip=True)
                author = author.split(' ')
                description = soup.find('span',
                                        itemprop='description').get_text(
                    strip=True)
                isbn = soup.find('span', itemprop='isbn').get_text(strip=True)
                id_book = id_book
                image_number = re.search('\d+/\d+\.jpg', str(find_id))
                image_link = (
                    f'http://fantasy-worlds.org/img/full/{image_number[0]}'
                )
                book_link = url
                a = Author(
                    first_name=author[0],
                    last_name=author[1]
                )
                a.save()
                b = Books(
                    author=a,
                    title=title,
                    book_link=book_link,
                    description=description,
                    id_book=id_book,
                    image_link=image_link,
                    isbn=isbn
                )
                b.save()
