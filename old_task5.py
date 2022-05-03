# import datetime
#
# import requests
#
# from utils import fetch
# from constants import TOKEN, URL
#
# db = 'D:/task/new.db'
# DATE_FORMAT = '%d | %B | %Y'
# url = '{URL}/task_4'.format(URL=URL)
#
#
# def task_5():
#     # SELECT * FROM table//////////////////////////////////////////////////////
#     orders_data = fetch(db, table='Orders')
#     order_details_data = fetch(db, table="'Order Details'")
#
#     orders_detail = {}
#
#     for order_detail in order_details_data:
#         order_id = order_detail[0]
#         unit_price = order_detail[2]
#         quantity = order_detail[3]
#         discount = order_detail[4]
#         # Можно лучше||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||????????????????
#         if order_id not in orders_detail:
#             #     orders_detail[order_id].append((unit_price, quantity, discount))
#             # else:
#             #     orders_detail[order_id] = [(unit_price, quantity, discount)]
#             orders_detail[order_id] = []
#         orders_detail[order_id].append((unit_price, quantity, discount))
#
#     countries = {}
#     delays = {}
#     for order_data in orders_data:
#         datetime_order = datetime.datetime.fromisoformat(order_data[3])
#         if not datetime.datetime(1997, 7, 3) <= datetime_order <= datetime.datetime(1997, 12, 20):
#             continue
#
#         # format constant ////////////////////////////////////////////////////
#         date = datetime.datetime.strftime(datetime_order, DATE_FORMAT)
#         country = order_data[13]
#         city = order_data[10]
#         order_id = order_data[0]
#
#         coast = 0
#         for order_detail in orders_detail[order_id]:
#             unit_price = order_detail[0]
#             quantity = order_detail[1]
#             discount = order_detail[2]
#             # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#             if discount != 0:
#                 coast += unit_price * quantity * (1 - discount)
#             else:
#                 coast += unit_price * quantity
#         coast = round(coast, ndigits=2)
#
#         if country not in countries:
#             countries[country] = {}
#
#         # Можно лучше|||||||||||||||||||||||||||||||||||||||||||||||||||||
#         if city not in countries[country]:
#             countries[country][city] = {'delay_percent': 0, 'orders': []}
#         orders = countries[country][city]['orders']
#         orders.append(
#             {
#                 'date': date,
#                 'coast': coast
#             }
#         )
#
#         required_date = order_data[4]
#         shipped_date = order_data[5]
#         if shipped_date > required_date:
#             if country not in delays:
#                 delays[country] = {}
#             if city not in delays[country]:
#                 delays[country][city] = 1
#             else:
#                 delays[country][city] += 1
#
#     for delay in delays.items():
#         country = delay[0]
#         cities = delay[1]
#         for city in cities:
#             delay_percent = delays[country][city] / len(countries[country][city]['orders']) * 100
#             delay_percent = round(delay_percent)
#             countries[country][city]['delay_percent'] = delay_percent
#
#     response = requests.post(
#         url=url,
#         json={
#             'countries': countries
#         },
#         headers={
#             'Authorization': 'Token {TOKEN}'.format(TOKEN=TOKEN)
#         }
#     )
#     print(response.status_code)
#     if response.status_code // 100 != 2:
#         raise ConnectionError(f'Неудачный запрос, полученный ответ{response.text}')
#     print(response.text)




# Заебал этот гит ебанный сука
print('ЗАЕБАЛ ЭТОТ ГИТ ПОШЁЛ ОН НАХУЙ KEKW')

