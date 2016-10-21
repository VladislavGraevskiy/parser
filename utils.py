import csv
from lxml import html
import requests

LIST_OF_FLATS = []


def pares(url):
    page = requests.get(url)
    p = page.json()
    #print(p)
    return p


def url_content(url):
    open_url = requests.get(url)
    doc1 = html.fromstring(open_url.content)
    return doc1


def create_list(address, rooms, price, link, date):
    LIST_OF_FLATS.append({
        'address': address.strip(),
        'rooms': rooms,
        'price': price,
        'link': link,
        'date': date
    })
    return LIST_OF_FLATS


def csv_file_writer(flats , path):
    with open(path, 'w') as csvfile:
        fieldnames = ['address', 'rooms', 'price', 'link', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for flat in flats:
            writer.writerow({'address': flat['address'],
                             'rooms': flat['rooms'],
                             'price': flat['price'],
                             'link': flat['link'],
                             'date': flat['date']
                             })
    print('File {} --- CREATE'.format(path))
