import utils


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
            utils.create_list(address.strip(), rooms, price, link, date)
        except IndexError:
            continue


def run():
    num = int(page_count(utils.url_content("http://www.kvartirant.by/ads/flats/type/rent/"))[0])
    for d in range(num+1):
        parse(utils.url_content("http://www.kvartirant.by/ads/flats/type/rent/page/{}/".format(d)))
    utils.csv_file_writer(utils.LIST_OF_FLATS, 'names.csv')