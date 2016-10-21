import utils


def page_count(json_date):
    last_page = json_date['page']['last']
    return last_page


def json_parse(json_date):

    for i in range(int(json_date['page']['items'])):
        flat = json_date['apartments'][i]
        address = flat['location']['address']
        room = flat['rent_type'].split('_')[0]
        price = flat['price']['amount']
        link = flat['url']
        date = flat['last_time_up']
        print(address, room, price, link, date)
        arg = [address, room, price, link, date]
        utils.create_list(*arg)


def run():
    url = 'https://ak.api.onliner.by/search/apartments{}'
    json_date = utils.pares(url.format('/'))
    last_page = page_count(json_date)

    for i in range(1, last_page):
        json_parse(utils.pares(url.format('?page='+str(i))))
    utils.csv_file_writer(utils.LIST_OF_FLATS, 'onliner.csv')