import datetime

import requests

from utils import fetch, get_all_from_table
from constants import TOKEN, URL

DB = 'D:/task/new.db'
DATE_FORMAT = '%d | %B | %Y'
url = '{URL}/task_4'.format(URL=URL)


def task_5():
    # SELECT * FROM table//////////////////////////////////////////////////////
    orders_data = get_all_from_table(DB, table='Orders')
    order_details_data = get_all_from_table(DB, table="'Order Details'")

    orders_coast = {}

    for order_detail in order_details_data:
        order_id = order_detail[0]
        unit_price = order_detail[2]
        quantity = order_detail[3]
        discount = order_detail[4]
        # Можно лучше///////////////////////////////////////////////////////////////
        if order_id not in orders_coast:
            orders_coast[order_id] = unit_price * quantity * (1 - discount)
            continue
        orders_coast[order_id] += unit_price * quantity * (1 - discount)

    countries = {}
    delays = {}
    for order_data in orders_data:
        datetime_order = datetime.datetime.fromisoformat(order_data[3])
        if not datetime.datetime(1997, 7, 3) <= datetime_order <= datetime.datetime(1997, 12, 20):
            continue

        # format constant ////////////////////////////////////////////////////
        date = datetime.datetime.strftime(datetime_order, DATE_FORMAT)
        country = order_data[13]
        city = order_data[10]
        order_id = order_data[0]

        coast = round(orders_coast[order_id], ndigits=2)

        if country not in countries:
            countries[country] = {}
        #     countries_1 ?????????????????
        countries_1 = countries[country]
        # Можно лучше////////////////////////////////////////////////////////
        if city not in countries_1:
            countries_1[city] = {'delay_percent': 0, 'orders': []}
        #     ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        countries_2 = countries_1[city]
        orders = countries_2['orders']
        orders.append(
            {
                'date': date,
                'coast': coast
            }
        )

        required_date = order_data[4]
        shipped_date = order_data[5]
        if shipped_date > required_date:
            if country not in delays:
                delays[country] = {}
            if city not in delays[country]:
                delays[country][city] = 0

            delays[country][city] += 1

    for delay in delays.items():
        country = delay[0]
        cities = delay[1]
        for city in cities:
            delay_percent = delays[country][city] / len(countries[country][city]['orders']) * 100
            delay_percent = round(delay_percent)
            countries[country][city]['delay_percent'] = delay_percent

    response = requests.post(
        url=url,
        json={
            'countries': countries
        },
        headers={
            'Authorization': 'Token {TOKEN}'.format(TOKEN=TOKEN)
        }
    )
    print(response.status_code)
    if response.status_code // 100 != 2:
        raise ConnectionError(f'Неудачный запрос, полученный ответ{response.text}')
    print(response.text)
