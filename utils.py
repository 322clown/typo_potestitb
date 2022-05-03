import sqlite3


def fetch(db_path: str, sql) -> list:
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor_execute = cursor.execute(sql)
    return cursor_execute.fetchall()


def get_all_from_table(db_path, table):
    return fetch(db_path, 'SELECT * FROM {}'.format(table))


def get_data_from_table(db_path: str, table: str, fields: list) -> list:
    fields_str = ', '.join(fields)
    return fetch(db_path, f'SELECT {fields_str} from {table}')


def insert_into_tabla(db_path, table, params: dict):
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        fields_names = ', '.join(params.keys())
        # fields_values = ', '.join((lambda i: f"'{i}'")(i) for i in params.values())
        # fields_values = ', '.join((lambda i: f"'{i}'" if type(i) == str else f"{i}")(i) for i in params.values())
        fields_values = ', '.join([f"'{i}'" if isinstance(i, str) else str(i) for i in params.values()])
        # isinstance()
        print(params.values())
        print(fields_values)
        print(f"INSERT INTO {table}({fields_names}) VALUES({fields_values})")
        # cursor_execute = cursor.execute(f"INSERT INTO {table}({fields_names}) VALUES({fields_values})")
        # db.commit()

