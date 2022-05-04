from task_4 import task_4
from task_5 import task_5
from utils import insert_into_tabla

DB = "D:\\pythonProject\\new.db"
params = {
    'categoryName': 'key3',
    'description': 'key2',
    'picture': 'key1'
}

table = 'Categories'

if __name__ == '__main__':
    task_5()
    # task_4(
    #     'Classical',
    #     'Pop',
    #     'Jazz'
    # )
    # insert_into_tabla(DB, table, params)
    # insert_into_tabla(
    #     'D:\\pythonProject\\new.db',
    #     "'Order Details'",
    #     params={
    #         'OrderID': 2059,
    #         'ProductID': 1,
    #         'UnitPrice': 12,
    #         'Quantity': 31,
    #         'Discount': 0.1,
    #     }
    # )
    # a = ['asdf', 'cc', '123', 'rrrrrr']
    # b = [i for i in a if len(i) > 3]
    # print(b)
    # a = input()

    