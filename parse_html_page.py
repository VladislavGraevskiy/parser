
import requests
from lxml import html
import csv
list_of_flats = []


def page_count(url_contents):
    return url_contents.xpath('//div[@class="pages-nums"]/select/option[last()]/text()')


def parse(url_contents):
    flats = url_contents.xpath('//div[@class="adtxt_box"]')

    for key, i in enumerate(flats):
        try:
            address = i.xpath('//span[@class="rooms"]/text()')[key]
            rooms = i.xpath('//span[@class="rooms-box type-3"]/text()')[key]
            price = i.xpath('//span[@class="price-box currency-840"]/text()')[key]
            link = i.xpath('//p[@class="title"]/a/@href')[key]
            date = i.xpath('//p[@class="date"]/text()')[key]
            print(address.strip(), rooms, price, link, date)
            list_of_flats.append({
                                'address': address.strip(),
                                'rooms': rooms,
                                'price': price,
                                'link': link,
                                'date': date
                                 })

        except IndexError:
            continue
        csv_file_writer(list_of_flats)


def csv_file_writer(flats):
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['address', 'rooms', 'price', 'link', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for flat in flats:
            writer.writerow({'address':flat['address'],
                             'rooms':flat['rooms'],
                             'price':flat['price'],
                             'link':flat['link'],
                             'date':flat['date']
                             })


def url_content(url):
    open_url = requests.get(url)
    doc1 = html.fromstring(open_url.content)
    return doc1


if __name__ == "__main__":
    try:
        num = int(input("Input num of page(Press ENTER to continue whith default data):"))
    except ValueError:
        num = ''
    if not num:
        num = int(page_count(url_content("http://www.kvartirant.by/ads/flats/type/rent/"))[0])
    for d in range(num+1):
        parse(url_content("http://www.kvartirant.by/ads/flats/type/rent/page/{}/".format(d)))